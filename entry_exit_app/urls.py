from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_views.as_view(), name="home"),
    path('test', views.test_views.as_view(), name="test"),
    path('update/<int:pk>', views.update_views.as_view(), name="update"),
]
