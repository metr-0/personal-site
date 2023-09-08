from django.urls import path

from .views import *

urlpatterns = [
    path('', Page.as_view(), name='homepage'),
    path('<slug:slug>', Page.as_view(), name='page')
]
