from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class TextVideoPageView(TemplateView): # new
    template_name = 'textvideo_about.html'