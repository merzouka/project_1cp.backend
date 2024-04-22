from django.db import models

from django.db import models
from authentication.models import user

Nationalities = [('Algérienne','Algérienne'),('Autre','Autre')]

class Haaj(models.Model):
    user = models.OneToOneField(user,  on_delete=models.CASCADE)
    first_name_arabic = models.CharField(max_length=100)
    last_name_arabic = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    NIN = models.CharField(max_length=150, unique=True)
    card_expiration_date = models.DateField()
    passport_id = models.CharField(max_length=100)
    passport_expiration_date = models.DateField()
    nationality = models.CharField(max_length=100, choices=Nationalities)
    phone_number = models.CharField(max_length=20)
    personal_picture = models.ImageField(upload_to='haaj_pictures/')

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(Haaj, self).save(*args, **kwargs)
        self.user.nombreInscription += 1
        self.user.save() 
        
class Haaja(models.Model):
    user = models.OneToOneField(user,  on_delete=models.CASCADE)
    first_name_arabic = models.CharField(max_length=100)
    last_name_arabic = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    NIN = models.CharField(max_length=150, unique=True)
    card_expiration_date = models.DateField()
    passport_id = models.CharField(max_length=100)
    passport_expiration_date = models.DateField()
    nationality = models.CharField(max_length=100, choices=Nationalities)
    phone_number = models.CharField(max_length=20)
    personal_picture = models.ImageField(upload_to='haaj_pictures/')
    maahram_id = models.PositiveIntegerField()
    
    def __str__(self):
        return self.user.email
    
    def save(self, *args, **kwargs):
        super(Haaja, self).save(*args, **kwargs)
        self.user.nombreInscription += 1
        self.user.save()  

class Tirage(models.Model):
    type_tirage=models.IntegerField(default=1)
    nombre_de_place=models.IntegerField(default=0)


        
class Baladiya(models.Model):
    name = models.CharField(max_length=100)
    id_utilisateur = models.ManyToManyField(user)
    wilaya=models.IntegerField(null=True,default=None)
    tirage= models.ForeignKey(Tirage,on_delete=models.CASCADE,default=None, null=True,) 
    def __str__(self):
        return self.name
      
class Winners(models.Model):
    nin = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nin

class WaitingList(models.Model):
    nin = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nin