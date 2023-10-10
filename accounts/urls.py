from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', include('two_factor.urls', namespace='two_factor')),
    # path('send-otp/', views.send_otp, name='send-otp'),
    
    # # # ワンタイム用にログイン画面変更
    # path('login/', views.login_view, name='login'),
    # # two-factor
    # path('enter-otp/', views.enter_otp, name='enter-otp'),

]