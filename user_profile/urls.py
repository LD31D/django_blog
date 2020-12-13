from django.urls import path

from .views import *


urlpatterns = [
	path('<str:username>/', ProfileView.as_view(), name='user_profile')
]
