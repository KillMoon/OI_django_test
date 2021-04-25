from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import Impress, Profile

admin.site.register(Impress, MapAdmin)
admin.site.register(Profile)
