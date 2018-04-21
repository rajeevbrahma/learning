# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

import datetime
from django.core.validators import RegexValidator

# class PhoneModel(models.Model):
    



class EmployeeDetails(models.Model):
	EmployeeID = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=100)
	Designation = models.CharField(max_length=50)
	DateofBirth = models.DateField()
	OriginalDoB = models.DateField()
	JoiningDate = models.DateField()
	TotalExperience_inYears = models.FloatField()
	TotalExperience_inAditya_inYears = models.FloatField()
	Email = models.EmailField()
	About = models.TextField(blank=True,null=True)
	
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	ContactNumber = models.CharField(validators=[phone_regex], max_length=13, blank=True)
	# ContactNumber = models.CharField(max_length=10)
	Image = models.ImageField()
	slug = models.SlugField(max_length=200,unique=True)
	created = models.DateTimeField(auto_now_add=True) # record the time when object is created
	updated = models.DateTimeField(auto_now=True)
	
	def save(self,*args,**kwargs):
		self.slug = slugify(str(self.EmployeeID)+"-"+self.Name)
		super(EmployeeDetails,self).save(*args, **kwargs)

	def __str__(self):
		return (str(self.EmployeeID)+"-"+self.Name) 

class EmployeeDailyReport(models.Model):
	EmpID = models.ForeignKey(EmployeeDetails)
	Acad_Year = models.IntegerField(default=int(datetime.date.today().year))
	Acad_Month = models.IntegerField(default=int(datetime.date.today().month))
	Entry_Time = models.DateTimeField(null=True,blank=True,)
	Exit_Time = models.DateTimeField(null=True,blank=True)
	Total_Time_Spent = models.IntegerField(null=True,blank=True)
	LeaveApplied = models.BooleanField(default=None,blank=True)

	Leave_Choices = (
		    ('cl','Casual Leave'),
		    ('ccl', 'Compensatory Casual Leave'),
		    ('od','On Duty'),
		    ('defult',''),
		    
		)
	LeaveType = models.CharField(max_length=6, choices=Leave_Choices, default='default')


	slug = models.SlugField(max_length=200,unique=True)
	created = models.DateTimeField(auto_now_add=True) # record the time when object is created
	updated = models.DateTimeField(auto_now=True)

# Learn-Python (if the title is like this then slugify will convert into the following -- learn-python) 
	def save(self,*args,**kwargs):
		self.slug = slugify(str(self.EmpID)+"->"+str(self.created))
		super(EmployeeDailyReport,self).save(*args, **kwargs)

	def __str__(self):
		return (str(self.EmpID)+str(self.created))

class EmployeeMonthlyReport(models.Model):
	EmpID = models.ForeignKey(EmployeeDetails)
	Acad_Year = models.IntegerField(default=int(datetime.date.today().year))
	Acad_Month = models.IntegerField(default=int(datetime.date.today().month))
	WorkingDays = models.IntegerField()
	AttendedDays = models.IntegerField()
	CL_available = models.IntegerField()
	CL_Used = models.IntegerField()
	CCL_available = models.IntegerField()
	CCL_Used = models.IntegerField()
	OD_Used = models.IntegerField()
	slug = models.SlugField(max_length=200,unique=True)
	created = models.DateTimeField(auto_now_add=True) # record the time when object is created
	updated = models.DateTimeField(auto_now=True)


	def save(self,*args,**kwargs):
		self.slug = slugify(str(self.EmpID)+"->"+str(self.created))
		super(EmployeeMonthlyReport,self).save(*args, **kwargs)

	def __str__(self):
		return (str(self.EmpID)+str(self.created))

