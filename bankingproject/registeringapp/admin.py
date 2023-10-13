from django.contrib import admin
from .models import Person,District,Branch,Material

admin.site.register([Person, District,Branch,Material])
