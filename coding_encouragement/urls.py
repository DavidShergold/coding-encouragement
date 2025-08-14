from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_quote, name='submit_quote'),
    path('my-quotes/', views.my_quotes, name='my_quotes'),
    path('signup/', views.signup, name='signup'),
]
