from rest_framework import serializers
from vaccination.models import registration,user,placeOne,placeTwo,placethree,placeFour

class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration 
        fields= '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user 
        fields= '__all__'

class placeOneSerializer(serializers.ModelSerializer):
    class Meta:
        model=placeOne 
        fields= '__all__'

class placeTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model=placeTwo 
        fields= '__all__'

class placethreeSerializer(serializers.ModelSerializer):
    class Meta:
        model=placethree 
        fields= '__all__'

class placeFourSerializer(serializers.ModelSerializer):
    class Meta:
        model=placeFour 
        fields= '__all__'
