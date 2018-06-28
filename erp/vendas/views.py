from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.conf import settings

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils import timezone #para usar com timezone.now()
from django.db.models import Q  #para usar com filter( Q() | Q())

# from django.contrib.auth.decorators import login_required # para usar com @login_required

from .forms import VendaForm


# Create your views here.
from core.models import ItemMov, Item, Local, Pessoa, Unidade, Marca

def vendas_home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("login")) #render(request, 'admin/login.html')

    context = {"titulo": "Vendas"}
    #return HttpResponse("<h1>Hello Vendas!!!</h1>")
    return render(request, 'vendas/vendas_home.html', context)

def vendas_lista(request):
    if not request.user.is_authenticated():
        context = {"url_retorno": "{% url 'vendas:vendas_lista' %}"}
        return HttpResponseRedirect(reverse("login"), context)  # render(request, 'admin/login.html')

    #@login_required(redirect_field_name='index')
    filtro_cliente = request.GET.get("p")
    filtro_item = request.GET.get("i")
    #filtro_vendedor = request.GET.get("u")
    itemmov_todos = ItemMov.objects.vendas().order_by('-movimentodt', 'pessoa', 'item') #[:5]

    if filtro_cliente:
        itemmov_todos = itemmov_todos.filter(pessoa__nome__icontains=filtro_cliente)
    if filtro_item:
        itemmov_todos = itemmov_todos.filter(item__descricao__icontains=filtro_item)
    #if filtro_vendedor:
    #    itemmov_todos = itemmov_todos.filter(
    #                        Q(user__first_name__icontains=filtro_vendedor) |
    #                        Q(user__last_name__icontains=filtro_vendedor)|
    #                        Q(user__username__icontains=filtro_vendedor)
    #    ).distinct()

    paginacao = Paginator(itemmov_todos, 10)
    page_request_var = "pagina"
    pagina = request.GET.get(page_request_var)
    num_paginas = paginacao.num_pages


    try:
        itemmov_pagina = paginacao.page(pagina)
    except PageNotAnInteger:
        itemmov_pagina = paginacao.page(1)
    except EmptyPage:
        itemmov_pagina = paginacao.page(paginacao.num_pages)

    context = {
            'itemmov_grid': itemmov_pagina,
            'page_request_var': page_request_var,
            'num_paginas': num_paginas
    }
    return render(request, 'vendas/vendas_lista.html', context)

def vendas_detalhe(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("admin:login"))  # render(request, 'admin/login.html')

    #itemmov_det = ItemMov.objects.get(id=1)
    itemmov_det = get_object_or_404(ItemMov, pk=pk)
    context = {"itemmov_det": itemmov_det}
    return render(request, 'vendas/vendas_detalhe.html', context)

def vendas_nova(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return HttpResponseRedirect(reverse("admin:login"))  # render(request, 'admin/login.html')

    dados = {"prdesconto": 0, "valordesconto": 0}

    form = VendaForm(request.POST or None, initial=dados)
    # ou:
    # form = VendaForm(dados)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.set_venda_defaults()
            instance.save()
            messages.success(request, "Salvo com sucesso!") #, extra_tags="callout callout-info")
            #HttpResponseRedirect(instance.get_absolute_url()) #mostra detalhes
            #HttpResponseRedirect(reverse("vendas:vendas_lista")) #não funciona

        else:
            messages.error(request, "Ocorreu um erro ao salvar!") #,extra_tags="callout callout-danger")

    context = {"form": form}
    return render(request, "vendas/vendas_form.html", context)


class ItemMovNovo(CreateView):
    model = ItemMov
    fields = ['item','local','movimentodt','tipomovimento','qtdemovimento','valormovimento','pessoa','valorunitario','valorsubtotal','prdesconto','valordesconto','valorliquido','valorimpostosdebito','valorimpostoscredito']
    template_name = 'vendas/vendas_form.html'



class ItemMovListView(generic.ListView):
    model = ItemMov
    template_name = 'vendas/vendas_lista.html'
    context_object_name = 'itemmov'

#class ItemMovDetailView(generic.DetailView):
#    model = ItemMov
#    template_name = 'vendas/vendas_detalhe.html'
#    context_object_name = 'itemmov_det'