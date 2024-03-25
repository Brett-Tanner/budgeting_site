from django.urls import path
from .views import HomePageView, SplashPageView

urlpatterns = [
    path("", SplashPageView.as_view(), name="splash"),
    path("home", HomePageView.as_view(), name="home"),
]
