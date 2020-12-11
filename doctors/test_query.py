from django.test import TestCase
from doctors.query import get_doctor_by_id, list_doctors
from doctors.models import *
import uuid

def create_test_data():

    doctors = [
        {
            'id': 'b8eec005-25e7-475a-b3f9-8b5f7d8471a4',
            'name': 'test_doctor_a', 
            'address': 'doctor_address_a', 
            'district': 'district_a', 
            'phone_number': 'phone_number',
            'categories': [
                {   
                    'query_name': 'category_a',
                    'display_name': 'Category A',
                    'services': [
                        {
                            'item': 'Service A',
                            'price': 100,
                            'remarks': None
                        }
                    ]
                },
                {   
                    'query_name': 'category_b',
                    'display_name': 'Category B',
                    'services': [
                        {
                            'item': 'Service B',
                            'price': 500,
                            'remarks': None
                        }
                    ]
                }
            ],
            'languages': [
                {
                    'query_name': 'language_a',
                    'display_name': 'Language A'
                },
                {
                    'query_name': 'language_b',
                    'display_name': 'Language B'
                }
            ],
            'opening_hours': [
                '星期一至五:0900-1800'
            ]
        },
        {
            'id': '50d00df4-3fa4-4c7d-97bc-243da5c0bc08',
            'name': 'test_doctor_b', 
            'address': 'doctor_address_b', 
            'district': 'district_b', 
            'phone_number': 'phone_number',
            'categories': [
                {   
                    'query_name': 'category_b',
                    'display_name': 'Category B',
                    'services': [
                        {
                            'item': 'Service B',
                            'price': 250,
                            'remarks': None
                        }
                    ]
                }
            ],
            'languages': [
                {
                    'query_name': 'language_a',
                    'display_name': 'Language A'
                },
                {
                    'query_name': 'language_b',
                    'display_name': 'Language B'
                }
            ],
            'opening_hours': [
                '星期一至五:0900-1800'
            ]
        },
        
    ]

    for doctor in doctors:
        doctor_obj = Doctor.objects.create(
            id = doctor.get('id'),
            name=doctor.get('name'),
            address=doctor.get('address'),
            district=doctor.get('district'), 
            phone_number=doctor.get('phone_number')
        )

        for category in doctor.get('categories'):
            category_obj = Category.objects.create(
                query_name=category.get('query_name'),
                display_name=category.get('display_name'),
                doctor=doctor_obj
            )

            for service in category.get('services'):
                Service.objects.create(
                    item=service.get('item'),
                    price=service.get('price'),
                    remarks=service.get('remarks'),
                    category=category_obj
                )

        for language in doctor.get('languages'):
            Language.objects.create(
                query_name=language.get('query_name'),
                display_name=language.get('display_name'),
                doctor=doctor_obj
            )

        for opening_hour in doctor.get('opening_hours'):
            OpeningHour.objects.create(
                details=opening_hour,
                doctor=doctor_obj
            )


class GetDoctorTests(TestCase):
    
    @classmethod
    def setUpTestData(self):
        create_test_data()

    def test_success(self):
        doctor = Doctor.objects.get(pk='b8eec005-25e7-475a-b3f9-8b5f7d8471a4')
        result: dict = get_doctor_by_id(doctor.id)
        self.assertFalse('error_code' in result)
        self.assertEqual(result.get('doctor', dict()).get('id'), str(doctor.id))

    def test_doctor_not_found(self):
        result: dict = get_doctor_by_id(str(uuid.uuid4()))
        self.assertEqual(result.get('error_code'), 'DOCTOR_NOT_FOUND')

        result: dict = get_doctor_by_id(123)
        self.assertEqual(result.get('error_code'), 'DOCTOR_NOT_FOUND')


class ListDoctorsTests(TestCase):
    
    @classmethod
    def setUpTestData(self):
        create_test_data()

    def test_district_query(self):
        district = 'district_a'
        result: dict = list_doctors(district=district)
        doctors = result.get('doctors')
        self.assertFalse('error_code' in result)
        self.assertFalse(doctors == [])
        for doctor in doctors:
            self.assertEqual(
                Doctor.objects.get(pk=doctor.get('id')).district,
                district
            )

        result: dict = list_doctors(district='dummy')
        self.assertTrue(result.get('doctors') == [])
        
    def test_category_query(self):
        category = 'category_b'
        result: dict = list_doctors(category=category)
        doctors = result.get('doctors')
        self.assertFalse('error_code' in result)
        self.assertFalse(doctors == [])
        categories_result = list()
        for doctor in doctors:
            categories_result += [category.get('display_name') for category in doctor.get('categories')]
        self.assertTrue('Category B' in categories_result)

        result: dict = list_doctors(category='dummy')
        self.assertTrue(result.get('doctors') == [])

    def test_language_query(self):
        language = 'language_a'
        result: dict = list_doctors(language=language)
        doctors = result.get('doctors')
        self.assertFalse('error_code' in result)
        self.assertFalse(doctors == [])
        for doctor in doctors:
            self.assertTrue('Language A' in doctor.get('languages'))

        result: dict = list_doctors(language='dummy')
        self.assertTrue(result.get('doctors') == [])

    def test_price_query(self):
        price_range = '200,300'
        result: dict = list_doctors(price_range=price_range)
        doctors = result.get('doctors')
        self.assertFalse('error_code' in result)
        self.assertFalse(doctors == [])
        doctor_ids = list()
        for doctor in doctors:
            doctor_ids.append(doctor.get('id'))
        self.assertTrue('50d00df4-3fa4-4c7d-97bc-243da5c0bc08' in doctor_ids)

        result: dict = list_doctors(price_range='dummy')
        self.assertTrue(result.get('error_code') == 'INVALID_PRICE_RANGE')
