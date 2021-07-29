from django.contrib import admin
from bf.models import InPlay
# Register your models here.


# admin.site.register(InPlay)
# admin.site.register(PostModel)
@admin.register(InPlay)
class AdminInPlay(admin.ModelAdmin):
    list_display = ['id', 'runner_home', 'runner_away', 'football_liga', 'time_inplay']
    list_display_links = ['id', 'runner_home', 'runner_away', 'football_liga']
    ordering = ('-id',)