from django.urls import path
from .views import CountryList, CountryDetail, DayList, UserCreate, LoginView
from django.conf.urls import url


urlpatterns = [   
    path("login/", LoginView.as_view(), name="login"), 
    path('countries/', CountryList.as_view(), name="country_list"),
    path('days/', DayList.as_view(), name="day_list"),
    path('country/<str:country>', CountryDetail.as_view(), name="country_detail"),
    path("users/", UserCreate.as_view(), name="user_create"),
]