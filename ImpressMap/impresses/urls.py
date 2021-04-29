from django.urls import path

from impress_map import settings
from impresses.views import home_page, CreateImpress, conf_view, cons_view

urlpatterns = [
    path('', home_page, name='homePage'),
    path('add/', CreateImpress.as_view(), name='add'),
    path('conf/', conf_view, name='conf'),
    path('cons/', cons_view, name='cons'),
]
