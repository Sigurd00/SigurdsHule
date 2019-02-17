from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Tekster(models.Model):
    title_lix = models.CharField(max_length=200)
    forfatter = models.CharField(max_length=100, default="Jacob Skadborg")
    beskrivelse_lix = models.TextField()
    tekst = models.TextField()
    lixtal = models.IntegerField()
    punktummer = models.IntegerField()
    antalSaetninger = models.IntegerField()
    avgLength = models.IntegerField()
    klassetrin_lix = models.IntegerField()
    mestBrugteOrd = models.CharField(max_length= 200)
    oprettet_lix = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title_lix

    class Meta:
        verbose_name_plural = "Tekster"
        verbose_name = "Tekst"

class TeksterForm(ModelForm):
    class Meta:
        model = Tekster
        fields = ['title_lix', 'forfatter', 'beskrivelse_lix', 'tekst', 'lixtal', 'punktummer', 'antalSaetninger', 'avgLength', 'klassetrin_lix', 'mestBrugteOrd', 'oprettet_lix']
