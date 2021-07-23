from django.db import models

class tb1(models.Model):
    ID = models.CharField(primary_key=True, max_length=40)
    Date = models.DateField(default=None)
    Time = models.TimeField(default=None)
    Temperature = models.FloatField(default=None)
    Humidity = models.IntegerField()
    Wind_Speed = models.FloatField(default=None)
    Max_Wind_Gust = models.FloatField(default=None)
    Precipitation = models.FloatField(default=None)
    class Meta:
        db_table = "Weather_Station" 

class tb2(models.Model):
    ID = models.CharField(primary_key=True, max_length=20)
    Date = models.DateField(default=None)
    Time = models.TimeField(default=None)
    Solar_Radiation = models.FloatField(default=None)
    class Meta:
        db_table = "Pyranometer" 