from django.db import models

from authentication.models import utilisateur  

Nationalities = [('Algérienne','Algérienne'),('Autre','Autre')]

class Haaj(utilisateur):
    first_name_arabic = models.CharField(max_length=100)
    last_name_arabic = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    NIN = models.CharField(max_length=150 , unique=True)
    card_expiration_date = models.DateField()
    passport_id = models.CharField(max_length=100)
    passport_expiration_date = models.DateField()
    nationality = models.CharField(choices=Nationalities)
    country_of_residence = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    personal_picture = models.ImageField(upload_to='haaj_pictures/')
    

    def __str__(self):
        return self.user.email
    
    def save(self, *args, **kwargs):
        self.user.nombreInscription += 1
        self.user.save()
        super().save(*args, **kwargs)
    
class Haaja(Haaj):
    maahram_id = models.PositiveIntegerField()
    
    
    def save(self, *args, **kwargs):
        self.user.nombreInscription += 1
        self.user.save()
        super().save(*args, **kwargs)