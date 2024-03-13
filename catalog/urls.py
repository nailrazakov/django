from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import *

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('cards/<int:product_id>/', cards, name='cards'),
    path('card/', card, name='card'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
