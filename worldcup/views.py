from urllib import request

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from collections import defaultdict
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Team, Player, Match, News, Highlight
from .services import get_standings, get_live_matches

from .models import News, Highlight
from .utils import get_live_matches

def home(request):
    news = News.objects.all().order_by('-id')
    highlights = Highlight.objects.all().order_by('-id')

    matches = get_live_matches()

    match_of_day = None

    if matches:

        # Live match first
        live_matches = [
            m for m in matches
            if m.get('status') in ['IN_PLAY', 'PAUSED']
        ]

        if live_matches:
            match_of_day = live_matches[0]

        else:

            # Upcoming match
            upcoming_matches = [
                m for m in matches
                if m.get('status') in ['SCHEDULED', 'TIMED']
            ]

            if upcoming_matches:
                match_of_day = upcoming_matches[0]

            else:
                # Fallback
                match_of_day = matches[0]

    return render(
        request,
        'worldcup/home.html',
        {
            'news': news,
            'highlights': highlights,
            'match_of_day': match_of_day,
        }
    )


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
    return render(request, 'worldcup/team_detail.html', {'team': team, 'players': players})

def groups(request):
    teams = Team.objects.all()
    groups_dict = defaultdict(list)
    for t in teams:
        groups_dict[t.group].append(t)
    return render(request, 'worldcup/groups.html', {'groups': groups_dict})

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'worldcup/news_detail.html', {'news': news})

def live_standings(request):
    data = get_standings()
    standings_list = data.get("standings", []) if data else []
    return render(request, "worldcup/live_standings.html", {"standings": standings_list})

def live_scores(request):
    return render(request, "worldcup/live_scores.html")

def live_scores_api(request):
    matches = get_live_matches()
    return JsonResponse(matches, safe=False)

def send_score_update(html_data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "scores",
        {
            "type": "score_update",
            "data": {"html": html_data}
        }
    )


from .models import Knockout
from django.shortcuts import render

def knockout(request):

    round16 = Knockout.objects.filter(stage='R16')
    quarter = Knockout.objects.filter(stage='QF')
    semi = Knockout.objects.filter(stage='SF')
    final = Knockout.objects.filter(stage='F')

    return render(
        request,
        'worldcup/knockout.html',
        {
            'round16': round16,
            'quarter': quarter,
            'semi': semi,
            'final': final,
        }
    )


from .models import TopScorer

def top_scorers(request):
    scorers = TopScorer.objects.all().order_by('-goals', '-assists')

    return render(
        request,
        'worldcup/top_scorers.html',
        {'scorers': scorers}
    )



def contact(request):
    return render(request, 'worldcup/contact.html')


def about(request):
    return render(request, 'worldcup/about.html')

def privacy(request):
    return render(request, 'worldcup/privacy.html')


from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://fifa-0a6i.onrender.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")