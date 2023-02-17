from django.http import HttpResponse


def rossy(request):
    context = {}
    context['hello'] = 'Hello Rossy'
    return
