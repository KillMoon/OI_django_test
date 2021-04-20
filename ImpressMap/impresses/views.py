from django.shortcuts import render

from impresses.models import Impress


def home_page(request):
    """Контроллер(представление) для главной страницы"""
    impresses = Impress.objects.all()
    context = {'impresses': impresses}
    return render(request, 'impresses/homePage.html', context)

