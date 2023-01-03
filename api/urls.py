from .views import get_drinks, drink_detail
from django.urls import path

app_name = 'api'


urlpatterns = [
    path('', get_drinks, name='drinks'),
    path('drink/<int:pk>/', drink_detail, name='drink' )
]