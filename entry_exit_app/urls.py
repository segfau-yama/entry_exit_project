from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_views.as_view(), name="home"),
    path('update/<int:pk>', views.test_views.as_view(), name="test"),
]
