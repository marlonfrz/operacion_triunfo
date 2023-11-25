from django.db import models


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
    slug = models.SlugField(max_length=250)
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