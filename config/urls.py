"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from boards import views as boards_views

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("users/", include("users.urls", namespace="users")),
    path("attendance/", include("attendance.urls", namespace="attendance")),
    path("boards/", include("boards.urls", namespace="boards")),
    path("calendar/", include("calendars.urls", namespace="calendars")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
<<<<<<< HEAD
    url(
        r"^download/(?P<path>.*)$",
        boards_views.download,
        {"document_root": settings.MEDIA_ROOT},
    ),
=======
    path("papers/", include("papers.urls", namespace="papers")),
    path("admin/", admin.site.urls),
>>>>>>> c157f5a73a9d9fa7e3084f365441b3718c059b09
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
