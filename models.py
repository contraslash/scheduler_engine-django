from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as auth_models

from base import models as base_models

from . import conf as scheduler_engine_conf
# Create your models here.

class Event(base_models.FullSlugBaseModel):
    """
    Event models
    """
    owner = models.ForeignKey(auth_models.User)
    start = models.DateTimeField()
    end = models.DateTimeField()
    guest_limit = models.PositiveIntegerField(default=scheduler_engine_conf.DEFAULT_MAX_INVITATIONS_PER_EVENT)
    pending_invitations = models.PositiveIntegerField(default=0)
    accepted_invitations = models.PositiveIntegerField(default=0)
    unaccepted_invitations = models.PositiveIntegerField(default=0)


class InvitationStatus(base_models.FullBaseModel):
    """
    Invitation Status Model, First Fixture should populate this model with Invited, Accepted, Declined, Unactive, Pending
    """
    pass

class Invitation(base_models.FullBaseModel):
    """
    Invitation Model, invitation of a event from a user to other
    """
    event_fk = models.ForeignKey(Event)
    user = models.ForeignKey(auth_models.User, related_name=scheduler_engine_conf.GUEST_USER_RELATED_NAME, null=True)
    invited_email = models.EmailField()
    invited_by = models.ForeignKey(auth_models.User, related_name=scheduler_engine_conf.GUEST_INVITED_BY_RELATED_NAME)
    invited_date = models.DateTimeField(auto_now_add=True)
    accepted_date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    status_fk = models.ForeignKey(InvitationStatus)


class Reminder(base_models.RemovableBaseModel):
    """
    Remider for a Event,
    """
    event_fk = models.ForeignKey(Event)
    user = models.ForeignKey(auth_models.User)
    remind_date = models.DateTimeField()