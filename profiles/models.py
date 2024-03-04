from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    sex = models.CharField(
        max_length=1,
        choices=[('M', 'Male'), ('F', 'Female')]
    )
    image = models.ImageField(upload_to='images')
    birth_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
