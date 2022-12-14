from django.urls import path, include
from . import views

urlpatterns = [
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/<imie>/', views.osoba_imie),
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
    path('osoby/osoby_add', views.osoba_add),
    path('druzyny/druzyny_add', views.druzyna_add),
    path('osoby/update/<int:pk>/', views.osoba_update_delete),
    path('osoby/delete/<int:pk>/', views.osoba_update_delete),
    path('api-auth/', include('rest_framework.urls')),
]