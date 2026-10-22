from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    city=models.CharField(max_length=100)
    course=models.ForeignKey('Course',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendances')
    date=models.DateField()
    status=models.CharField(max_length=10,choices=[('Present','Present'),('Absent','Absent')]   )

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"