from django.test import TestCase
from doctors.data import create
from doctors.query import get_doctor_by_id, get_doctors
from doctors.models import Doctor, Language
from doctors.serializers import DoctorSerializer
import uuid

class SerializerTests(TestCase):
    
    @classmethod
    def setUpTestData(self):
        create()
        self.doctor = Doctor.objects.first()
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
                'services',
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
        self.assertEqual(self.doctor.services.count(), len(self.result.get('services')))
        


class GetDoctorTests(TestCase):
    
    @classmethod
    def setUpTestData(self):
        create()

    def test_success(self):
        doctor = Doctor.objects.first()
        result: dict = get_doctor_by_id(doctor.id)
        assert not 'error_code' in result
        assert result.get('doctor', dict()).get('id') == str(doctor.id)

    def test_doctor_not_found(self):
        result: dict = get_doctor_by_id(str(uuid.uuid4()))
        assert result.get('error_code') == 'DOCTOR_NOT_FOUND'

        result: dict = get_doctor_by_id(123)
        assert result.get('error_code') == 'DOCTOR_NOT_FOUND'


class GetDoctorsTests(TestCase):
    
    @classmethod
    def setUpTestData(self):
        create()

    def test_district_query(self):
        district = 'kwun-tong'
        result: dict = get_doctors(district=district)
        doctors = result.get('doctors')
        self.assertFalse('error_code' in result)
        self.assertFalse(doctors == [])
        for doctor in doctors:
            self.assertEqual(
                Doctor.objects.get(pk=doctor.get('id')).district,
                district
            )

        result: dict = get_doctors(district='dummy')
        self.assertTrue(result.get('doctors') == [])
        
    def test_category_query(self):
        category = 'dentistry'
        result: dict = get_doctors(category=category)
        doctors = result.get('doctors')
        self.assertFalse('error_code' in result)
        self.assertFalse(doctors == [])
        for doctor in doctors:
            self.assertTrue('牙科' in doctor.get('categories'))

        result: dict = get_doctors(category='dummy')
        self.assertTrue(result.get('doctors') == [])

    def test_language_query(self):
        language = 'english'
        result: dict = get_doctors(language=language)
        doctors = result.get('doctors')
        self.assertFalse('error_code' in result)
        self.assertFalse(doctors == [])
        for doctor in doctors:
            self.assertTrue('英語' in doctor.get('languages'))

        result: dict = get_doctors(language='dummy')
        self.assertTrue(result.get('doctors') == [])
