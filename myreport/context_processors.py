# from .models import *
# from accounts.models import User
# from django.contrib.auth.decorators import login_required

# @login_required
# def my_context_processor(request):
#     pass
#     # 未読件数を表示
#     c_num = ReportRead.objects.filter(user=request.user).count()
#     midoku = ""
#     if c_num > 0:
#         midoku = str(c_num)        

#     return {
#         'midoku': midoku,
#         'site_name': 'Hogehoge Site',
#     }