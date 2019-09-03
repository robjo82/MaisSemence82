from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.hours_declaration,
         name="hours_declaration"
         ),
]