from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import url, include



urlpatterns = [
    path('', views.index , name='index'),
    
    path('/author/', views.index_auth , name='index_auth'),
    url('book/add/', views.add_book, name='add_book'),
    url('auth/add/', views.add_author, name='add_auth'),
    path('book/<int:pk>/', views.book_detail , name='book_detail'),
    path('auth/<int:pk>/', views.auth_detail , name='auth_detail'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
    path('auth/delete/<int:pk>', views.auth_delete, name='auth_delete'),
    path('edit/<int:pk>', views.book_update, name='book_edit'),
    path('auth/edit/<int:pk>', views.auth_update, name='auth_edit'),
    
    
]



