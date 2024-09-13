from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)

    def__str__(self):
      return self.name

class Employee(models.Model):
   name= models.Char.Field(max_length=225)
   dept = models.ForeginKey(Department, on_delete=models.CASCADE)
   job_title = models.CharField(max_length=225)
   salary = models.DecimalField(max_digits=10, decimal_places=2)
   bonus = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)

   def__str__(self):
    return f'{self.name}-(self.job_title)'


