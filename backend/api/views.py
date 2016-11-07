from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, check_password
from api.models import *
from api.forms import *

def login_user(request):
	if request.method == 'POST' and 'loginForm' in request.POST:
		l_form = loginForm(request.POST)
		s_form = signupForm()
		if l_form.is_valid():
			email = l_form.cleaned_data['email']
			password = l_form.cleaned_data['password']

			try:
				user_obj = User.objects.get(email=email)
			except:
				user_is_valid = False
				status = {
					'error': True,
					'error_message': 'Invalid Username or Password!',
					'success': False,
					'success_message': '',
				}
				
				variables = RequestContext(request, {
					'status': status,
					'loginForm': l_form,
					'signupForm':  s_form
				})
				return render_to_response('signup-page.html', variables)

			username = user_obj.username
			user = authenticate(username = username, password = password)

			if user != None:
				user_is_valid = True
				login(request, user)
				return HttpResponseRedirect('/home/')
			else:
				user_is_valid = False

			if user_is_valid == False:	
				status = {
					'error': True,
					'error_message': 'Invalid Username or Password!',
					'success': False,
					'success_message': '',
				}
			else:
				status = {
					'error': False,
					'error_message': '',
					'success': True,
					'success_message': 'Login Succesful!',
				}

			variables = RequestContext(request, {
				'status': status,
				'loginForm': l_form,
				'signupForm': s_form
			})
			return render_to_response('signup-page.html', variables)
	else:
		l_form = loginForm()
		s_form = signupForm()
		variables = RequestContext(request, {
			'loginForm': l_form,
			'signupForm': s_form
		})
		return render_to_response('login.html', variables)

	if request.method == 'POST' and 'signupForm' in request.POST:
		l_form = loginForm()
		s_form = signupForm(request.POST)
		existing_user = True

		if s_form.is_valid():
			first_name = s_form.cleaned_data['first_name']
			email = s_form.cleaned_data['email']
			password = s_form.cleaned_data['password']

			try:
				user_obj = User.objects.get(email=email)
			except:
				existing_user = False

			if(existing_user == True):
				status = {
					'error': True,
					'error_message': 'Account for the Email ID below already exists.',
					'success': False,
					'success_message': '',
				}
				variables = RequestContext(request, {
					'status': status,
					'loginForm': l_form,
					'signupForm': s_form
				})
				return render_to_response('signup-page.html', variables)
