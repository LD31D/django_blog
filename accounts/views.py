from django.shortcuts import redirect
from django.views.generic import View, FormView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LogoutView(View):
	LOGOUT_URL = '/blog/'

	def get(self, request):
		logout(request)
		return redirect(self.LOGOUT_URL)


class CustomLoginView(LoginView):
	authentication_form = AuthenticationForm
	form_class = AuthenticationForm
	template_name = 'accounts/login/index.html'

	LOGIN_REDIRECT_URL = '/blog/'

	def get_redirect_url(self):
		return self.LOGIN_REDIRECT_URL

	def form_valid(self, form):
		user = form.get_user()
		login(self.request, user)
		return super(CustomLoginView, self).form_valid(form)


class RegisterView(FormView):
	template_name = 'accounts/register/index.html'
	form_class = UserCreationForm

	success_url = '/blog/'

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return super(RegisterView, self).form_valid(form)