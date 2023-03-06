from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.about.models import Representation, Career, Management, Instagramlink
from .serializers import RepresentationSerializer, CareerSerializer, MAngementSerializer, InstagramlinkSerializer



class RepresentationListAPIView(generics.ListAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RepresentationCreateAPIView(generics.CreateAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CareerListAPIView(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class CareerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class ManagementListAPIView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = MAngementSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    


class InstagramlinkListAPIView(generics.ListAPIView):
    queryset = Instagramlink.objects.all()
    serializer_class = InstagramlinkSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



