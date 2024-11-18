from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom de l'évènement")
    start_time = models.DateTimeField(verbose_name="Début de l'évènement")
    end_time = models.DateTimeField(verbose_name="Fin de l'évènement")
    
    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return self.name