from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout

from accounts.collection import UserCollection
from menu.collection import MenuCollection

'''
We use this class to access the model layer and perform database operations
'''
class Facade:
    @staticmethod
    def create_user(form):
        if form.is_valid():
            UserCollection.create_user(form)
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

    @staticmethod
    def add_menu_item(form):
        if form.is_valid():
            MenuCollection.insert(form)
            return HttpResponseRedirect(reverse_lazy('menu:list'))
        else:
            return None

    @staticmethod
    def get_menu():
        return MenuCollection.get_menu()
