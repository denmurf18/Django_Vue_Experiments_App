from django.urls import path
from .views import vue_page, api_data

urlpatterns = [
    path('vue-page/', vue_page, name='vue_page'),
    path('api/data', api_data, name='api_data'),
]