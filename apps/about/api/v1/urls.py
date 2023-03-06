from django.urls import path

from .views import RepresentationCreateAPIView, InstagramlinkListAPIView

urlpatterns = [
    path('repserentation/', RepresentationCreateAPIView.as_view(), name='about'),
    path('instagram/', InstagramlinkListAPIView.as_view(), name='instagramlink')
]


