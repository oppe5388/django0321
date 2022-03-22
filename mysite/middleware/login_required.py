from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.user.is_authenticated:
            if request.path != '/accounts/login/':
                return HttpResponseRedirect('/accounts/login/')            
        return response