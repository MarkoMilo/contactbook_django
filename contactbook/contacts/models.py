from django.db import models


class AddressEntry(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    # gender = models.BooleanField(null=False)
    name = models.CharField(null=False, max_length=50)
    firstname = models.CharField(null=False, max_length=50)
    birthdate = models.DateField(null=False)
    active = models.BooleanField(null=False)


class Person(AddressEntry):
    pass


class Contact(AddressEntry):
    pass

