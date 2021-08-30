from django.urls import path
from vaccination import views

urlpatterns = [
    path('getalluser', views.ShowAll),
    path('createuser',views.CreateUser),
    path('getuser/<pk>',views.viewUserDeatils),
    path('register',views.vaccineRegistration),
    path('update',views.upadteStatus),
    path('cancel',views.cancelAppointment)
]