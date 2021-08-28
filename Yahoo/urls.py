from django.contrib import admin
from django.urls import path, include
from financial_news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('financial_news.urls')),
    path('',views.index,name = 'index'),
]
