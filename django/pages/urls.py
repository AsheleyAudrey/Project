from django.urls import path
from .views import HomePageView, SignPageView

urlpatterns = [
    path('sign/', SignPageView.as_view(), name='sign'),
    path('', HomePageView.as_view(), name='home'),
]
