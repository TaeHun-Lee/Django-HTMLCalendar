from django.contrib import admin
from django.urls import path
import events.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', events.views.calendar_view, name="calendar"),
    path('event/new/', events.views.event, name="new"),
    path('event/edit/<int:event_id>', events.views.event, name="edit"),
]
