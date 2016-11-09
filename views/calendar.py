#! -*- encoding: UTF-8 -*-
__author__ = 'ma0@contraslash.com'
from django.views import generic

from base import views as base_views

from .. import models as scheduler_engine_models

class BaseCalendar(base_views.BaseListView):
    """
    Simple base view for a calendar event display
    """
    template_name = "scheduler_engine/calendar/simple_calendar.html"
    queryset = scheduler_engine_models.Event.objects.all()
    context_object_name = "events"

class AllEvents(BaseCalendar):
    pass
