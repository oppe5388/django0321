# def my_context_processor(req):
#     return {
#         'domain_name': 'https://hogehoge.com',
#         'site_name': 'Hogehoge Site',
#     }

from .models import *
import jpbizday
from datetime import date, datetime, timedelta

def my_context_processor(request):

    # 発送日をつくる
    nowadays = datetime.now() #今日
    # 何かの時のために、表示しない日に設定したら、表示しない

    # それ以外
    mail_date = nowadays + timedelta(1)
    # 次の平日を取得
    while jpbizday.is_bizday(mail_date) == False:
        mail_date = mail_date + timedelta(1)

    #次の平日まで何日あるか
    date_cnt = (mail_date - nowadays) / timedelta(days=1) #整数に

    if date_cnt >= 2:
        next_mail_date = mail_date
    else:
        # 次の平日の次の平日を取得
        next_mail_date = mail_date + timedelta(1)
        while jpbizday.is_bizday(next_mail_date) == False:
            next_mail_date = next_mail_date + timedelta(1)

    #VCC休みは祝日とするでOK？祝日登録モデルを作成する


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
            'mail_date': mail_date,
            'next_mail_date': next_mail_date,
        }