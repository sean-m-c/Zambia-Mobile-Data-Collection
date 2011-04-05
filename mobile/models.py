from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=200)
    iso_alpha_2_code = models.CharField(max_length=2, default="ZA", unique=True)

    def __unicode__(self):
        return self.iso_alpha_2_code

    class Meta:
        ordering = ["name"]


class District(models.Model):
    name = models.CharField(unique=True, max_length=200)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Chief(models.Model):
    name = models.CharField(unique=True, max_length=200)
    district = models.ForeignKey(District)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Village(models.Model):
    name = models.CharField(unique=True, max_length=200)
    chief = models.ForeignKey(Chief)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Submission(models.Model):
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name='submitted_by')
    mac = models.CharField(max_length=200, null=True)
    ip = models.IPAddressField()

    def __unicode__(self):
        return self.mac

    class Meta:
        ordering = ["date_added"]


class HealthPost(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class AgeRange(models.Model):
    start = models.IntegerField(max_length=3)
    end = models.IntegerField(max_length=3)

    def __unicode(self):
        return self.start + '-' + self.end


class Person(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, null=True)
    gender = models.IntegerField(max_length=1)

    def __unicode__(self):
        return self.first_name + ' ' + self.surname;


class BirthForm(models.Model):
    birth_date = models.DateField()
    father = models.CharField(null=True, max_length=200)
    mother = models.CharField(max_length=200)
    district = models.ForeignKey(District)
    chief = models.ForeignKey(Chief)
    village = models.ForeignKey(Village)
    person = models.ForeignKey(Person, related_name='person_birth', unique=True)
    submission = models.ForeignKey(Submission, unique=True)

    def __unicode__self(self):
        return self.birth_date

    class Meta:
        ordering = ["birth_date"]


class DeathForm(models.Model):
    death_date = models.DateField()
    marital_status = models.CharField(max_length=1)
    death_description = models.TextField()
    age_range = models.ForeignKey(AgeRange)
    health_post = models.ForeignKey(HealthPost)
    village = models.ForeignKey(Village)
    person = models.ForeignKey(Person, related_name='person_death', unique=True)
    submission = models.ForeignKey(Person, unique=True)

    def __unicode(self):
        return self.death_date

    class Meta:
        ordering = ["death_date"]