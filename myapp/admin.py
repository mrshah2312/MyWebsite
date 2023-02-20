from django.contrib import admin
from .models import *

all_models = [Master]

for model in all_models:
    admin.site.register(model)