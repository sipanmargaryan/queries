
from django.contrib import admin

import hotels.models


admin.site.register(hotels.models.Hotel)
admin.site.register(hotels.models.Room)
admin.site.register(hotels.models.Reservation)