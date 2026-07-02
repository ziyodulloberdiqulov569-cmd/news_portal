from django.urls import path
from .views import home, news_detail, category_news

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('category/<int:category_id>/', category_news, name='category_news'),
]