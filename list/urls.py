from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clist', views.clist, name='clist'),
    path('lists/job', views.job, name='job'),
    path('lists/<str:pk>', views.list, name='list'),
    path('lists/delete/<str:sk>/<str:pk>', views.delete, name='delete'),
    path('deletelist/<str:pk>', views.dellist, name='deletelist'),
    path('lists/edit/<str:sk>/<str:pk>', views.edit, name='edit'),
]