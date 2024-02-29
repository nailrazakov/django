from django.urls import path, include

from catalog.views import *

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),

]
