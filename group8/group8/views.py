from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'homePage.html', {})

def biography(request):
    return render(request, 'biography.html', {})

def Discography(request):
    return render(request, 'discography.html', {})

def Tour(request):
    return render(request, 'Tour.html', {})

def SocialMedia(request):
    return render(request, 'SocialMedia.html', {})

def upcoming(request):
    return render(request, 'SocialMedia.html', {})
