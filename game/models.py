from django.db import models
from django.utils import timezone
class Question(models.Model):
	Primary_img = models.ImageField(upload_to='images/')
	option1 = models.ImageField(upload_to='images/')
	option2 = models.ImageField(upload_to='images/')
	option3 = models.ImageField(upload_to='images/')

class Submission(models.Model):
	username = models.CharField(max_length=250)
	que1 = models.IntegerField(default=1)
	que2 = models.IntegerField(default=1)
	que3 = models.IntegerField(default=1)
	que4 = models.IntegerField(default=1)
	que5 = models.IntegerField(default=1)
	ans1 = models.IntegerField(default=1)
	ans2 = models.IntegerField(default=1)
	ans3 = models.IntegerField(default=1)
	ans4 = models.IntegerField(default=1)
	ans5 = models.IntegerField(default=1)
	state = models.IntegerField(default=0)
	conn = models.IntegerField(default=0)
	conn_at = models.DateTimeField(default=timezone.now,auto_now=False,auto_now_add=False)
	created_at = models.DateTimeField(default=timezone.now)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.username+" state="+str(self.state) 
