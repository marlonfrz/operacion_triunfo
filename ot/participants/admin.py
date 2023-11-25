from django.contrib import admin
from .models import MusicStyle, Competitor, Teacher, Judge


@admin.register(MusicStyle)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]


@admin.register(Competitor)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "slug",
        "birthdate",
        "subject",
        "city",
        "job",
        "hobbies",
        "avatar",
    ]


@admin.register(Teacher)
class PostAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "slug", "subject", "avatar"]


@admin.register(Judge)
class PostAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "slug", "job", "avatar"]
