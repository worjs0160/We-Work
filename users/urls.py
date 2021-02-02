from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("info/<int:pk>/", views.UserInfoView.as_view(), name="info"),
    path("update_profile/", views.UpdateProfile.as_view(), name="update_profile"),
    path("update_password/", views.update_password, name="update_password"),
    path("find_password/", views.find_password, name="find_password"),
]
