"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.views.generic import TemplateView para usar com url(r'^about/$', TemplateView.as_view(templatename="about.html")), outra opção é em views.py criar  class AboutView(TemplateView):     template_name = "about.html" e em urls.py fazer from some_app.views import AboutView  urlpatterns = [ url(r'^about/$', AboutView.as_view()),]

# url(r'regular expression', destination method, name='optional name')

app_name = 'vendas'
urlpatterns = [
    url(r'vendas_home', views.vendas_home, name='vendas_home'),
    url(r'vendas_lista', views.vendas_lista, name='vendas_lista'),
    url(r'vendas_detalhe/(?P<pk>[0-9]+)/$', views.vendas_detalhe, name = 'vendas_detalhe'),
    #url(r'^(?P<pk>[0-9]+)/$', views.ItemMovDetailView.as_view(), name='vendas_detalhe'),
    url(r'venda/novo/$', views.ItemMovNovo.as_view(), name='vendas_novo'),
    url(r'venda/nova/$', views.vendas_nova, name='vendas_nova'),

]

urlpatterns += staticfiles_urlpatterns()
