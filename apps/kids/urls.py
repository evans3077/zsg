from django.urls import path
from . import views

app_name = "kids"

urlpatterns = [
    path("", views.overview, name="overview"),
]

