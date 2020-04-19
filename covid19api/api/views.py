from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import Country, Day
from .serializers import CountrySerializer, DaySerializer, UserSerializer

import json
from datetime import datetime

class CountryList(APIView):

    def get(self, request, version):
        countries = Country.objects.all()
        data = CountrySerializer(countries, many=True).data
        return Response(data)


    def post(self, request, version):

        if request.body:

            json_data = json.loads(request.data)
            for key in json_data:

                country, created = Country.objects.update_or_create(name=key)

                for day_entry in json_data[key]:

                    date = datetime.strptime(day_entry["date"], "%Y-%m-%d")

                    defaults = {"new_cases": day_entry["new_cases"], 
                                "new_deaths": day_entry["new_deaths"], 
                                "total_cases": day_entry["total_cases"],
                                "total_deaths": day_entry["total_deaths"]}

                    obj, created = Day.objects.update_or_create(date=date, country=country, defaults=defaults)

        return Response({"created"}, status=status.HTTP_201_CREATED)


class CountryDetail(APIView):

    def get(self, request, version, country):
        countries = Country.objects.filter(name=country)
        data = CountrySerializer(countries, many=True).data
        return Response(data)


class DayList(APIView):

    def get(self, request, version):
        days = Day.objects.all()
        data = DaySerializer(days, many=True).data
        return Response(data)


class UserCreate(generics.CreateAPIView):
    # exempt from auth
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request, version):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)