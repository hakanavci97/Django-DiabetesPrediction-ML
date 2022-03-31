from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="dashboard-index"),
    path('predictions/',views.predictions,name="dashboard-predictions"),
    path('result/',views.result,name="result"),
    path('diabetes/',views.diabetes,name="diabetes"),
    path('dataset/',views.dataset,name="dataset"),
    path('about/',views.about,name="about")
 
]
