from rest_framework import serializers

from apps.about.models import Representation, Career, Management, Instagramlink

class RepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representation
        fields = ('id', 'name', 'avatar', 'icon_flag', 'country', 'phone_number', 'email')
    

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id', 'title', 'avatar', 'country', 'salary', 'type_work', 'description', 'requrements', 'views')



class MAngementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ('id', 'name', 'avatar', 'position', 'phone_number', 'email', 'description')
    


class InstagramlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instagramlink
        fields = ('id', 'image', 'link')





    

    

    