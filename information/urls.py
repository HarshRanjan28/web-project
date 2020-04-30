from django.urls import path

from . import views

urlpatterns = [

    path('bodybuilding',views.bodybuilding,name = 'bodybuilding'),
    path('cardio',views.cardio,name = 'cardio')
]