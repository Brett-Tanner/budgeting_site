from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class SplashPageView(TemplateView):
    template_name = "splash.html"
