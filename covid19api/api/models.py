from django.db import models
from datetime import datetime, date

# Create your models here.

class Country(models.Model):
    # name of the country
    name = models.CharField(max_length=255, null=False)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_country')
        ]
        
    def __str__(self):
        return f"Country: {self.name}"

class Day(models.Model):
    date = models.DateField(default=date.today ,blank=True)
    
    new_cases = models.IntegerField(default=0)
    
    new_deaths = models.IntegerField(default=0)
    
    total_cases = models.IntegerField(default=0)

    total_deaths = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    country = models.ForeignKey(Country, related_name='days', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'country')
    
    def __str__(self):
        return f"Date: {self.date}, new cases: {self.new_cases}, new deaths: {self.new_deaths}, total cases: {self.total_cases}, total deaths: {self.total_deaths}"