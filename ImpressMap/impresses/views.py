from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from impresses.forms import ImpressForm
from impresses.models import Impress


def home_page(request):
    """Контроллер(представление) для главной страницы"""
    context = {}
    if request.user.is_authenticated:
        impresses = Impress.objects.filter(user=request.user)
        context = {'impresses': impresses}

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
            self.object.user = self.request.user
        except BaseException:
            pass
        self.object.save()
        return super().form_valid(form)
