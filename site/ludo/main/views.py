from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import SubmitNewSolution
from .models import Code
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "main/user.html", { 'id':id, 'user':user })

def home(request):
    return render(request, "main/home.html", {})

@login_required
def submit(request):
    if request.method == 'POST':
        form = SubmitNewSolution(request.POST)

        if form.is_valid():
            t = form.cleaned_data['title']
            c = form.cleaned_data['code']
            a = request.user#???
            code = Code(author=a, title=t, code=c)
            code.save()
            #request.user.code_ser.create(title=t, code=c)
            return HttpResponseRedirect('/%i' %a.id)

    form = SubmitNewSolution()
    return render(request, "main/submit.html", {'title':'Submit code', 'form':form })
