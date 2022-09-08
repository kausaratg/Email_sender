from django.urls import path
from email_sender import views

urlpatterns = [
    path('', views.send, name="send"),
    path("email_confirm", views.email_confirm, name="email_confirm")
]
