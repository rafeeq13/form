from django.db import models
class AddJob(models.Model):
    jobtitle = models.CharField(max_length=100)
    job_description = models.TextField()
    requirements = models.TextField(max_length=400, default="")
    add = models.DateField()
    deadline = models.DateTimeField()


class Apply(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    contact=models.IntegerField(default=None)
    address=models.CharField(max_length=70,default=None)
    education=models.CharField(max_length=30)
    obtained_marks=models.IntegerField(default=None)
    total_marks=models.IntegerField(default=None)
    apply=models.CharField(max_length=70,primary_key=True,default=None)
    resume=models.FileField(upload_to='enroll/',max_length=250, null=True, blank=True,default=None)






class Info(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    size=models.IntegerField()
    location=models.CharField(max_length=100)







    