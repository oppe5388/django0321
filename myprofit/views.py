from django.shortcuts import render


def profit_top(request):
    context ={'aaa': ''}
    return render(request, 'myprofit/top.html', context)

def new01(request):
    context ={'aaa': ''}
    return render(request, 'myprofit/new01.html', context)

def new02(request):
    context ={'aaa': ''}
    return render(request, 'myprofit/new02.html', context)

def new03(request):
    context ={'aaa': ''}
    return render(request, 'myprofit/new03.html', context)

def new04(request):
    context ={'aaa': ''}
    return render(request, 'myprofit/new04.html', context)
    