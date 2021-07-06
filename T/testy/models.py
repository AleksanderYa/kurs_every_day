import datetime
from django.db import models
from django.utils import timezone

# https://django.fun/docs/django/ru/3.2/intro/tutorial02/


#
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

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text