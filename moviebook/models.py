from django.db import models


class Zanr(models.Model):
    
    nazev_zanru = models.CharField(max_length=80)
    
    def __str__(self):
        return "{0}".format(self.nazev_zanru)

    class Meta:
        verbose_name="Žánr"
        verbose_name_plural="Žánry"

class Rezie (models.Model):
    
    
    nazev_rezie = models.CharField(max_length=80)
    
    def __str__(self):
        return "{0} ".format(self.nazev_rezie)
    
    class Meta:
        verbose_name="Režisér"
        verbose_name_plural="Režiséři"

class Herec (models.Model):
    
    
    nazev_herce = models.CharField(max_length=80)
    
    def __str__(self):
        return "{0}".format(self.nazev_herce)
    
    class Meta:
        verbose_name="Herec"
        verbose_name_plural="Herci"
        
        
class Film(models.Model):
    nazev = models.CharField(max_length=200)
    popis= models.TextField(null=True, blank=True)
    zanr=models.ForeignKey(Zanr, on_delete=models.CASCADE, null=True)
    rezie=models.ForeignKey(Rezie, on_delete=models.CASCADE, null=True)
    herec=models.ForeignKey(Herec, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return "Název: {0}|Žánr: {1}|Režie: {2}".format(self.nazev,self.zanr,self.rezie)
    
    class Meta:
        verbose_name="Film"
        verbose_name_plural="Filmy"






