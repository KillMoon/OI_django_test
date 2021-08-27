from django.forms import ModelForm

from impresses.models import Impress


class ImpressForm(ModelForm):
    """Форма ввода для модели Impress"""
    class Meta:
        model = Impress
        fields = ('name', 'info', 'location', 'address')
asd
