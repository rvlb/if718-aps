from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout

from django.contrib import messages

from .collection import UserCollection

class UserControlador:
    @staticmethod
    def create_user(form):
        if form.is_valid():
            UserCollection.create_user(form)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect(reverse_lazy('core:index'))
        else:
            return None

    @staticmethod
    def log_user_in(request, form):
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse_lazy('core:index'))
        else:
            return None

    @staticmethod
    def log_user_out(request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('core:index'))

    @staticmethod
    def user_is_authenticated(request):
        return request.user.is_authenticated()