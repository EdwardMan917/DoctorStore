from drf_yasg import openapi
from dataclasses import dataclass

@dataclass
class GetDoctor:

    ID = 'Get Doctor by ID'
    
    PARAMETERS = [
        openapi.Parameter(
            'doctor_id', 
            openapi.IN_PATH, 
            type=openapi.TYPE_STRING,
            description='''
                ID of doctor in UUID4 format. There are 7 valid IDs:

                93191810-7a02-4df0-a352-d2e8a146c112
                37fcb0c2-6e31-4819-80a1-89a98d0b9b76
                8332abf4-9b22-4e99-aaf9-df5dcfc3cc4b
                f5a98247-aea2-49df-9bcd-e3de98b8fe51
                0316d9d5-295f-4892-9797-a316553e74d5
                d0cd68b1-1329-45a4-93c3-410ee4815f00
                066210c7-f2e9-43f0-8ff9-4e660bcfee67
            '''
        )
    ]  

    # Errors
    DOCTOR_NOT_FOUND = 'DOCTOR_NOT_FOUND'
    INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR'

    RESPONSES = {
        200: 'Doctor retrieved successfully.',
        404: f'{DOCTOR_NOT_FOUND}: Doctor with the ID provided is not found.',
        500: f'{INTERNAL_SERVER_ERROR}: Unexpected server error occured.'
    }

    STATUS = {
        'SUCCESS': 200,
        DOCTOR_NOT_FOUND: 404,
        INTERNAL_SERVER_ERROR: 500
    }


@dataclass
class GetDoctors:

    ID = 'Get Doctors'
    
    PARAMETERS = [
        openapi.Parameter(
            'district', 
            openapi.IN_QUERY, 
            type=openapi.TYPE_STRING, 
            required=False,
            description='''
                District of the doctor's location. Valid values:

                kwun-tong
                fanling
                mongkok
                tsuen-wan
                central
                sheung-wan
            '''
        ),
        openapi.Parameter(
            'category', 
            openapi.IN_QUERY, 
            type=openapi.TYPE_STRING, 
            required=False,
            description='''
                Category of the doctor's profession. Valid values:

                dentistry
                pediatrics
                chinese-medicine
                bone-setting
                acupuncture
                psychiatric
                ophthalmology
                dermatology
            '''
        ),
        openapi.Parameter(
            'language', 
            openapi.IN_QUERY, 
            type=openapi.TYPE_STRING, 
            required=False,
            description='''
                Language the doctor is able to communicate in. Valid values:

                english
                cantonese
            '''
        ),
        openapi.Parameter(
            'price_range', 
            openapi.IN_QUERY, 
            type=openapi.TYPE_STRING, 
            required=False,
            description='''
                Price range of the doctors services in format of CSV with 2 values.
                Both values are inclusive and must be positive integers. Eg. 200,300 or 400,100
            '''
        )
    ]  

    # Errors
    INVALID_PRICE_RANGE = 'INVALID_PRICE_RANGE'
    INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR'

    RESPONSES = {
        200: 'Doctor retrieved successfully.',
        400: f'{INVALID_PRICE_RANGE}: Price range parameter is incorrect.',
        500: f'{INTERNAL_SERVER_ERROR}: Unexpected server error occured.'
    }

    STATUS = {
        'SUCCESS': 200,
        INVALID_PRICE_RANGE: 400,
        INTERNAL_SERVER_ERROR: 500
    }
