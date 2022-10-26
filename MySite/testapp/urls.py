from django.urls import path

from news.views import HomeNews
from .views import *

urlpatterns = [
    # path('', HomeNews.as_view(), name='test'),
    path('', Test.as_view(), name='test'),
    path('rubric/<int:pk>/', GetRubric.as_view(), name='rubric'),
]