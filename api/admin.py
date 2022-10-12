from django.contrib import admin
from django.apps import apps
#from .models.company import Company
# Register your models here.
#admin.site.register(Company);

all_models = apps.get_app_config('api').get_models()

for model in all_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass