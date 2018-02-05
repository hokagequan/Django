from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('password/', auth_views.PasswordChangeView.as_view(template_name="change_password.html"), name="change_password"),
    path('password/done/', auth_views.PasswordChangeDoneView.as_view(template_name="change_password_done.html"), name="change_password_done"),
]