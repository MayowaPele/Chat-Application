from django.urls import path
from .views import getMessages, home, room, checkroom, sendMessage, getMessages

app_name = 'core'

urlpatterns = [
    path("", home, name='home'),
    path('<str:room>/', room, name='room'),
    path('checkroom', checkroom, name='checkroom'),
    path('send', sendMessage, name='sendMessage'),
    path('getmessages/<str:room>/', getMessages, name='getMessages')
]