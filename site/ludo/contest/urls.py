from django.urls import path

from . import views

urlpatterns = [
    path('', views.contests_list, name='contest'),
    path('<int:id>', views.show_contest, name='contest info')
]
