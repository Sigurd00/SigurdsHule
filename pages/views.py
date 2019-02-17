from django.shortcuts import render
from .models import Projekter
import os
# Create your views here.
# pages views


def index(request):
    context = {
        'stylesheetcss': 'bootstrap.css',
        'stylesheetjs': 'bootstrap.js',
        'title': 'Sigurds Hule',
        'hjem': 'active',
    }
    return render(request, 'index.html', context)


def visprojekter(request, trin):

    projekter = Projekter.objects.all()
    context = {
        'stylesheetcss': 'bootstrap.css',
        'stylesheetjs': 'bootstrap.js',
        'project': 'active',
        'title': '',
        '1g': '',
        '2g': '',
        '3g': '',
        'projekter': projekter,
        'trin': trin
    }

    if trin == 1:
        context['1g'] = 'active'
        context['title'] = 'Første år i gymnasiet'
    if trin == 2:
        context['2g'] = 'active'
        context['title'] = 'Andet år i gymnasiet'
    if trin == 3:
        context['3g'] = 'active'
        context['title'] = 'Tredje år i gymnasiet'

    return render(request, 'projects.html', context)


def viewproject(request, trin, title):

    projekt = Projekter.objects.get(title=title)

    context = {
        'stylesheetcss': 'bootstrap.css',
        'stylesheetjs': 'bootstrap.js',
        'project': 'active',
        '1g': '',
        '2g': '',
        '3g': '',
        'trin': trin,
        'projekt': projekt,

    }
    if trin == 1:
        context['1g'] = 'active'
        context['title'] = 'Første år i gymnasiet'
    if trin == 2:
        context['2g'] = 'active'
        context['title'] = 'Andet år i gymnasiet'
    if trin == 3:
        context['3g'] = 'active'
        context['title'] = 'Tredje år i gymnasiet'

    return render(request, 'showProject.html', context)
