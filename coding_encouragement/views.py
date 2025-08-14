from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q
from .models import Quote
from .forms import QuoteSubmissionForm
import random

# Create your views here.
def home(request):
    # Get a random approved quote
    approved_quotes = Quote.objects.filter(is_approved=True)
    
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
            quote.save()
            messages.success(request, 'Your motivational quote has been submitted successfully! 🎉')
            return redirect('home')
    else:
        form = QuoteSubmissionForm()
    
    return render(request, 'coding_encouragement/submit_quote.html', {'form': form})

def my_quotes(request):
    if request.user.is_authenticated:
        user_quotes = Quote.objects.filter(submitted_by=request.user)
        context = {
            'quotes': user_quotes,
            'total_count': user_quotes.count()
        }
        return render(request, 'coding_encouragement/my_quotes.html', context)
    else:
        return redirect('login')

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
