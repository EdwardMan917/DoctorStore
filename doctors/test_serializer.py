from django.test import TestCase
from doctors.test_query import create_test_data
from doctors.models import Doctor, Language
from doctors.serializers import DoctorSerializer
import uuid

class SerializerTests(TestCase):
    
    @classmethod
    def setUpTestData(self):
        create_test_data()
        self.doctor = Doctor.objects.get(pk='b8eec005-25e7-475a-b3f9-8b5f7d8471a4')
        self.categories = self.doctor.categories.all()
        self.result = DoctorSerializer(self.doctor).data
    
    def test_keys(self):
        self.assertEqual(
            set(self.result.keys()), 
            {
                'id', 
                'name', 
                'address', 
                'phone_number', 
                'categories', 
                'languages', 
                'opening_hours'
            }
        )

    def test_doctor_details(self):
        self.assertEqual(self.doctor.name, self.result.get('name'))
        self.assertEqual(self.doctor.address, self.result.get('address'))
        self.assertEqual(str(self.doctor.id), self.result.get('id'))
        self.assertEqual(self.doctor.phone_number, self.result.get('phone_number'))
        
    def test_related_details(self):
        self.assertEqual(self.doctor.categories.count(), len(self.result.get('categories')))
        self.assertEqual(self.doctor.languages.count(), len(self.result.get('languages')))
        self.assertEqual(self.doctor.opening_hours.count(), len(self.result.get('opening_hours')))
        self.assertTrue('services' in category for category in self.result.get('categories'))
        
