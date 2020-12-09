
from django.urls import path
from doctors.views import DoctorView, DoctorsView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Doctor Store APIs",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="edwardman917@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=()
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns += [
    path('doctor/<uuid:doctor_id>', DoctorView.as_view(), name='get_doctor'),
    path('doctor', DoctorsView.as_view(), name='get_doctors')
]
