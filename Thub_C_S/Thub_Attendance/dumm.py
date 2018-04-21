# SerialID = models.AutoField(primary_key=True)
	# Doc_DateTime = models.IntegerField(default=lambda:datetime.date.today())
	



class EmployeeDailyReport(models.Model):
	EmployeeID = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=100)
	Designation = models.CharField(max_length=50)
	Acad_Year = models.IntegerField(default=int(datetime.date.today().year))
	Acad_Month = models.IntegerField(default=int(datetime.date.today().month))
	Entry_Time = models.DateTimeField(blank=True)
	Exit_Time = models.DateTimeField(blank=True)
	slug = models.SlugField(max_length=200,unique=True)
	created = models.DateTimeField(auto_now_add=True) # record the time when object is created
	updated = models.DateTimeField(auto_now=True)

# Learn-Python (if the title is like this then slugify will convert into the following -- learn-python) 
	def save(self,*args,**kwargs):
		self.slug = slugify(self.EmployeeID+str(created))
		super(EmployeeDailyReport,self).save(*args, **kwargs)

	def __str__(self):
		return (self.EmployeeID+str(created))	



class EmployeeDailyReport(models.Model):
	EmployeeID = models.ForeignKey(EmployeeDetails)

	Acad_Year = models.IntegerField(default=int(datetime.date.today().year))
	Acad_Month = models.IntegerField(default=int(datetime.date.today().month))
	Entry_Time = models.DateTimeField(null=True,blank=True,)
	Exit_Time = models.DateTimeField(null=True,blank=True)
	slug = models.SlugField(max_length=200,unique=True)
	created = models.DateTimeField(auto_now_add=True) # record the time when object is created
	updated = models.DateTimeField(auto_now=True)

# Learn-Python (if the title is like this then slugify will convert into the following -- learn-python) 
	def save(self,*args,**kwargs):
		self.slug = slugify(str(self.EmployeeID)+"->"+str(self.created))
		super(EmployeeDailyReport,self).save(*args, **kwargs)

	def __str__(self):
		return (str(self.EmployeeID)+str(self.created))			