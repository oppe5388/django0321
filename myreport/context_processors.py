from .models import *

def my_context_processor(request):
    if request.user.id is None:
        return {}
    else:
        # 未読件数を表示
        c_num = ReportRead.objects.filter(user=request.user).count()
        midoku = ""
        if c_num > 0:
            midoku = str(c_num)        

        return {
            'midoku': midoku,
            'site_name': 'Hogehoge Site',
        }
    