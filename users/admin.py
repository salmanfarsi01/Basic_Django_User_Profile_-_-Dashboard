# users/admin.py
from django.contrib import admin
from .models import Profile, Thought

admin.site.register(Profile)
admin.site.register(Thought)