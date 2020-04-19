from rest_framework import serializers
from .models import Country, Day
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ("date", "new_deaths", "total_cases", "total_deaths", "updated_at")

class CountrySerializer(serializers.ModelSerializer):

    days = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ("name", "updated_at", "days")

    def get_days(self, instance):
        days = instance.days.all().order_by('-date')
        return DaySerializer(days, many=True).data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user