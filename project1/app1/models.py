from django.db import models
import datetime
from django.contrib.auth.models import User

 #Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	mobile_number = models.CharField(max_length=13)
	social = models.URLField(max_length=100)
	role = models.CharField(max_length=30, default='writer')

	def __str__(self):
		return self.user.username

class Order_model(models.Model):
	number = models.CharField(max_length=300)
	account = models.CharField(max_length=300, blank=True)
	files = models.CharField(max_length=300, blank=True)
	subject = models.CharField(max_length=300, blank=True)
	topic = models.CharField(max_length=300, blank=True)
	client_deadline = models.CharField(max_length=300, blank=True, null=True)
	price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	number_of_pages = models.IntegerField(blank=True, null=True)
	spaced = models.CharField(max_length=300, blank=True)
	format = models.CharField(max_length=300, blank=True)
	number_of_sources = models.IntegerField(blank=True, null=True)
	abstract = models.BooleanField(blank=True, default=False)
	slieds = models.CharField(max_length=300, blank=True)
	questions = models.CharField(max_length=300, blank=True)
	problems = models.CharField(max_length=300, blank=True)
	paper_type = models.CharField(max_length=300, blank=True)
	assign_date = models.CharField(max_length=300, blank=True, null=True)
	details = models.CharField(max_length=300, blank=True)
	real_time_deadline = models.TimeField(blank=True, null=True)
	status = models.CharField(max_length=300, blank=True, default='available')
	writer_deadline = models.CharField(max_length=300, blank=True, null=True) 
	writer_time = models.TimeField(blank=True, null=True)
	writer_number = models.CharField(max_length=300, blank=True)
	words_min = models.IntegerField(blank=True, null=True)
	writer = models.ForeignKey(User, null=True)
	writer_name = models.CharField(max_length=300, null=True)
	writer_email = models.EmailField(max_length=300, blank=True)
	send_date = models.CharField(max_length=300, blank=True, null=True)
	payment = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	payment_date = models.CharField(max_length=300, blank=True, null=True)
	client_num_of_order = models.CharField(max_length=300, blank=True)
	controller = models.ForeignKey(UserProfile, null=True)
	times_returned_for_revision = models.IntegerField(default=0)
	
	

	def __str__(self):
		return self.number

	def get_absolut_url(self):
		return 'http://127.0.0.1:8000/' + self.number

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'



	

class Tender(models.Model):
	order = models.OneToOneField(Order_model)
	writers = models.ManyToManyField(User)

	def writers_list(self):
		iden = self.id
		tender = Tender.objects.get(id=iden)
		writers = tender.writers.all()
		return writers


class Comment(models.Model):
	author = models.ForeignKey(User)
	order = models.ForeignKey(Order_model)
	text = models.CharField(max_length=200)
	create_date = models.DateTimeField(default=datetime.datetime(2000, 1, 1, 1, 1, 1, 1))


class FileModel(models.Model):
	author = models.ForeignKey(User)
	order = models.ForeignKey(Order_model)
	order_file = models.FileField(upload_to='order_files/%Y/%m/%d')
	create_date = models.DateTimeField(default=datetime.datetime(2000, 1, 1, 1, 1, 1, 1))
	is_final = models.BooleanField(blank=True, default=False)


