from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from style_app.forms import ClientForm
from style_app.models import Client


# Create your views here.
def Main_template(request):
	form = {}
	errors = []
	if request.POST:
		form['name'] = request.POST.get('name')
		form['phone'] = request.POST.get('phone')

		if not form['name']:
			errors.append('Заполните имя')

		if not form['phone']:
			errors.append('Введите Ваш контактный номер')

		if not errors:
			p = Client(client_name=form['name'], client_phone=form['phone'])
			p.save()
	return render(request, 'main.html', {'errors': errors})


def Katalog_template(request):
	return render(request, 'katalog.html')


def About_us_template(request):
	return render(request, 'about_us.html')


def Price_template(request):
	return render(request, 'price.html')


def Contacts_template(request):
	return render(request, 'contacts.html')


def k1_template(request):
	return render(request, '1.html')

def k2_template(request):
	return render(request, '2.html')

def k3_template(request):
	return render(request, '3.html')

def k4_template(request):
	return render(request, '4.html')

def k5_template(request):
	return render(request, '5.html')

def k6_template(request):
	return render(request, '6.html')