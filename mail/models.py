from django.db import models

class Email_Subscription(models.Model):
	Email = models.CharField(max_length=200)
	Subscribed = models.BooleanField(default=True)

	def __str__(self):
		return f"Email: {self.Email}"

class userInfo(models.Model):
	Name = models.CharField(max_length=200)
	Username = models.CharField(max_length=200)
	Age = models.IntegerField(default=0)
	Description = models.TextField()

	def __str__(self):
		return self.Name