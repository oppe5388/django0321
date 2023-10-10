# from django.http import HttpResponse
# from django_otp.plugins.otp_email.models import EmailDevice

# def send_otp(request):
#     user = request.user
#     device, created = EmailDevice.objects.get_or_create(user=user, name='my-device')

#     if created:
#         device.generate_challenge()

#     return HttpResponse('OTP has been sent to your email.')


# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib import messages
# # from .otp_backend import EmailOTPBackend  # カスタム認証バックエンドをインポート

# import random
# import string
# from django.contrib.auth.backends import ModelBackend
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth import get_user_model


# # def login_view(request):
# #     if request.method == 'POST':
# #         username = request.POST.get('username')
# #         password = request.POST.get('password')
# #         user = authenticate(request, username=username, password=password)

# #         if user is not None:
# #             # backend = EmailOTPBackend()
# #             # backend.user_authenticated(user)  # OTPを生成してメールで送信
# #             return redirect('accounts:enter-otp')

# #     return render(request, 'registration/login.html')



# from django.shortcuts import render, redirect
# from django.contrib import messages

# # ワンタイムパスワード入力画面
# def enter_otp(request):
#     if request.method == 'POST':
#         otp_entered = request.POST.get('otp')
#         otp_sent = request.session.get('otp')  # セッションからOTPを取得

#         if otp_entered == otp_sent:
#             # OTPが一致した場合、ユーザーをログインさせます。
#             # （ここでは詳細なログイン処理は省略します）
#             return redirect('home')
#         else:
#             # OTPが一致しない場合、エラーメッセージを表示します。
#             messages.error(request, 'Invalid OTP. Please try again.')
    
#     return render(request, 'enter_otp.html')



# def generate_otp():
#     # 6桁のランダムな数字を生成します。
#     return ''.join(random.choice(string.digits) for _ in range(6))

# # class EmailOTPBackend(ModelBackend):
# #     def user_authenticated(self, user):
# #         otp = generate_otp()  # ワンタイムパスワードを生成する関数
# #         send_mail(
# #             'Your OTP',
# #             f'Your OTP is {otp}',
# #             settings.DEFAULT_FROM_EMAIL,
# #             [user.email],
# #             fail_silently=False,
# #         )
# #         return super().user_authenticated(user)
    
    
# from django.contrib.auth import get_user_model

# class EmailOTPBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         User = get_user_model()
#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         User = get_user_model()
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
