from django.shortcuts import render
from .scrap import web_scraping
from .models import Career
from hitcount.views import HitCountDetailView


def scrapping_insta(request):
    web_scraping()
    return render(request, 'about/about.html')

    
class CareerDetailwiew(HitCountDetailView):
    model = Career
    template_name = 'about/career_detail.html'
    count_hit = True



