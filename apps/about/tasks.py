from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .models import Instagramlink
from .scrap import web_scraping


@shared_task(name='scrap_instagram')
def scrap_instagram():
    Instagramlink.objects.all().delete()
    web_scraping()
