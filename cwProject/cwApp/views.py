from django.shortcuts import render


# Create your views here.
def index(request, link):
    return render(request, 'cwApp/index.html', {'link': link})


def base(request, link):
    return render(request, 'cwApp/Base.html', {'link': link})


def about(request, link):
    return render(request, 'cwApp/About.html', {'link': link})
