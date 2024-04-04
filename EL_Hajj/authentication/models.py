from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

PROVINCES = [
    (1, 'Wilaya d''Adrar'),
    (2, 'Wilaya de Chlef'),
    (3, 'Wilaya de Laghouat'),
    (4,'Wilaya d''Oum El Bouaghi'),
    (5,'Wilaya de Betna'),
    (6,'Wilaya de Bejaya'),
    (7,'Wilaya de Biskra'),
    (8,'Wilaya de Bechar'),
    (9,'Wilaya de Blida'),
    (10,'Wilaya de Bouira'),
    (11,'Wilaya de Tamanrasset'),
    (12,'Wilaya de Tebessa'),
    (13,'Wilaya de Tlemcen'),
    (14, 'Wilaya de Tiaret'),
    (15,'Wilaya de Tizi Ouzou'),
    (16,'Wilaya d''Alger'),
    (17, 'Wilaya de Djelfa'),
    (18 , 'Wilaya de Jijel'),
    (19,'Wilaya de Setif'),
    (20,'Wilaya de Saida'),
    (21,'Wilaya de Skikda'),
    (22,' Wilaya de SIDI Bel Abbes'),
    (23,'Wilaya de Annaba'),
    (24,'Wilaya de Guelma'),
    (25,'Wilaya de Constantine'),
    (26,'Wilaya de Medea'),
    (27,'Wilaya de Mostaganem'),
    (28,'Wilaya de Msila'),
    (29, 'Wilaya de Mascara'),
    (30, 'Wilaya de Ouargla'),
    (31, 'Wilaya de Oran'),
    (32, 'Wilaya de El Bayadh'),
    (33, 'Wilaya de Illizi'),
    (34, 'Wilaya de Bordj Bou Arreridj'),
    (35, 'Wilaya de Boumerdès'),
    (36, 'Wilaya de El Tarf'),
    (37, 'Wilaya de Tindouf'),
    (38, 'Wilaya de Tissemsilt'),
    (39, 'Wilaya de El Oued'),
    (40, 'Wilaya de Khenchela'),
    (41, 'Wilaya de Souk Ahras'),
    (42, 'Wilaya de Tipaza'),
    (43, 'Wilaya de Mila'),
    (44, 'Wilaya de Aïn Defla'),
    (45, 'Wilaya de Naâma'),
    (46, 'Wilaya de Aïn Témouchent'),
    (47, 'Wilaya de Ghardaïa'),
    (48, 'Wilaya de Relizane'),
    (49, 'Wilaya de El Mghair'),
    (50, 'Wilaya de El Menia'),
    (51, 'Wilaya de Ouled Djellal'),
    (52, 'Wilaya de Bordj Baji Mokhtar'),
    (53, 'Wilaya de Béni Abbès'),
    (54, 'Wilaya de Timimoun'),
    (55, 'Wilaya de Touggourt'),
    (56, 'Wilaya de Djanet'),
    (57, 'Wilaya de In Salah'),
    (58, 'Wilaya de In Guezzam')  
]

USERCHOICES = [
    (1,'utilisateur'),
    (2,'hedj'),
    (3,'gestionnaireWizara'),
    (4,'gestionnaireWilaya'),
    (5,'gestionnaireTirage')]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
class role(models.Model):
    role = models.CharField(max_length=50)



class CustomUser(AbstractBaseUser):
    id_role = models.ManyToManyField(role)
    username = None
    email = models.EmailField(max_length=254,unique=True)
    is_email_verified = models.BooleanField(null=True)
    code = models.CharField(max_length=4, null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['id_role']
    objects = CustomUserManager()

    def __str__(self):
        return self.email   
    

class utilisateur(AbstractBaseUser):
    emailUtilisateur = models.OneToOneField(CustomUser,on_delete=models.CASCADE,to_field='email')
    username = None
    password = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20,blank=False)
    dateOfBirth = models.DateField(blank=False)
    city= models.CharField(max_length=50,blank=False)
    province = models.IntegerField(choices=PROVINCES)
    STATUS_CHOICES = [
        ('M', 'male'),
        ('F', 'female'),
    ]
    gender = models.CharField(max_length=1, choices=STATUS_CHOICES, default='M',blank=False)
    nombreInscription = models.PositiveSmallIntegerField(default = 0)
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'dateOfBirth', 'province', 'city', 'gender']
    
    

class PasswordReset(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="password reset's user",
        null=True
    )