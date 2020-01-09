from django.db import models

# Create your models here.
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    ContactNo = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
