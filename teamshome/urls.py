from django.urls import path
from .views import HomePageView, TextVideoPageView

urlpatterns = [
    path('textvideo/', TextVideoPageView.as_view(), name='textvideo_about'),
    path('', HomePageView.as_view(), name='home'),
]
