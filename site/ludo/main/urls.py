from django.urls import path

from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
#path("<str:download>", views.download_file, name="download_file"),
path("", views.home, name="home"),
path("submit/", views.submit, name="submit")
]
