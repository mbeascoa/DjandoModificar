from django.urls import path

from mod import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='empleados'),

]

