from django.contrib import admin
from bf.models import InPlay
# Register your models here.


# admin.site.register(InPlay)
# admin.site.register(PostModel)
@admin.register(InPlay)
class AdminInPlay(admin.ModelAdmin):
    list_display = ['id', 'time_inplay', 'amaunt_match', 'runner_home', 'runner_away', 'football_liga' ]
    list_display_links = ['id', 'runner_home', 'runner_away', 'football_liga']
    ordering = ('-id',)
    search_fields = ['id', 'time_inplay', 'amaunt_match', 'runner_home', 'runner_away', 'football_liga' ]
    
   
