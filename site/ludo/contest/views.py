from django.shortcuts import render, get_object_or_404
from .models import Contest


def contests_list(request):
    contests = Contest.objects.all()
    return render(request, "contest/contests_list.html", { 'contests': contests })

def show_contest(request, id):
    contest = get_object_or_404(Contest, pk=id)#Contest.objects.get(id=id)
    participants = contest.participants.all()

    if request.method == "POST":
        if request.POST.get("play_game"):
            contest.game()
        elif request.POST.get("contest"):
            for i in range(100):
                contest.game()


    return render(request, "contest/show_contest.html", { 'contest': contest,
                                                          'participants': participants })
