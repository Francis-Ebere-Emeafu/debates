from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    sex = models.CharField(
        max_length=1,
        choices=[('M', 'Male'), ('F', 'Female')]
    )
    image = models.ImageField(upload_to='images')
    birth_date = models.DateField()

    def __str__(self):
        return self.name
