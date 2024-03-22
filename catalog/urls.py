from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('cards/<int:pk>/', ProductDetailView.as_view(), name='cards'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
