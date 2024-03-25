from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.template_name = "home.html"
        else:
            self.template_name = "splash.html"

        return super().get(request, *args, **kwargs)
