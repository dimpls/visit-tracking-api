from django.utils import timezone
from rest_framework.views import APIView

from .serializers import StoreSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Store, Employee
from .serializers import VisitSerializer


class StoreListByPhoneNumber(APIView):
    serializer_class = StoreSerializer

    def get(self, request, phone_number):
        stores = Store.objects.filter(employee__phone_number=phone_number)
        if stores.exists():
            serializer = self.serializer_class(stores, many=True)
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "Store with the provided phone number was not found."},
                            status=status.HTTP_404_NOT_FOUND)


class CreateVisit(APIView):
    serializer_class = VisitSerializer

    def post(self, request, id):
        phone_number = request.data.get('phone_number')

        if phone_number is None:
            return Response({'error': 'phone_number is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            employee = Employee.objects.get(phone_number=phone_number)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            store = Store.objects.get(pk=id, employee=employee)

        except Store.DoesNotExist:
            return Response({'error': 'Employee is not associated with the specified Store'},
                            status=status.HTTP_403_FORBIDDEN)

        current_datetime = timezone.now()

        serializer = VisitSerializer(data={'date_time': current_datetime,
                                           'store': store.pk,
                                           'latitude': request.data.get('latitude'),
                                           'longitude': request.data.get('longitude')})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
