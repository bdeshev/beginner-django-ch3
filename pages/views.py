from django.http import HttpResponse
from django.views.generic import TemplateView


def home_page_view(request):
    return HttpResponse("Homepage")

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"