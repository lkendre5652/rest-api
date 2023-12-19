from django.db import models

class ServiceParent(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.name

class ServiceChild(models.Model):
    parent_cat = models.ForeignKey(ServiceParent, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class ParentLocations(models.Model):
    service_name = models.ForeignKey(ServiceChild, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=25)

    def __str__(self):
        return self.location_name
class Location(models.Model):
    service_name = models.ForeignKey(ServiceChild, on_delete=models.CASCADE)
    parent_location = models.ForeignKey(ParentLocations, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name



    
