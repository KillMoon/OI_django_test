from django.urls import path

from impresses.views import home_page, CreateImpress

urlpatterns = [
    path('', home_page, name='homePage'),
    path('add/', CreateImpress.as_view(), name='add')
]
