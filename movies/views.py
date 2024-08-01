from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    context: dict = {
        'movies': ['deadpool', 'deadpool 2', 'deadpool and wolverine']
    }
    return render(request, 'movies/index.html', context)

def about(request) -> HttpResponse:
    return render(request, 'movies/about.html', {'first_name': 'Alex'})


""" NOTE: This is how the template file dirs work"""
# app/template/app/index.html
# movies/template/movies/index.html

