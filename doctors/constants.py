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
            description='ID of doctor in UUID4 format'

        )
    ]  

    # Errors
    DOCTOR_NOT_FOUND = 'DOCTOR_NOT_FOUND'
    INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR'

    RESPONSES = {
        200: 'Doctor retrieved successfully.',
        404: f'{DOCTOR_NOT_FOUND}: Doctor with the ID provided is not found.',
        500: f'{INTERNAL_SERVER_ERROR}: Unexpected server error.'
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
            description="District of the doctor's location. Eg. kwun-tong"
        ),
        openapi.Parameter(
            'category', 
            openapi.IN_QUERY, 
            type=openapi.TYPE_STRING, 
            required=False,
            description="Category of the doctor's profession. Eg. dentistry"
        ),
        openapi.Parameter(
            'language', 
            openapi.IN_QUERY, 
            type=openapi.TYPE_STRING, 
            required=False,
            description="Language the doctor is able to communicate in. Eg. english"
        ),
        openapi.Parameter(
            'price_range', 
            openapi.IN_QUERY, 
            type=openapi.TYPE_STRING, 
            required=False,
            description="Price range of the doctors services. Eg. 200,300"
        )
    ]  

    # Errors
    INVALID_PRICE_RANGE = 'INVALID_PRICE_RANGE'
    INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR'

    RESPONSES = {
        200: 'Doctor retrieved successfully.',
        400: f'{INVALID_PRICE_RANGE}: Price range parameter is incorrect.',
        500: f'{INTERNAL_SERVER_ERROR}: Unexpected server error.'
    }

    STATUS = {
        'SUCCESS': 200,
        INVALID_PRICE_RANGE: 400,
        INTERNAL_SERVER_ERROR: 500
    }
