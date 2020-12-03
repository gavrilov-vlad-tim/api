from django.urls import path

from .views import SignupView, success_signup

urlpatterns = [
    path('', SignupView.as_view(), name='signup'),
    path('success-signup/', success_signup, name='success_signup')

]
