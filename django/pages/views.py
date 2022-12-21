from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'index.html'

class SignPageView(TemplateView): # new
    template_name = 'sign.html'
