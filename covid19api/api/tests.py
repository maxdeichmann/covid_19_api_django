from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Country, Day
from .serializers import CountrySerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class BaseViewTest(APITestCase):
    client = APIClient()



    def setUp(self):
        # ...
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

        self.create_country("Germany")
        self.create_country("UK")
        self.create_country("USA")

        germany = Country.objects.filter(name="Germany").first()

        self.create_day("2020-01-01", 100, 100, 100, 100, germany)
        self.create_day("2020-01-02", 100, 100, 100, 100, germany)
    
    @staticmethod
    def create_country(name=""):
        if name:
            Country.objects.create(name=name)
    
    @staticmethod
    def create_day(date="", new_cases=0, new_deaths=0, total_cases=0, total_deaths=0, country=None):
        if date and new_cases and new_deaths and total_cases and total_deaths and country:
            Day.objects.create(date=date, new_cases=new_cases, new_deaths=new_deaths, total_cases=total_cases, total_deaths=total_deaths, country=country)

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )



class GetAllCountriesTest(BaseViewTest):
    def test_get_all_countries_unauth(self):
        """
        This test ensures that it is not possible to access the data
        without being authorized.
        """

        self.client.logout()

        # hit the API endpoint
        response = self.client.get(
            reverse("country_list", kwargs={"version": "v1"})
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_all_countries_auth(self):
        """
        This test ensures that all countries added in the setUp method
        exist when we make a GET request to the countries/ endpoint
        """

        # log the client in
        self.client.login(username="test", password="test")

        # hit the API endpoint
        response = self.client.get(
            reverse("country_list", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Country.objects.all()
        serialized = CountrySerializer(expected, many=True)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class StoreAllCountriesTest(BaseViewTest):
    json_string = """{
        "Togo": [
            {"date": "2020-03-07", "location": "Togo", "new_cases": 0.0, "new_deaths": 0.0, "total_cases": 1, "total_deaths": 0.0}, 
            {"date": "2020-03-08", "location": "Togo", "new_cases": 0.0, "new_deaths": 0.0, "total_cases": 1, "total_deaths": 0.0}, 
            {"date": "2020-03-09", "location": "Togo", "new_cases": 0.0, "new_deaths": 0.0, "total_cases": 1, "total_deaths": 0.0}, 
            {"date": "2020-03-10", "location": "Togo", "new_cases": 0.0, "new_deaths": 0.0, "total_cases": 1, "total_deaths": 0.0}
        ],
        "Germany": [
            {"date": "2020-03-07", "location": "Togo", "new_cases": 0.0, "new_deaths": 0.0, "total_cases": 1, "total_deaths": 0.0}
        ]
    }
    """

    def test_store_all_countries_unauth(self):
        self.client.logout()

        response = self.client.post("/api/v1/countries/", self.json_string, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



    def test_store_all_countries_auth(self):
        self.client.login(username="test", password="test")

        response = self.client.post("/api/v1/countries/", self.json_string, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

