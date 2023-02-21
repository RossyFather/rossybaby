from django.http import HttpResponse
from django.shortcuts import render


def rossy(request):
    context          = {}
    context['Rossy Title'] = 'Hello Rossy'
    return render(request, 'rossy.html', context)
