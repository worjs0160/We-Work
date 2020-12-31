from django.urls import path
from users import views as user_views
from . import views

app_name = "core"

# as_view() 이용하여 클래스를 뷰로 변환
urlpatterns = [
    path("", views.test_home, name="home"),
    path("sample", views.sample, name="sample"),
]
