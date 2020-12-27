from django.urls import path

from .views import *


urlpatterns = [
	path('edit/', ProfileEditView.as_view(), name='user_profile_edit'),
	path('view/<str:username>/', ProfileView.as_view(), name='user_profile'),
]
