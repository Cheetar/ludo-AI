from django.shortcuts import render
from .models import Contest


def contests_list(request):
    contests = Contest.objects.all()
    return render(request, "contest/contests_list.html", { 'contests': contests })

def show_contest(request, id):
    contest = Contest.objects.get(id=id)
    return render(request, "contest/show_contest.html", { 'contest': contest })
