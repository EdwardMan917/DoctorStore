from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
import uuid


dummy_doctor = {
    "id": "d0cd68b1-1329-45a4-93c3-410ee4815f00",
    "name": "name",
    "address": "address",
    "phone_number": "12345678",
    "categories": [],
    "languages": [],
    "opening_hours": []
}

class GetDoctorViewTests(APITestCase):

    @patch('doctors.views.get_doctor_by_id')
    def test_success(self, mocked_query):
        endpoint = reverse('get_doctor', args=[str(uuid.uuid4())])
        mocked_query.return_value = dict(doctor=dummy_doctor)
        response = self.client.get(endpoint)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('doctor' in response.json())
    
    @patch('doctors.views.get_doctor_by_id')
    def test_doctor_not_found(self, mocked_query):
        endpoint = reverse('get_doctor', args=[str(uuid.uuid4())])
        mocked_query.return_value = dict(error_code='DOCTOR_NOT_FOUND')
        response = self.client.get(endpoint)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json().get('error_code'), 'DOCTOR_NOT_FOUND')

    @patch('doctors.views.get_doctor_by_id')
    def test_internal_error(self, mocked_query):
        endpoint = reverse('get_doctor', args=[str(uuid.uuid4())])
        mocked_query.return_value = dict(error_code='INTERNAL_SERVER_ERROR')
        response = self.client.get(endpoint)
        
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.json().get('error_code'), 'INTERNAL_SERVER_ERROR')


class GetDoctorsViewTests(APITestCase):

    @patch('doctors.views.get_doctors')
    def test_success(self, mocked_query):
        endpoint = reverse('get_doctors')
        mocked_query.return_value = dict(doctors=[dummy_doctor])
        response = self.client.get(endpoint)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('doctors' in response.json())
    
    @patch('doctors.views.get_doctors')
    def test_invalid_price(self, mocked_query):
        endpoint = reverse('get_doctors')
        mocked_query.return_value = dict(error_code='INVALID_PRICE_RANGE')
        response = self.client.get(endpoint)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get('error_code'), 'INVALID_PRICE_RANGE')

    @patch('doctors.views.get_doctors')
    def test_internal_error(self, mocked_query):
        endpoint = reverse('get_doctors')
        mocked_query.return_value = dict(error_code='INTERNAL_SERVER_ERROR')
        response = self.client.get(endpoint)
        
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.json().get('error_code'), 'INTERNAL_SERVER_ERROR')
