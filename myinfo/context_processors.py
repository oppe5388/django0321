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
    tomorrow = nowadays + timedelta(1) #明日
    # 表示しない日に設定したら、表示しない
    if Holiday.objects.filter(title="3", non_date=date.today()).exists():
        mail_date=""
        next_mail_date=""
        pass
    # それ以外
    else:
        mail_date = tomorrow
        # 次の平日を取得、VCC休業日は祝日と同じ扱い
        while jpbizday.is_bizday(mail_date) == False \
            or Holiday.objects.filter(title="1", non_date=mail_date).exists() \
            or Holiday.objects.filter(title="2", non_date=mail_date).exists():

            mail_date = mail_date + timedelta(1)

        #次の平日まで何日あるか
        vcc_cnt = Holiday.objects.filter(title="2", non_date__range=[tomorrow, mail_date]).count()
        date_cnt = (mail_date - nowadays) / timedelta(days=1) #整数に

        if date_cnt >= 2:
            if vcc_cnt +1 >= date_cnt:
                # 次の平日の次の平日を取得：下とコード重複してるけど分岐を書き直してない
                next_mail_date = mail_date + timedelta(1)
                while jpbizday.is_bizday(next_mail_date) == False \
                    or Holiday.objects.filter(title="1", non_date=next_mail_date).exists() \
                    or Holiday.objects.filter(title="2", non_date=next_mail_date).exists():
                
                    next_mail_date = next_mail_date + timedelta(1)
            else:
                next_mail_date = mail_date
        else:
            # 次の平日の次の平日を取得：上とコード重複してるけど分岐を書き直してない
            next_mail_date = mail_date + timedelta(1)
            while jpbizday.is_bizday(next_mail_date) == False \
                or Holiday.objects.filter(title="1", non_date=next_mail_date).exists() \
                or Holiday.objects.filter(title="2", non_date=next_mail_date).exists():
                
                next_mail_date = next_mail_date + timedelta(1)

        #VCC休みは祝日とするでOK？祝日登録モデルを作成する

    # FAXリンク用に今日の日付
    faxday = date.today().strftime('%Y-%m-%d')


    # 未読件数を表示
    if request.user.id is None:
        return {
            'mail_date': mail_date,
            'next_mail_date': next_mail_date,
            'faxday': faxday,
        }
    # LDはLD共有も含む
    elif request.user.id < 5 :
        
        c_num = ReadStates.objects.filter(user=request.user, information__is_draft=False).count()
        midoku_info = ""
        if c_num > 0:
            midoku_info = str(c_num)        

        return {
            'midoku_info': midoku_info,
            'mail_date': mail_date,
            'next_mail_date': next_mail_date,
            'faxday': faxday,
        }
    # OP
    else:
        c_num = ReadStates.objects.filter(user=request.user, information__is_draft=False, information__to_flag="").count()
        midoku_info = ""
        if c_num > 0:
            midoku_info = str(c_num)        

        return {
            'midoku_info': midoku_info,
            'mail_date': mail_date,
            'next_mail_date': next_mail_date,
            'faxday': faxday,
        }