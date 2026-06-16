from django.shortcuts import render, get_object_or_404
from collections import defaultdict
from .models import Team, Player, Match,Team,News

from .models import Team, Player, Match, News

from .models import Highlight

def home(request):
    news = News.objects.all()
    highlights = Highlight.objects.all()

    return render(request, 'worldcup/home.html', {
        'news': news,
        'highlights': highlights
    })


def teams(request):
    teams = Team.objects.all()
    return render(request, 'worldcup/teams.html', {'teams': teams})

def players(request):
    players = Player.objects.all()
    return render(request, 'worldcup/players.html', {'players': players})

def standings(request):
    teams = Team.objects.all().order_by('-points')
    return render(request, 'worldcup/standings.html', {'teams': teams})

def team_detail(request, id):
    team = get_object_or_404(Team, id=id)
    players = Player.objects.filter(team=team)

    return render(
        request,
        'worldcup/team_detail.html',
        {
            'team': team,
            'players': players
        }
    )


def groups(request):
    teams = Team.objects.all()

    groups = defaultdict(list)

    for t in teams:
        groups[t.group].append(t)

    return render(request, 'worldcup/groups.html', {
        'groups': groups
    })


def news_detail(request, id):
    news = News.objects.get(id=id)
    return render(request, 'worldcup/news_detail.html', {'news': news})

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_score_update(html_data):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "scores",
        {
            "type": "score_update",
            "data": {
                "html": html_data
            }
        }
    )




from django.shortcuts import render
from .services import get_standings

def live_standings(request):
    data = get_standings()

    standings = []

    if data:
        standings = data.get("standings", [])

    return render(
        request,
        "worldcup/live_standings.html",
        {"standings": standings}
    )


from django.shortcuts import render
from django.http import JsonResponse
from .services import get_live_matches

def live_scores(request):

    return render(
        request,
        "worldcup/live_scores.html"
    )

def live_scores_api(request):

    matches = get_live_matches()

    return JsonResponse(matches, safe=False)



