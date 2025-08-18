from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_quote, name='submit_quote'),
    path('my-quotes/', views.my_quotes, name='my_quotes'),
    path('my-votes/', views.my_votes, name='my_votes'),
    path('all-quotes/', views.all_quotes, name='all_quotes'),
    path('vote/<int:quote_id>/', views.vote_quote, name='vote_quote'),
    path('report/<int:quote_id>/', views.report_quote, name='report_quote'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
