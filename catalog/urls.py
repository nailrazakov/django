from django.urls import path, include

from catalog.views import *

urlpatterns = [
    path('', main),
    path('feedback/', feedback),

]
