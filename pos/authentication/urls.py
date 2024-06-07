from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView


app_name = "authentication"
urlpatterns = [
    path('authentication/login', login_view, name="login"),
    path('authentication/register', register_user, name="register"),
    path("authentication/logout", LogoutView.as_view(), name="logout")
]
