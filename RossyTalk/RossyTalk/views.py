from django.http import HttpResponse
from django.shortcuts import render


def rossy(request):
    views_name = 'Rossybaby'
    return render(request, 'rossy.html', {'name': views_name})
