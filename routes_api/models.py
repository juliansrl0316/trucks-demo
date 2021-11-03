from django.db import models

class TruckRoute(models.Model):
    """ Modelo base de datos para usuarios en el sistema"""
    jobId = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    moveDate = models.CharField(max_length = 200)
    time = models.CharField(max_length = 200)
    availableDelivery = models.CharField(max_length = 200)
    movingFrom = models.CharField(max_length = 200)
    movingTo = models.CharField(max_length = 200)
    Lbs = models.CharField(max_length = 200)
    miles = models.CharField(max_length = 200)
    estimate = models.CharField(max_length = 200)

    
    
