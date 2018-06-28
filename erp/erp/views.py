from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.http import HttpResponseRedirect


from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#from django.views import generic
#from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from .models import Pergunta, Produto, Unidade_Medida

# Create your views here.

def index(request):
    return render(request, 'index.html')



def login_view(request):
    if request.user.is_authenticated():
        return render(request, 'index.html')  # render(request, 'admin/login.html')

    form = LoginForm(request.POST or None)

    url_retorno = request.POST.get("url_retorno")
    if request.method == 'POST':

        if form.is_valid():
            usuario = form.cleaned_data.get("usuario")
            senha = form.cleaned_data.get("senha")
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                login(request, user)
                #messages.success(request, "Login realizado com sucesso!") #, extra_tags="callout callout-info")
                if not url_retorno:
                    return render(request, "index.html") #HttpResponseRedirect(render(request, 'index.html'))
                else:
                    return render(request, url_retorno)
            else:
                messages.error(request, "Erro ao efetuar login")
                context = {"form": form,
                           "url_inicial": url_retorno
                           }
                return render(request, "login.html", context)
        else:
            messages.error(request, "Tente novamente")
            context = {"form": form,
                       "url_inicial": url_retorno
                       }
            return render(request, "login.html", context)
    else:
        context = {"form": form,
               "url_inicial": url_retorno
                   }
        return render(request, "login.html", context)




def logout_view(request):
    logout(request)
    return render(request, 'index.html')