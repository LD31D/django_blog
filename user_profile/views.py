from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from .forms import ProfileEditForm


class ProfileView(DetailView):
	template_name = 'user_profile/profile/index.html'

	def get_object(self):
		self.user = get_object_or_404(User, username=self.kwargs['username'])
		return self.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
	template_name = 'user_profile/profile_edit/index.html'
	form_class = ProfileEditForm

	def get_success_url(self):
		return reverse('profile:user_profile', kwargs={'username': self.request.user.username})

	def get_object(self, queryset=None):
		user_profile = get_object_or_404(UserProfile, user=self.request.user)
		return user_profile
