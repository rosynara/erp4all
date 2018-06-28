from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect

#from django.views import generic
#from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




#from .models import Pergunta, Produto, Unidade_Medida

# Create your views here.

def core_home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("login"))

    return render(request, 'core/core_home.html')




