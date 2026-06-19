from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('teams/', views.teams, name='teams'),
    path('players/', views.players, name='players'),

    path('groups/', views.groups, name='groups'),
    path('live-scores/', views.live_scores, name='live_scores'),
    path('live-scores/', views.live_scores, name='live_scores'),
    path('api/live-scores/', views.live_scores_api, name='live_scores_api'),


    path('live-standings/', views.live_standings, name='live_standings'),

    path('team/<int:id>/', views.team_detail, name='team_detail'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('knockout/', views.knockout, name='knockout'),
    path(
    'top-scorers/',
    views.top_scorers,
    name='top_scorers'
),

path('contact/', views.contact, name='contact'),
path('about/', views.about, name='about'),
path('privacy/', views.privacy, name='privacy'),
path('robots.txt', views.robots_txt),

  
]