from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from django.contrib.auth import login
from .forms import SignUpForm

def film_list(request):
    html = """
    {% load static %}
    <html><head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
    <h1>Film Explorer</h1>
    </body></html>
    """
    return HttpResponse(html)

def film_list_template(request):
    films = ["Inception", "Interstellar", "The Matrix"]
    return render(request, "films02_list.html", {"films": films})

def film_detail(request, slug): 
    film = get_object_or_404(Film, slug=slug)
    return render(request, 'film_detail.html', {'film': film})

def films04_db(request):
    films = Film.objects.all()
    return render(request, 'films02_list.html', {"films": films})

def films05_with_links(request):
    films = Film.objects.all()
    return render(request, 'films04_list.html', {"films": films})

def films06_datatable(request):
    films = Film.objects.all()
    return render(request, 'films05_list.html', {"films": films})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('films07') 
        else:
            form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})