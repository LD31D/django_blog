from django.urls import path

from .views import *


urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
	path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]
