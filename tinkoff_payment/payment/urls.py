from django.urls import re_path
from .views import NotificationHandler

urlpatterns = [
    re_path("^for-notification$", NotificationHandler.DefaultHandler.as_view())
]
