from django.db import models

class Detail(models.Model):
	name = models.CharField(max_length=100,null = True)
	age = models.CharField(max_length=100,null = True)
	rollnumber = models.CharField(max_length = 20,null = True)
	section = models.CharField(max_length=20,null = True)
	branch = models.CharField(max_length=30, null = True)
	year = models.CharField(max_length=20,null = True)
	email = models.CharField(max_length=30,null = True)
	adhaar_number = models.CharField(max_length = 12,null = True)

	def __str__(self):
		return self.name
