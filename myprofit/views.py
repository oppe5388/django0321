from django.shortcuts import render

# Create your views here.

#使用中のidndex
def profit_top(request):
    context ={
            'aaa': '',
        }

    return render(request, 'myprofit/top.html', context)