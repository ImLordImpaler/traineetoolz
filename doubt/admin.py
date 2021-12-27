from django.contrib import admin

from doubt.models import Doubt , Response , Tag

admin.site.register(Doubt)
admin.site.register(Response)
admin.site.register(Tag)