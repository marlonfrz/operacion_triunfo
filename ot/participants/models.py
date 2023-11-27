from django.db import models
from django.urls import reverse


class MusicStyle(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name}"


class Competitor(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    birthdate = models.DateField()
    subject = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    hobbies = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=False)
    musicstyle = models.ManyToManyField(MusicStyle)

    class Meta:
        ordering = ["-first_name"]
        indexes = [
            models.Index(fields=["-first_name"]),
        ]

    def __str__(self):
        return f"{self.first_name}"

    def get_absolute_url(self):
        return reverse("competitor_detail", args=[self.slug])


class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    subject = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=False)

    class Meta:
        ordering = ["-first_name"]
        indexes = [
            models.Index(fields=["-first_name"]),
        ]

    def __str__(self):
        return f"{self.first_name}"

    def get_absolute_url(self):
        return reverse("teacher_detail", args=[self.slug])


class Judge(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    job = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=False)

    class Meta:
        ordering = ["-first_name"]
        indexes = [
            models.Index(fields=["-first_name"]),
        ]

    def __str__(self):
        return f"{self.first_name}"

    def get_absolute_url(self):
        return reverse("judge_detail", args=[self.slug])
