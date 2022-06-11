# def my_context_processor(req):
#     return {
#         'domain_name': 'https://hogehoge.com',
#         'site_name': 'Hogehoge Site',
#     }

from .models import *

def my_context_processor(request):
    if request.user.id is None:
        return {}
    else:
        # 未読件数を表示
        c_num = ReadStates.objects.filter(user=request.user, information__is_draft=False).count()
        midoku_info = ""
        if c_num > 0:
            midoku_info = str(c_num)        

        return {
            'midoku_info': midoku_info,
        }