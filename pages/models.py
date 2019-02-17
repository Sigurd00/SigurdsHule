from django.db import models
from django.utils import timezone
import os
# Create your models here.


class Projekter(models.Model):
    title = models.CharField(max_length=200)
    beskrivelse = models.TextField()
    img_code = models.ImageField(upload_to='projectImages/code', blank=True)
    img_looks = models.ImageField(upload_to='projectImages/looks', blank=True)
    klassetrin = models.IntegerField()
    oprettet = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projekter"
        verbose_name = "Projekt"
