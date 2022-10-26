from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('send_mail/', SendMail.as_view(), name='send_mail'),
    path('', HomeNews.as_view(), name='home'),
    # path('', cache_page(60 * 5)(HomeNews.as_view()), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<slug:slug>/', ViewNews.as_view(), name='view_news'),
    # path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
