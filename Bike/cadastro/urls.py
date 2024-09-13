from django.urls import path 
from . import views
urlpatterns = [ 
    path('', views.home, name='index'), 
    path('blog', views.blog, name='blog'),
    path('form/', views.form, name='form'),
    path('log', views.lform, name='logform'),
    path('montagem', views.monta, name='mBike'),
    path('api/', views.user_manager, name='api_crud')
]