from django.conf.urls import url

from views import calendar
urlpatterns = [
    url(
        # ### Views of calendar ###
        r'^all$',
        calendar.AllEvents.as_view()
    )
]
