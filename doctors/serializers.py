from doctors.models import Doctor
from rest_framework import serializers



class DoctorSerializer(serializers.ModelSerializer):

    categories = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    opening_hours = serializers.SerializerMethodField() 
    
    class Meta:
        model = Doctor
        fields = (
            'id', 
            'name',
            'address',
            'phone_number', 
            'categories', 
            'languages',
            'services',
            'opening_hours'
        )

    def get_categories(self, obj):
        return obj.categories.all().values_list('name', flat=True)

    def get_languages(self, obj):
        return obj.languages.all().values_list('name', flat=True)

    def get_services(self, obj):
        return obj.services.all().values('item', 'price', 'remarks')

    def get_opening_hours(self, obj):
        return obj.opening_hours.all().values_list('details', flat=True)