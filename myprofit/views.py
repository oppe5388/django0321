from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Post

def used02(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/used02.html', context)

def used03(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/used03.html', context)

def used04(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/used04.html', context)

def used05entry(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'form': PostCreateForm, # 商品とコースのプルダウン
    }
    context['parentcategory_list'] = ParentCategory.objects.all()# 商品とコースのプルダウン
    context['classdrop_list'] = ClassDrop.objects.all()# 車種クラスプルダウン
    return render(request, 'myprofit/used05entry.html', context)

def used05(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/used05.html', context)

def used06(request):
    #会員証番号欄→これも未使用なのでcontext = {}で良さそう
    searchForm = SearchForm(request.GET)
    context = {
        'searchForm': searchForm,
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/used06.html', context)

def used06confirm(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/used06confirm.html', context)

def used07(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/used07.html', context)

def history(request):
    return render(request, 'myprofit/history.html')
    

def profit_top(request):
    context ={'aaa': ''}
    return render(request, 'myprofit/top.html', context)


def new02(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/new02.html', context)

def new03(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/new03.html', context)

def new04(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/new04.html', context)

def new05entry(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'form': PostCreateForm, # 商品とコースのプルダウン
    }
    context['parentcategory_list'] = ParentCategory.objects.all()# 商品とコースのプルダウン
    context['classdrop_list'] = ClassDrop.objects.all()# 車種クラスプルダウン
    return render(request, 'myprofit/new05entry.html', context)

def new05(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/new05.html', context)

def new06(request):
    #会員証番号欄→これも未使用なのでcontext = {}で良さそう
    searchForm = SearchForm(request.GET)
    context = {
        'searchForm': searchForm,
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/new06.html', context)

def new06confirm(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/new06confirm.html', context)

def new07(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/new07.html', context)

def service02(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/service02.html', context)

def service03(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/service03.html', context)

def service04(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/service04.html', context)

def service05entry(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
        'form': PostCreateForm, # 商品とコースのプルダウン
    }
    context['parentcategory_list'] = ParentCategory.objects.all()# 商品とコースのプルダウン
    context['classdrop_list'] = ClassDrop.objects.all()# 車種クラスプルダウン
    return render(request, 'myprofit/service05entry.html', context)

def service05(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/service05.html', context)

def service06(request):
    #会員証番号欄→これも未使用なのでcontext = {}で良さそう
    # searchForm = SearchForm(request.GET)
    context = {
        # 'searchForm': searchForm,
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/service06.html', context)

def service06confirm(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/service06confirm.html', context)

def service07(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
        'cancel_flag': request.GET.get('cancel_flag'),
    }
    return render(request, 'myprofit/service07.html', context)

def service01(request):
    context = {
        'route': request.GET.get('route'),
        'cert_no': request.GET.get('cert_no'),
    }
    return render(request, 'myprofit/service01.html', context)


def entry_example(request):

    form = PostCreateForm # 商品とコースのプルダウン
    context ={
        'form': form,
    }
    context['parentcategory_list'] = ParentCategory.objects.all()# 商品とコースのプルダウン
    context['classdrop_list'] = ClassDrop.objects.all()# 車種クラスプルダウン
    context['carforprice_list'] = CarForPrice.objects.all().order_by('id')# 車種クラスプルダウン
    return render(request, 'myprofit/entry_example.html', context)

def car(request, pk):
    
    # form = CarInsertForm(request.POST)
    
    context ={
        'cardrop_list': CarDrop.objects.filter(parent=pk).order_by('id'), #該当の車種
        # 'carclass': get_object_or_404(ClassDrop, pk=pk), #該当のクラス
        'carclass': ClassDrop.objects.filter(id=pk).first(),#該当のクラス
        # 'form': form,
    }
    
    # # 元の画面に車名と3桁を差し込み（車名クリックでsubmit）
    # if form.is_valid():
    #     context['car_name'] = form.cleaned_data['car']
    #     context['car_digit'] = form.cleaned_data['digit']
    #     context['function_name'] = 'insert_car' #JS関数名

    #     return render(request, 'myprofit/car_close.html', context)
    
    return render(request, 'myprofit/car.html', context)


def search_example(request):
    context = {
    }
    return render(request, 'myprofit/search_example.html', context)