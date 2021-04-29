from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from impresses.forms import ImpressForm
from impresses.models import Impress, Profile


def home_page(request):
    """Контроллер(представление) для главной страницы"""
    context = {}
    if request.user.is_authenticated:
        impresses = Impress.objects.filter(profile__user=request.user)
        profile = Profile.objects.get(user=request.user)
        context = {'impresses': impresses, 'profile': profile}
    return render(request, 'impresses/homePage.html', context)


class CreateImpress(CreateView):
    """Контроллер для создание нового объекта Impress"""
    template_name = 'impresses/create.html'
    form_class = ImpressForm
    success_url = reverse_lazy('homePage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        try:
            profile = Profile.objects.get(user=self.request.user)
            self.object.profile = profile
        except BaseException:
            pass
        self.object.save()
        return super().form_valid(form)


def conf_view(request):
    """Контроллер для вывода правил конфиденциальности"""
    return render(request, 'impresses/conf.html')


def cons_view(request):
    """Контроллер для вывода пользовательского соглашения """
    return render(request, 'impresses/cons.html')
