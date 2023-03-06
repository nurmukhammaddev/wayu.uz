from django.urls import path
from .views import scrapping_insta
from .scrap import web_scraping



urlpatterns = [
    path('', scrapping_insta, name='scraping'),
    path('sc/', web_scraping)
]