from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginhandle, name="loginhandles"),
    path("member/", views.member, name="member"),
    path("logout/", views.logquit, name="logquit"),
]

