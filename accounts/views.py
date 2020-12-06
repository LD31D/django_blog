from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import View


class LogoutView(View):
	LOGOUT_URL = '/blog/'

	def get(self, request):
		logout(request)
		return redirect(self.LOGOUT_URL)
