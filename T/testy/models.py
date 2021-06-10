from django.db import models  

#class Employee(models.Model):  
#    eid = models.CharField(max_length=20)  
#    ename= models.CharField(max_length=100)  
#    econtact = models.CharField(max_length=15)  
#    class Meta:  
#        db_table = "be_db"  
# Create your models here.

class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
#    first_name = models.CharField(max_length=50) # for creating varchar column  
#    release_date = models.DateField()                        # for creating date column  
#    num_stars = models.IntegerField()  
    
class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name = models.CharField(max_length=30)  
    contact = models.IntegerField()  
    email = models.EmailField(max_length=50)  
    age = models.IntegerField()  