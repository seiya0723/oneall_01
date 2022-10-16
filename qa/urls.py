from django.urls import path
from . import views

app_name = "qa"
urlpatterns = [
    path("", views.index, name="index"),
    path("good/<int:pk>/", views.good, name="good"),
]
