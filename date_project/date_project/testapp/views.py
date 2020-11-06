import datetime
import calendar
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class DateSerialzer(serializers.Serializer):
    start_date = serializers.DateField(
        required=True, input_formats=["%d/%m/%Y"])
    end_date = serializers.DateField(required=True, input_formats=["%d/%m/%Y"])


class CalculateSatOrSun(APIView):
    serializer_class = DateSerialzer

    def post(self, request):
        # Get start or end date
        start = request.data.get('start_date')
        end = request.data.get('end_date')

        # Change format
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')

        week = {}
        for i in range((end_date - start_date).days):
            day = calendar.day_name[(
                start_date + datetime.timedelta(days=i+1)).weekday()]
            week[day] = week[day] + 1 if day in week else 1

        # Check saturday exist or not
        try:
            saturday = week['Saturday']
        except:
            saturday = 0

       # Check Sunday exist or not
        try:
            sunday = week['Sunday']
        except:
            sunday = 0
        Response_data = {
            "Saturday": saturday,
            "Sunday": sunday
        }
        return Response(Response_data)
