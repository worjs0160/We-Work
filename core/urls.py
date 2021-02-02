from django.urls import path
from users import views as user_views
from . import views

app_name = "core"

# as_view() 이용하여 클래스를 뷰로 변환
urlpatterns = [
    path("home", views.home, name="home"),
    path("", user_views.LoginView.as_view(), name="login"),
]
