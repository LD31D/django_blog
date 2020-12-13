from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404


class ProfileView(DetailView):
	template_name = 'user_profile/profile/index.html'

	def get_object(self):
		self.user = get_object_or_404(User, username=self.kwargs['username'])
		return self.user
