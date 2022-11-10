from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('druzyny/', views.druzyna_list),
    path('druzyny/<int:pk>/', views.druzyna_detail),
    path('druzyny/druzyny_add', views.druzyna_add),
    path('osoby/', views.OsobaList.as_view()),
    path('osoby/<int:pk>/', views.OsobaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)