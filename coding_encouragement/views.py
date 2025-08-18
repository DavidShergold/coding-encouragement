from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db.models import Q, Count, Case, When, IntegerField
from django.core.paginator import Paginator
from .models import Quote, Report, Vote
from .forms import QuoteSubmissionForm
import random

# Create your views here.
def home(request):
    # Get a random approved quote that's not hidden
    approved_quotes = Quote.objects.filter(is_approved=True, is_hidden=False)
    
    if approved_quotes.exists():
        random_quote = random.choice(approved_quotes)
        
        # Get user's vote for this quote if authenticated
        user_vote = None
        if request.user.is_authenticated:
            user_vote = random_quote.get_user_vote(request.user)
        
        context = {
            'quote': random_quote,
            'total_quotes': approved_quotes.count(),
            'user_vote': user_vote
        }
        return render(request, 'coding_encouragement/home.html', context)
    else:
        # No quotes yet, show welcome message
        context = {
            'quote': None,
            'message': "Welcome to Coding Encouragement! 🚀 Be the first to submit a motivational quote!"
        }
        return render(request, 'coding_encouragement/home.html', context)

@login_required
def submit_quote(request):
    if request.method == 'POST':
        form = QuoteSubmissionForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.submitted_by = request.user
            quote.is_approved = False  # New quotes require approval
            quote.save()
            messages.success(request, 'Your motivational quote has been submitted successfully! 🎉 It will appear once approved by our moderators.')
            return redirect('home')
    else:
        form = QuoteSubmissionForm()
    
    return render(request, 'coding_encouragement/submit_quote.html', {'form': form})

def my_quotes(request):
    if request.user.is_authenticated:
        user_quotes = Quote.objects.filter(submitted_by=request.user)
        approved_count = user_quotes.filter(is_approved=True, is_hidden=False).count()
        pending_count = user_quotes.filter(is_approved=False).count()
        hidden_count = user_quotes.filter(is_hidden=True).count()
        
        context = {
            'quotes': user_quotes,
            'total_count': user_quotes.count(),
            'approved_count': approved_count,
            'pending_count': pending_count,
            'hidden_count': hidden_count,
        }
        return render(request, 'coding_encouragement/my_quotes.html', context)
    else:
        return redirect('login')

@login_required
def report_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    
    if request.method == 'POST':
        reason = request.POST.get('reason')
        description = request.POST.get('description', '')
        
        # Check if user already reported this quote
        existing_report = Report.objects.filter(quote=quote, reported_by=request.user).first()
        if existing_report:
            messages.warning(request, 'You have already reported this quote.')
            return redirect('home')
        
        # Create the report
        report = Report.objects.create(
            quote=quote,
            reported_by=request.user,
            reason=reason,
            description=description
        )
        
        # Check if quote should be auto-hidden
        quote.check_auto_hide()
        
        messages.success(request, 'Thank you for reporting this quote. Our moderators will review it.')
        return redirect('home')
    
    # For GET requests, show the reporting form
    context = {
        'quote': quote,
        'report_reasons': Report.REPORT_REASONS
    }
    return render(request, 'coding_encouragement/report_quote.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Coding Encouragement, {user.username}! 🎉')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

def user_logout(request):
    """Handle user logout with success message"""
    if request.method == 'POST':
        username = request.user.username if request.user.is_authenticated else "User"
        logout(request)
        messages.success(request, f"👋 Goodbye {username}! You've been successfully logged out.")
        return redirect('home')
    return redirect('home')

@login_required
def vote_quote(request, quote_id):
    """Handle voting on quotes via AJAX"""
    if request.method == 'POST':
        quote = get_object_or_404(Quote, id=quote_id)
        vote_type = request.POST.get('vote_type')
        
        if vote_type not in ['up', 'down']:
            return JsonResponse({'error': 'Invalid vote type'}, status=400)
        
        # Get or create the vote
        vote, created = Vote.objects.get_or_create(
            quote=quote,
            user=request.user,
            defaults={'vote_type': vote_type}
        )
        
        if not created:
            if vote.vote_type == vote_type:
                # Same vote - remove it (toggle off)
                vote.delete()
                current_vote = None
            else:
                # Different vote - update it
                vote.vote_type = vote_type
                vote.save()
                current_vote = vote_type
        else:
            current_vote = vote_type
        
        # Return updated vote counts
        return JsonResponse({
            'cumulative_rank': quote.get_cumulative_rank(),
            'current_vote': current_vote
        })
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def all_quotes(request):
    """Display all quotes with sorting and pagination"""
    # Get sorting parameter
    sort_by = request.GET.get('sort', 'newest')
    
    # Get all approved, non-hidden quotes
    quotes = Quote.objects.filter(is_approved=True, is_hidden=False)
    
    # Apply sorting
    if sort_by == 'oldest':
        quotes = quotes.order_by('created_at')
    elif sort_by == 'highest_ranked':
        # Annotate with vote counts and sort by cumulative rank
        quotes = quotes.annotate(
            upvotes=Count('votes', filter=Q(votes__vote_type='up')),
            downvotes=Count('votes', filter=Q(votes__vote_type='down')),
            cumulative_rank=Count('votes', filter=Q(votes__vote_type='up')) - Count('votes', filter=Q(votes__vote_type='down'))
        ).order_by('-cumulative_rank', '-created_at')
    elif sort_by == 'lowest_ranked':
        # Sort by lowest rank first
        quotes = quotes.annotate(
            upvotes=Count('votes', filter=Q(votes__vote_type='up')),
            downvotes=Count('votes', filter=Q(votes__vote_type='down')),
            cumulative_rank=Count('votes', filter=Q(votes__vote_type='up')) - Count('votes', filter=Q(votes__vote_type='down'))
        ).order_by('cumulative_rank', '-created_at')
    else:  # newest (default)
        quotes = quotes.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(quotes, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Add user vote information for each quote if user is authenticated
    if request.user.is_authenticated:
        for quote in page_obj:
            quote.user_vote = quote.get_user_vote(request.user)
    
    context = {
        'page_obj': page_obj,
        'current_sort': sort_by,
        'sort_options': [
            ('newest', 'Newest First'),
            ('oldest', 'Oldest First'),
            ('highest_ranked', 'Highest Ranked'),
            ('lowest_ranked', 'Lowest Ranked'),
        ]
    }
    
    return render(request, 'coding_encouragement/all_quotes.html', context)

@login_required
def my_votes(request):
    """Display all quotes the user has voted on with filtering and sorting"""
    # Get filter and sort parameters
    vote_filter = request.GET.get('filter', 'all')  # all, up, down
    sort_by = request.GET.get('sort', 'recent_vote')
    
    # Get all votes by the current user
    user_votes = Vote.objects.filter(user=request.user).select_related('quote')
    
    # Apply vote filter
    if vote_filter == 'up':
        user_votes = user_votes.filter(vote_type='up')
    elif vote_filter == 'down':
        user_votes = user_votes.filter(vote_type='down')
    # 'all' includes both up and down votes
    
    # Apply sorting
    if sort_by == 'oldest_vote':
        user_votes = user_votes.order_by('created_at')
    elif sort_by == 'newest_quote':
        user_votes = user_votes.order_by('-quote__created_at')
    elif sort_by == 'oldest_quote':
        user_votes = user_votes.order_by('quote__created_at')
    else:  # recent_vote (default)
        user_votes = user_votes.order_by('-updated_at', '-created_at')
    
    # Pagination
    paginator = Paginator(user_votes, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Add user vote information for each quote
    for vote in page_obj:
        vote.quote.user_vote = vote.vote_type
        vote.quote.vote_date = vote.updated_at or vote.created_at
    
    context = {
        'page_obj': page_obj,
        'current_filter': vote_filter,
        'current_sort': sort_by,
        'filter_options': [
            ('all', 'All Votes'),
            ('up', 'Likes Only'),
            ('down', 'Dislikes Only'),
        ],
        'sort_options': [
            ('recent_vote', 'Recently Voted'),
            ('oldest_vote', 'Oldest Votes'),
            ('newest_quote', 'Newest Quotes'),
            ('oldest_quote', 'Oldest Quotes'),
        ]
    }
    
    return render(request, 'coding_encouragement/my_votes.html', context)
