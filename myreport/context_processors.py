from .models import *
from accounts.models import User

def my_context_processor(request):

    # 未読件数を表示
    c_num = ReportRead.objects.filter(user=request.user).count()
    midoku = ""
    if c_num > 0:
        midoku = str(c_num)        

    return {
        'midoku': midoku,
        'site_name': 'Hogehoge Site',
    }