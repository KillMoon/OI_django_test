from django.urls import path

from impresses.views import home_page

urlpatterns = [
    path('', home_page, name='homePage')
]
