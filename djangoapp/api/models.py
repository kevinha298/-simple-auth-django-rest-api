from django.db import models

# Create your models here.
class Users(models.Model):
    employeeID = models.CharField(max_length=10, unique=True)
    employeeName = models.CharField(max_length=100)
    age = models.IntegerField()
    ranking = models.FloatField() 

    def upload_photo(self, filename):
        path = f'api/photo/{filename}'
        return path
    
    photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)


    def upload_file(self, filename):
        path = f'api/file/{filename}'
        return path
    
    resume = models.ImageField(upload_to=upload_file, null=True, blank=True)

    def __str__(self):
        return f'{self.employeeID} - {self.employeeName}'