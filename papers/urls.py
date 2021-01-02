from django.urls import path
from . import views

app_name = "papers"

urlpatterns = [
    path('', views.summary, name='summary'),
    path('show/', views.show_paper, name='show_paper'),
    path('new/', views.new_paper, name='new_paper'),
    path('inbox/', views.inbox, name='inbox', kwargs={'box': 'inbox'}),
    path('inbox_nc/', views.inbox, name='inbox_nc',
         kwargs={'box': 'inbox_nc'}),
    path('outbox/', views.inbox, name='outbox', kwargs={'box': 'outbox'}),
    path('archive/', views.inbox, name='archive', kwargs={'box': 'archive'}),
    path('search_inbox/', views.inbox,
         name='search_inbox', kwargs={'box': 'inbox'}),
    path('search_inbox_nc/', views.inbox,
         name='search_inbox_nc', kwargs={'box': 'inbox_nc'}),
    path('search_outbox/', views.inbox,
         name='search_outbox', kwargs={'box': 'outbox'}),
    path('search_archive/', views.inbox,
         name='search_archive', kwargs={'box': 'archive'}),
]
