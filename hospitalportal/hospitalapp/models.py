from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	c =[('0','Guest'),
	     ('1','Applicant'),
	     ('2','Recruiter'),]
	role_type = models.CharField(max_length=5,choices=c,default='0')
	uid = models.CharField(max_length=15)
	has_arogyasri = models.BooleanField(default=False)
	has_hospital = models.BooleanField(default=False)
class arogyasri(models.Model):
	ufrom = models.CharField(max_length=100,null=True,blank=True)
	prob = models.CharField(max_length=100,null=True,blank=True)
	mble = models.CharField(max_length=10,null=True,blank=True)
	usd = models.OneToOneField(User,on_delete=models.CASCADE)
class docprofile(models.Model):
	dname = models.CharField(max_length=100,null=True,blank=True)
	experience = models.CharField(max_length=100,null=True,blank=True)
	specialist = models.CharField(max_length=100,null=True,blank=True)
	mobilenum = models.CharField(max_length=12,null=True,blank=True)
	usd = models.OneToOneField(User,on_delete=models.CASCADE)
class staff(models.Model):
	jtitle = models.CharField(max_length=100)
	jlocation = models.CharField(max_length=100)
	jreq = models.TextField()
	jexpr = models.IntegerField()
	jsal = models.PositiveIntegerField(default=200)
	is_avail = models.BooleanField(default=True)
	jcrtm = models.DateTimeField(auto_now_add=True)
	usj = models.ForeignKey(User,on_delete=models.CASCADE)
	jcmp = models.ForeignKey(docprofile,on_delete=models.CASCADE)


