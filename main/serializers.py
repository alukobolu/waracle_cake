from rest_framework import serializers
from .models import *


#Register a user
class CakeSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(required=True)
    comment = serializers.CharField(required=True)
    imageURL = serializers.CharField(required=True)
    yumFactor = serializers.IntegerField(required=True)


    class Meta:
        model = Cake
        fields = ['name','comment','imageURL', 'yumFactor']

    def validate(self, validated_data):
        yumFactor = validated_data['yumFactor']
        if yumFactor > 5 or yumFactor < 1:
            raise serializers.ValidationError('Invalid YumFactor')
        return validated_data

    def create(self, validated_data):
        return Cake.objects.create(**validated_data)
    
