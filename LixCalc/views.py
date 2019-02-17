from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TeksterForm


def lixCalc(request):
    context = {
        'stylesheetcss': 'bootstrap.css',
        'stylesheetjs': 'bootstrap.js',
    }
    if request.method == 'POST':
        form = TeksterForm(request.POST)
        if form.is_valid():
            return render(request,'index.html', context)
        else:
            form = TeksterForm()

        return render(request, 'lixCalc/lixCalc.html',context)

    return render(request, 'LixCalc/lixCalc.html', context)

