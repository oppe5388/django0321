# import random
# import string
# from django.contrib.auth.backends import ModelBackend
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth import get_user_model

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
