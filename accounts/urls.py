from django.urls import path

from .views import *


urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
	path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset-password/done/', ResetPasswordDoneView.as_view(), name='reset_password_done'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', ResetPasswordCompleteView.as_view(), name='password_reset_complete')
]
