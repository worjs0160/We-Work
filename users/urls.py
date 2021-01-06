from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("info/<int:pk>", views.UserInfoView.as_view(), name="info"),
    path("update_info", views.update_info, name="update_info"),
    path("update_password", views.update_password, name="update_password"),
]