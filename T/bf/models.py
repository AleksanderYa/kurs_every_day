from django.db import models

# Create your models here.
class InPlay(models.Model):
    time_inplay = models.IntegerField()
    scorre_home = models.IntegerField()
    scorre_away = models.IntegerField()
    amaunt_match = models.IntegerField()
    runner_home = models.CharField(max_length=50)
    runner_away = models.CharField(max_length=50)
    football_liga = models.CharField(max_length=100, )
    url_match = models.CharField(max_length=500)
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    def __str__(self):
        return self.amaunt_match
    

