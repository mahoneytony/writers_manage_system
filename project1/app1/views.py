from django.shortcuts import render
from django.shortcuts import render, render_to_response
from app1.models import *
from django.http import HttpResponse, HttpResponseRedirect
from app1.forms import Exel_field_form, Order_form, UserForm, UserProfileForm, UploadOrderFileForm, CommentForm, FileForm
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q


# Create your views here.

keys=[
'order','account','files','subject','topic','deadline','price','pages',
'spaced','format','sources','abstract','slieds','questions','problems','paper_type','assign_date','details','deadline_time_real','status',
'21','writers_DL','writer_time','writer_num','words_min','writer_name','email','send_date','payment','payment_date','file','name','client']



@login_required
def personal(request):
	user = request.user
	if user.is_authenticated():
		return writer_cabinet(request)
	else:
		return register(request)

@login_required
def writer_cabinet(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='in progress')
	if request.method == 'GET':
		return render(request, 'personal.html', {'orders':orders, 'user':user})

'''
def extract_from_exel(request):
	if request.method == 'GET':
		return render(request, 'correction_page.html')
	elif request.method == 'POST':
		text = request.POST['exel_string']
		list_of_params = text.split('	')
		dict_out={}
		for x, y in zip(keys, list_of_params):
   			dict_out[x] = y

		return render(request, 'correction_page.html', dict_out)

#def create_order(request):
#	if request.method == 'GET':
#		return render(request, 'correction_page.html', dict_out)


def extract_from_exel(request):
	if request.method == 'GET':
		return render(request, 'correction_page.html')
	elif request.method == 'POST':
		exel_form = Exel_field_form(request.POST)
		order_form = Order_form(request.POST)
		if order_form.is_bound:
			text = request.POST['exel_string']
			list_of_params = text.split('	')
			dict_out={}
			for x, y in zip(keys, list_of_params):
   				dict_out[x] = y

			return render(request, 'correction_page.html', dict_out)
		else:
			return HttpResponse('sdsdsd')
'''
@login_required
def extract_from_exel(request):
	if request.method == 'GET':
		return render(request, 'create_order.html')
	elif request.method == 'POST':
		return HttpResponseRedirect('/correction_page/')

@login_required
def correction(request):
	if request.method == 'POST':
		text = request.POST['exel_string']
		list_of_params = text.split('	')
		dict_out={}
		for x, y in zip(keys, list_of_params):
   			dict_out[x] = y
		writers = User.objects.filter(userprofile__role='writer')
		dict_out['writers'] = writers
		return render(request, 'correction_page.html', dict_out)



@login_required
def model_creating(request):
	if request.method == 'POST':
		form = Order_form(request.POST)
		if form.is_valid():
			if request.POST['writer_id'] == 'status available':
				status_for_model = 'available'
				writer_for_model = None
			else:
				status_for_model = 'unconfirmed'
				writer_for_model = User.objects.get(id=request.POST['writer_id'])

			model = Order_model(number = request.POST['number'],
								account = request.POST['account'],
								files = request.POST['files'],
								subject = request.POST['subject'],
								topic = request.POST['topic'],
								client_deadline = request.POST['client_deadline'],
								price = request.POST['price'],
								number_of_pages = request.POST['number_of_pages'],
								spaced = request.POST['spaced'],
								format = request.POST['format'],
								number_of_sources = request.POST['number_of_sources'],
								abstract = abstract_transform(request.POST['abstract']),
								slieds = request.POST['slieds'],
								questions = request.POST['questions'],
								problems = request.POST['problems'],
								paper_type = request.POST['paper_type'],
								assign_date = request.POST['assign_date'],
								details = request.POST['details'],
								real_time_deadline = dl_transform(request.POST['real_time_deadline']),
								#status = request.POST['status'],
								status = status_for_model,
								writer_deadline = request.POST['writer_deadline'],
								writer_time = request.POST['writer_time'],
								writer_number = request.POST['writer_number'],
								words_min = request.POST['words_min'],
								#writer_name = request.POST['writer_name'],
								writer_email = request.POST['writer_email'],
								send_date = request.POST['send_date'],
								payment = request.POST['payment'],
								payment_date = request.POST['payment_date'],
								client_num_of_order = request.POST['client_num_of_order'],
								#writer = User.objects.get(id=request.POST['writer_id']),
								writer = writer_for_model
								)
			model.save()

			return HttpResponseRedirect('http://127.0.0.1:8000/')
		else:
			return HttpResponse(form.errors)

def date_transform(tr_date):
	if tr_date != '':
		iso_date_str = tr_date.split('.')[::-1]
		iso_date_int = []
		for p in iso_date_str:
			iso_date_int.append(int(p))
		iso_date=datetime.date(iso_date_int[0], iso_date_int[1], iso_date_int[2])
		return iso_date
	else:
		return datetime.date(1984, 1, 1)


def abstract_transform(client_value):
	if client_value == 'Yes':
		return True
	elif client_value == 'No':
		return False

def dl_transform(client_val):
	client_val = client_val.strip()
	separator_index = client_val.index(':')
	hours = int(client_val[:separator_index].strip())
	minutes = int(client_val[separator_index+1:-2].strip())
	if client_val[-2:] == 'AM':
		return datetime.time(hours, minutes)
	elif client_val[-2:] == 'PM':
		hours += 12
		return datetime.time(hours, minutes)

'''
def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	registered = False
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registered = True
		else:
			return HttpResponse(user_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return HttpResponseRedirect('http://127.0.0.1:8000/personal/')
'''

def user_login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request. method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				if user.userprofile.role == 'writer':
					return HttpResponseRedirect('/personal_cabinet/')
				elif user.userprofile.role == 'controller':
					return HttpResponseRedirect('/controller_cabinet/')
				elif user.userprofile.role == 'admin':
					return HttpResponseRedirect('http://127.0.0.1:8000/')
			else:
				return HttpResponse('this account is disabled')
		else:
			return HttpResponse("Invalid login details")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('http://127.0.0.1:8000/')

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		user_form = UserForm(request.POST)
		user_profile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and user_profile_form.is_valid():
			user_model = User(
				username=request.POST['username'],
				email=request.POST['email'],
				password=request.POST['password'],
				first_name=request.POST['first_name'],
				last_name=request.POST['last_name'])
			user_model.set_password(user_model.password)
			user_model.save()
			user_profile_model = UserProfile(
				mobile_number=request.POST['mobile_number'],
				social=request.POST['social'],
				user = user_model)

			user_profile_model.save()

			return HttpResponseRedirect('/login/')
		else:
			return HttpResponse(form.errors)


def index(request):
	as_writer = False
	as_controller = False
	user = request.user
	if user.is_authenticated():
		user_model = User.objects.get(email=user.email)
		if user_model.userprofile.role == 'writer':
			as_writer = True
		elif user_model.userprofile.role == 'controller':
			as_controller = True
		return render(request, 'index.html', {'as_writer':as_writer, 'as_controller':as_controller})
	else: return render(request, 'index.html')

@login_required
def available_orders(request):
	orders = Order_model.objects.filter(status='available')
	return render(request, 'available_orders.html', {'orders':orders})



def upload_order_file(request):
	order_number = request.POST['order_num']
	order = Order_model.objects.get(number=order_number)
	form = UploadOrderFileForm(request.POST, request.FILES)
	if form.is_valid():
		order.order_file = request.FILES['order_file']
		order.save()
		order.status = 'on checking'
		order.save()
		return HttpResponseRedirect('/personal/')
		return HttpResponse('invalid')

def for_check(request):
	orders = Order_model.objects.filter(status='on checking')
	return render(request, 'for_check.html', {'orders':orders})

def results_of_checking(request):
	result = request.POST['result_of_checking']
	if result.startswith('set_as_done'):
		order_number = result[11:]
		order = Order_model.objects.get(number=order_number)
		order.status = 'done'
		order.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/controller_cabinet/')
	elif result.startswith('return_to_writer'):
		order_number = result[16:]
		order = Order_model.objects.get(number=order_number)
		order.status = 'returned for revision'
		order.times_returned_for_revision = F('times_returned_for_revision') + 1
		order.save()
		return HttpResponseRedirect('/controller_cabinet/')


def on_checking_orders(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='on checking')
	if request.method == 'GET':
		return render(request, 'personal.html', {'orders':orders, 'user':user})

def completed_orders(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='done')
	if request.method == 'GET':
		return render(request, 'personal.html', {'orders':orders, 'user':user})



def apply_order(request):
	order = Order_model.objects.get(number=request.POST['order_num'])
	user = request.user
	user_model = User.objects.get(email=user.email)
	try:
		tender = order.tender
		tender.writers.add(user_model)
		return HttpResponseRedirect('/to_apply_order_list/')
	except:
		tender = Tender(order=order)
		tender.save()
		tender.writers.add(user_model)
		tender.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/personal_cabinet/')

def to_apply_list(request):
	tenders = Tender.objects.all()
	return render(request, 'to_apply.html', {'tenders':tenders})

def set_writer(request):
	value = request.POST['values']
	separator_index = value.index('//')
	writer_id = value[:separator_index]
	writer = User.objects.get(id=writer_id)
	order_num = value[separator_index+2:]
	order = Order_model.objects.get(number=order_num)
	tender = order.tender
	order.writer = writer
	order.save()
	order.status = 'in progress'
	order.save()
	tender.delete()
	return HttpResponseRedirect('/to_apply_order_list/')




def for_precheck_list(request):
	orders = Order_model.objects.filter(status='on pre-check')
	return render(request, 'for_check.html', {'orders':orders})
'''
def return_from_precheck(request):
	comment_form = CommentFromControllerForm(request.POST)
	user = User.objects.get(email=request.user.email)
	order = Order_model.objects.get(number=request.POST['order_num'])
	if comment_form.is_valid():
		model = Comment(
			text = request.POST['controller_comment'],
			order = order,
			author = user,
			create_date = datetime.datetime.now()
			)
		model.save()
		order.status = 'in progress'
		order.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/available_orders')
	else:
		return HttpResponse(comment_form.errors)
'''
def returnen_from_precheck_list(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='returned from pre-check')
	if request.method == 'GET':
		return render(request, 'personal.html', {'orders':orders, 'user':user})



def create_message(request):
	comment_form = CommentForm(request.POST)
	user = User.objects.get(email=request.user.email)
	order = Order_model.objects.get(number=request.POST['order_num'])
	if comment_form.is_valid():
		model = Comment(
			text = request.POST['comment'],
			order = order,
			author = user,
			create_date = datetime.datetime.now()
			)
		model.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/'+str(request.POST['order_num']))
	else:
		return HttpResponse(comment_form.errors)


def add_file_to_order(request):
	file_form = FileForm(request.POST, request.FILES)
	user = User.objects.get(email=request.user.email)
	order = Order_model.objects.get(number=request.POST['order_num'])
	if file_form.is_valid():
		order_file = FileModel(
			author = user,
			order = order,
			order_file = request.FILES['order_file'],
			create_date = datetime.datetime.now()
			)
		order_file.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/'+str(request.POST['order_num']))
	else:
		return HttpResponse(file_form.errors)


def upload_final_order_file(request):
	order_number = request.POST['order_num']
	order = Order_model.objects.get(number=order_number)
	user = User.objects.get(email=request.user.email)
	if order.status == 'in progress':
		form = UploadOrderFileForm(request.POST, request.FILES)
		if form.is_valid():
			final_file_model = FileModel(
				author = user,
				order = order,
				order_file = request.FILES['order_file'],
				create_date = datetime.datetime.now(),
				is_final = True
				)
			final_file_model.save()
			order.status = 'on checking'
			order.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/personal_cabinet')
		else:
			return HttpResponse(form.errors)
	elif order.status == 'returned for revision':
		prev_final_file = order.filemodel_set.get(is_final=True)
		prev_final_file.is_final = False
		prev_final_file.save()
		form = UploadOrderFileForm(request.POST, request.FILES)
		if form.is_valid():
			final_file_model = FileModel(
				author = user,
				order = order,
				order_file = request.FILES['order_file'],
				create_date = datetime.datetime.now(),
				is_final = True
				)
			final_file_model.save()
			order.status = 'on checking with controller'
			order.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/personal_cabinet')

	elif order.status == 'on checking' or order.status == 'on checking with controller':
		prev_final_file = order.filemodel_set.get(is_final=True)
		prev_final_file.is_final = False
		prev_final_file.save()
		form = UploadOrderFileForm(request.POST, request.FILES)
		if form.is_valid():
			final_file_model = FileModel(
				author = user,
				order = order,
				order_file = request.FILES['order_file'],
				create_date = datetime.datetime.now(),
				is_final = True
				)
			final_file_model.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/personal_cabinet')
		else:
			return HttpResponse(form.errors)
	else: HttpResponseRedirect('http://127.0.0.1:8000/personal_cabinet')





def writers_personal_cabinet(request):
	#as default show all writers orders with status 'in progress'
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders_in_progress = user_model.order_model_set.filter(status='in progress')
	orders_returned_for_revision = user_model.order_model_set.filter(status='returned for revision')
	orders_on_checking = user_model.order_model_set.filter(status='on checking')
	orders_on_checking_with_controller = user_model.order_model_set.filter(status='on checking with controller')
	unconfirmed_orders = user_model.order_model_set.filter(status='unconfirmed')
	if request.method == 'GET':
		return render(request, 'writers_cabinet_page.html',
		 {'orders_in_progress':orders_in_progress,
		 'user':user,
		 'orders_returned_for_revision':orders_returned_for_revision,
		 'orders_on_checking':orders_on_checking,
		 'orders_on_checking_with_controller':orders_on_checking_with_controller,
		 'unconfirmed_orders':unconfirmed_orders,
		 })


def in_progress_orders(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='in progress')
	if request.method == 'GET':
		return render(request, 'personal.html', {'orders':orders, 'user':user})


def writers_orders_on_checking(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='on checking')
	if request.method == 'GET':
		return render(request, 'writers_cabinet_page.html', {'orders':orders, 'user':user})

def done_writers_orders(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='done')
	if request.method == 'GET':
		return render(request, 'writers_cabinet_page.html', {'orders':orders, 'user':user})

def returned_for_revision_writers_orders(request):
	user = request.user
	user_model = User.objects.get(email=user.email)
	orders = user_model.order_model_set.filter(status='returned for revision')
	if request.method == 'GET':
		return render(request, 'writers_cabinet_page.html', {'orders':orders, 'user':user})

def controller_cabinet(request):
	user = User.objects.get(email=request.user.email)
	orders = user.userprofile.order_model_set.filter(status='on checking with controller')
	return render(request, 'controller_cabinet.html', {'orders':orders})

def take_for_check(request):
	user = User.objects.get(id=request.user.id)
	order = Order_model.objects.get(number=request.POST['order_num'])
	userprofile = user.userprofile
	order.controller = userprofile
	order.save()
	order.status='on checking with controller'
	order.save()
	return HttpResponseRedirect('http://127.0.0.1:8000/'+str(request.POST['order_num']))


@login_required
def order_page(request, number):
	user = User.objects.get(email=request.user.email)
	role = user.userprofile.role
	status_available = False
	status_in_progress = False
	comments = None
	files_list = None
	order = Order_model.objects.get(number=number)
	status_on_checking = False
	status_on_checking_with_controller = False
	final_file = None
	status_returned_for_revision = False

	if order.status == 'available':
		status_available = True

	elif order.status == 'in progress':
		status_in_progress = True
		comments = order.comment_set.order_by('-create_date')
		files_list = order.filemodel_set.filter(is_final=False).order_by('-create_date')

	elif order.status == 'on checking':
		status_on_checking = True

	elif order.status == 'on checking with controller':
		status_on_checking_with_controller = True
		comments = order.comment_set.order_by('-create_date')
		files_list = order.filemodel_set.filter(is_final=False).order_by('-create_date')
		final_file = order.filemodel_set.get(is_final=True)

	elif order.status == 'returned for revision':
		status_returned_for_revision = True
		comments = order.comment_set.order_by('-create_date')
		files_list = order.filemodel_set.order_by('-create_date')



	return render(request, 'order_page.html', {
		'order':order,
		'status_available':status_available,
		'status_in_progress':status_in_progress,
		'comments':comments,
		'files_list':files_list,
		'status_on_checking':status_on_checking,
		'status_on_checking_with_controller':status_on_checking_with_controller,
		'final_file':final_file,
		'status_returned_for_revision':status_returned_for_revision,
		})



def order_page_a(request, number):
	order = Order_model.objects.get(number=number)
	user = User.objects.get(id=request.user.id)
	user_role = user.userprofile.role
	comments = order.comment_set.order_by('-create_date')
	files_list = order.filemodel_set.filter(is_final=False).order_by('-create_date')
	admin = User.objects.filter(is_staff = True)
	messages_and_files_form = False
	apply_order_button = False
	messages_and_files_in_available_status_form = False
	final_file_upload_form = False
	take_for_check_button = False
	controller_decision =False
	final_file_link = False
	final_file = False
	confirmation_menu = False


	if user_role == 'writer':
		if order.status == 'available':
			apply_order_button = True
			messages_and_files_form = True
			comments = order.comment_set.filter(Q(author=user)|Q(author=admin)).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=user)|Q(author=admin)).order_by('-create_date')
		elif order.status == 'in progress':
			messages_and_files_form = True
			comments = order.comment_set.filter(Q(author=user)|Q(author=admin)).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=user)|Q(author=admin)).order_by('-create_date')
			final_file_upload_form = True
		elif order.status == 'on checking':
			messages_and_files_form = True
			comments = order.comment_set.filter(Q(author=user)|Q(author=admin)|Q(author__userprofile__role='controller')).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=user)|Q(author=admin)|Q(author__userprofile__role='controller')).filter(is_final=False).order_by('-create_date')
			final_file_upload_form = True
		elif order.status == 'on checking with controller':
			controller = order.controller.user
			messages_and_files_form = True
			comments = order.comment_set.filter(Q(author=user)|Q(author=admin)|Q(author=controller)).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=user)|Q(author=admin)|Q(author=controller)).filter(is_final=False).order_by('-create_date')
			final_file_upload_form = True
		elif order.status == 'returned for revision':
			controller = order.controller.user
			messages_and_files_form = True
			comments = order.comment_set.filter(Q(author=user)|Q(author=admin)|Q(author=controller)).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=user)|Q(author=admin)|Q(author=controller)).filter(is_final=False).order_by('-create_date')
			final_file_upload_form = True

		elif order.status == 'unconfirmed':
			confirmation_menu = True
			messages_and_files_form = True

		elif order.status == 'done':
			pass
	elif user_role == 'controller':
		if order.status == 'available':
			return HttpResponseRedirect('http://127.0.0.1:8000/')
		elif order.status == 'in progress':
			return HttpResponseRedirect('http://127.0.0.1:8000/')
		elif order.status == 'on checking':
			writer = order.writer
			messages_and_files_form = True
			take_for_check_button = True
			comments = order.comment_set.filter(Q(author=writer)|Q(author=admin)|Q(author=user)|Q(author__userprofile__role='controller')).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=writer)|Q(author=admin)|Q(author=user)).filter(is_final=False).order_by('-create_date')

		elif order.status == 'on checking with controller':
			writer = order.writer
			messages_and_files_form = True
			comments = order.comment_set.filter(Q(author=writer)|Q(author=admin)|Q(author=user)).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=writer)|Q(author=admin)|Q(author=user)).filter(is_final=False).order_by('-create_date')
			controller_decision = True
			final_file_link=True
			final_file = order.filemodel_set.get(is_final=True)
		elif order.status == 'returned for revision':
			writer = order.writer
			messages_and_files_form = True
			comments = order.comment_set.filter(Q(author=writer)|Q(author=admin)|Q(author=user)).order_by('-create_date')
			files_list = order.filemodel_set.filter(Q(author=writer)|Q(author=admin)|Q(author=user)).filter(is_final=False).order_by('-create_date')
		elif order.status == 'done':
			pass
	elif user_role == 'admin':
		messages_and_files_form = True
		comments = order.comment_set.order_by('-create_date')
		files_list = order.filemodel_set.order_by('-create_date')
	return render(request, 'order_page_a.html',
			{
			'user':user,
			'order':order,
			'comments':comments,
			'apply_order_button':apply_order_button,
			'messages_and_files_form':messages_and_files_form,
			'files_list':files_list,
			'admin':admin,
			'final_file_upload_form':final_file_upload_form,
			'take_for_check_button':take_for_check_button,
			'controller_decision':controller_decision,
			'final_file':final_file,
			'final_file_link':final_file_link,
			'confirmation_menu':confirmation_menu,
			}
		)


def confirmation(request):
	order = Order_model.objects.get(number=request.POST['order_num'])
	user = User.objects.get(id=request.user.id)
	if request.POST['writers_desigion'] == 'confirm':
		order.status = 'in progress'
	elif request.POST['writers_desigion'] == 'reject':
		rejection = Rejection(
			rejector = User.objects.get(id = request.user.id),
			order = order,
			date_of_rejection = datetime.datetime.now()
			)
		rejection.save()
		order.status = 'available'
		order.writer = None
	order.save()
	user.save()
	return HttpResponseRedirect('http://127.0.0.1:8000/personal_cabinet')
