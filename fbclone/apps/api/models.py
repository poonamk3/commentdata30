from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




class StudentClass(models.Model):
	classname=models.CharField(max_length=10,blank=True)
	def __str__(self):
		return self.classname

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=200)
	roll=models.IntegerField()
	stuclass=models.ForeignKey(StudentClass,related_name='stuclass',on_delete= models.CASCADE,blank=True,null=True)
	city=models.CharField(max_length=200)
	def __str__(self):
		return self.name



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


