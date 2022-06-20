from django.shortcuts import render


def profit_top(request):
    context ={
            'aaa': '',
        }

    return render(request, 'myprofit/top.html', context)
