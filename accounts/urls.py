from django.urls import path

from .views import *

urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
