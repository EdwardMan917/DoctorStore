from oslash.either import Either, Left, Right

from doctors.models import Doctor
from django.db.models import Q
from typing import Union

from doctors.constants import GetDoctor, GetDoctors
from doctors.serializers import DoctorSerializer

from django.http import QueryDict


def get_doctor_by_id(doctor_id: str) -> dict:

    def get_doctor_object(ctx: dict) -> Either:
        doctor = Doctor.objects.filter(pk=ctx.get('doctor_id')).first()
        if not doctor:
            return Left(dict(ctx, error_code=GetDoctor.DOCTOR_NOT_FOUND))
        return Right(dict(doctor=DoctorSerializer(doctor).data))

    try:
        result: Either = Right(dict(doctor_id=doctor_id)) | get_doctor_object

        return result.value
    except Exception:
        return dict(error_code=GetDoctor.INTERNAL_SERVER_ERROR)


def get_doctors(
    district: Union[str, None]=None, 
    category: Union[str, None]=None, 
    language: Union[str, None]=None, 
    price_range: Union[str, None]=None
) -> dict:

    def validate_price_range(ctx: dict) -> Either:
        price_query = price_range

        if not price_query:
            return Right(ctx)

        try:
            price_query = price_query.split(',')
            price_query.sort()
            lower_limit, upper_limit = map(int, price_query)
            price_query = Q(services__price__range=(lower_limit, upper_limit))
            return Right(dict(condition=ctx.get('condition').add(price_query, Q.AND)))
        except ValueError:
            return Left(dict(error_code=GetDoctors.INVALID_PRICE_RANGE))

    
    def generate_filter(ctx: dict) -> Right:
        condition = ctx.get('condition')
        
        if district:
            condition.add(Q(district=district), Q.AND)
        if category:
            condition.add(Q(categories__query_name=category), Q.AND)
        if language:
            condition.add(Q(languages__query_name=language), Q.AND)
        
        return Right(dict(condition=condition))


    def filter_doctors(ctx: dict) -> Right:
        doctors = Doctor.objects.filter(ctx.get('condition')).distinct()
        if not doctors:
            return Right(dict(doctors=list()))
        return Right(dict(doctors=DoctorSerializer(doctors, many=True).data))


    try:
        result: Either = Right(dict(condition=Q())) | validate_price_range |\
                         generate_filter | filter_doctors
        return result.value

    except Exception:
        return dict(error_code=GetDoctors.INTERNAL_SERVER_ERROR)

