from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.utils.dateparse import parse_date
from django.db.models import Q
from datetime import datetime

class IcfBogieChecksheetCreateAPIView(APIView):

    def post(self, request):
        serializer = IcfBogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IcfWheelMeasurementSearchCreateAPIView(APIView):


    def get(self, request):
        form_number = request.query_params.get('form_number')
        created_by = request.query_params.get('created_by')
        created_at_str = request.query_params.get('created_at')
        search = request.query_params.get('search')

        filters = {}
        if form_number:
            filters['form_number'] = form_number
        if created_by:
            filters['created_by'] = created_by
        if created_at_str:
            try:
                parsed_date = datetime.strptime(created_at_str.strip(), "%Y-%m-%d").date()
                filters['created_at'] = parsed_date
            except ValueError:
                return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        queryset = IcfWheelMeasurement.objects.filter(**filters)

        if search:
            search_results_1 = IcfWheelMeasurement.objects.filter(form_number__icontains=search)
            search_results_2 = IcfWheelMeasurement.objects.filter(created_by__icontains=search)
            queryset = (search_results_1 | search_results_2).distinct()

            if filters:
                queryset = queryset.filter(**filters)

        serializer = IcfWheelMeasurementSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = IcfWheelMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
