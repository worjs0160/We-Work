from django.urls import path
from . import views

app_name = "papers"

urlpatterns = [
    path('', views.summary, name='summary'),
    path('show/<int:id>/', views.show_paper, name='show_paper'),
    path('new/', views.new_paper, name='new_paper'),
    path('inbox/<int:page>/', views.inbox,
         name='inbox', kwargs={'box': 'inbox'}),
    path('inbox_nc/<int:page>/', views.inbox, name='inbox_nc',
         kwargs={'box': 'inbox_nc'}),
    path('outbox/<int:page>/', views.inbox,
         name='outbox', kwargs={'box': 'outbox'}),
    path('archive/<int:page>/', views.inbox, name='archive'),
    path('search_inbox/<str:search_type>/<str:search_word>/<int:page>/', views.inbox,
         name='search_inbox'),
    path('search_inbox_nc/<str:search_type>/<str:search_word>/<int:page>/', views.inbox,
         name='search_inbox_nc'),
    path('search_outbox/<str:search_type>/<str:search_word>/<int:page>/', views.inbox,
         name='search_outbox'),
    path('search_archive/<str:search_type>/<str:search_word>/<int:page>/', views.inbox,
         name='search_archive'),
    path('gg/', views.gg, name='gg'),
]
