from django.urls import path
from user_app.apps import UserAppConfig
from user_app.views import LoginView, LogoutView, RegisterView, ProfileView, PasswordRecoveryView, verification_view

app_name = UserAppConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
    path('verification/', verification_view, name='verification'),

]
