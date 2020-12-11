from rest_framework.response import Response
from rest_framework import views
from doctors.query import get_doctor_by_id, list_doctors
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from doctors.constants import GetDoctor, ListDoctors

class DoctorView(views.APIView):

    @swagger_auto_schema(
        manual_parameters=GetDoctor.PARAMETERS,
        responses=GetDoctor.RESPONSES,
        operation_id=GetDoctor.ID
    )
    def get(self, request, doctor_id: str):
       
        repsonse_body: dict = get_doctor_by_id(doctor_id)
        
        return Response(
            status=GetDoctor.STATUS.get(repsonse_body.get('error_code', 'SUCCESS')),
            data=repsonse_body
        )


class ListDoctorsView(views.APIView):

    @swagger_auto_schema(
        manual_parameters=ListDoctors.PARAMETERS,
        responses=ListDoctors.RESPONSES,
        operation_id=ListDoctors.ID
    )
    def get(self, request):
        
        queries = request.GET
        repsonse_body: dict = list_doctors(
            district=queries.get('district'),
            category=queries.get('category'),
            language=queries.get('language'),
            price_range=queries.get('price_range')
        )
        
        return Response(
            status=ListDoctors.STATUS.get(repsonse_body.get('error_code', 'SUCCESS')),
            data=repsonse_body
        )