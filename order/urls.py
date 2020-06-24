from django.urls import path

from .views import MainPageOrderView


urlpatterns = [
    path('', MainPageOrderView.as_view(), name='main_order'),
]