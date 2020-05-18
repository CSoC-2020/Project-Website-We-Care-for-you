from django.contrib import admin
from core.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'number_of_blogs', 'number_of_confessions', )
    list_filter = ("user",)
    search_fields = ['number_of_blogs', 'number_of_confessions',]

admin.site.register(Profile, ProfileAdmin)
