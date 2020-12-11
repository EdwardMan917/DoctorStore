from doctors.models import Doctor, Category, Service
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'item',
            'price',
            'remarks'
        )

class CategorySerializer(serializers.ModelSerializer):
    
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'display_name',
            'services'
        )


class DoctorSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True, read_only=True)
    languages = serializers.SlugRelatedField(
        many=True,
        read_only=True, 
        slug_field='display_name'
    )
    opening_hours = serializers.SlugRelatedField(
        many=True,
        read_only=True, 
        slug_field='details'
    )
    
    class Meta:
        model = Doctor
        fields = (
            'id', 
            'name',
            'address',
            'phone_number', 
            'categories', 
            'languages',
            'opening_hours'
        )
