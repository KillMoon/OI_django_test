from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from social_core.pipeline import user

from impresses.forms import ImpressForm
from impresses.models import Impress


def home_page(request):
    """Контроллер(представление) для главной страницы"""
    impresses = Impress.objects.all()
    context = {'impresses': impresses}
    print()
    return render(request, 'impresses/homePage.html', context)


class CreateImpress(CreateView):
    """Контроллер для создание нового объекта Impress"""
    template_name = 'impresses/create.html'
    form_class = ImpressForm
    success_url = reverse_lazy('homePage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

