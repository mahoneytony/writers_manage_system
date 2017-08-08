from django import forms
from app1.models import UserProfile
from django.contrib.auth.models import User

class Exel_field_form(forms.Form):
	exel_field = forms.CharField(max_length=1000)

class Order_form(forms.Form):
	number = forms.CharField(max_length=300, required=False)
	account = forms.CharField(max_length=300, required=False)
	files = forms.CharField(max_length=300, required=False)
	subject = forms.CharField(max_length=300, required=False)
	topic = forms.CharField(max_length=300, required=False)
	client_deadline = forms.CharField(max_length=300, required=False)
	price = forms.CharField(max_length=300, required=False)
	number_of_pages = forms.CharField(max_length=300, required=False)
	spaced = forms.CharField(max_length=300, required=False)
	format = forms.CharField(max_length=300, required=False)
	number_of_sources = forms.CharField(max_length=300, required=False)
	abstract = forms.CharField(max_length=300, required=False)
	slieds = forms.CharField(max_length=300, required=False)
	questions = forms.CharField(max_length=300, required=False)
	problems = forms.CharField(max_length=300, required=False)
	paper_type = forms.CharField(max_length=300, required=False)
	assign_date = forms.CharField(max_length=300, required=False)
	details = forms.CharField(max_length=1000, required=False)
	real_time_deadline = forms.CharField(max_length=300, required=False)
	status = forms.CharField(max_length=300, required=False)
	writer_deadline = forms.CharField(max_length=300, required=False) 
	writer_time = forms.CharField(max_length=300, required=False)
	writer_number = forms.CharField(max_length=300, required=False)
	words_min = forms.CharField(max_length=300, required=False)
	writer_name = forms.CharField(max_length=300, required=False)
	writer_email = forms.CharField(max_length=300, required=False)
	send_date = forms.CharField(max_length=300, required=False)
	payment = forms.CharField(max_length=300, required=False)
	payment_date = forms.CharField(max_length=300, required=False)
	client_num_of_order = forms.CharField(max_length=300, required=False)
	
class UserForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

class UserProfileForm(forms.Form):
	social = forms.URLField(max_length=100)
	mobile_number = forms.CharField(max_length=100)


class UploadOrderFileForm(forms.Form):
	order_file = forms.FileField()

class CommentForm(forms.Form):
	comment = forms.CharField(max_length=2000)

'''
class CommentFromControllerForm(forms.Form):
	controller_comment = forms.CharField(max_length=200)
'''

class FileForm(forms.Form):
	order_file = forms.FileField()

	