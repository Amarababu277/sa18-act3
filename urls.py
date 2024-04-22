from django.urls import path
from myapp.views import index, show

urlpatterns = [
    path('products/', index, name='index'),
    path('products/<int:pk>/', show, name='show'),
]