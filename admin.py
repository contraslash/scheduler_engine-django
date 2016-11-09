from django.contrib import admin

from . import models as scheduler_engine_models
# Register your models here.

admin.site.register(scheduler_engine_models.Event)
