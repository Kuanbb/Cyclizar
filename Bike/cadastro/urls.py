from django.urls import path 
from .views import home, blog, user_manager, form
urlpatterns = [ 
    path('', home, name='index'), 
    path('blog', blog, name='blog'),
    path('form/', form, name='form'),
    path('api/', user_manager, name='api_crud')
]