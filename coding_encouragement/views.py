from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q
from .models import Quote, Report
from .forms import QuoteSubmissionForm
import random

# Create your views here.
def home(request):
    # Get a random approved quote that's not hidden
    approved_quotes = Quote.objects.filter(is_approved=True, is_hidden=False)
    
    if approved_quotes.exists():
        random_quote = random.choice(approved_quotes)
        context = {
            'quote': random_quote,
            'total_quotes': approved_quotes.count()
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
