from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', Regiser.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
