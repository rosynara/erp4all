from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone #para usar com timezone.now()

#para usar com def get_absolute_url(self): return reverse('hello:produto_detail', kwargs={'pk':self.pk})


# Create your models here.
class Unidade(models.Model):
    descricao = models.CharField(max_length=120)
    validadedt = models.DateField(null=True)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Marca(models.Model):
    descricao = models.CharField(max_length=120)
    validadedt = models.DateField(null=True)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Local(models.Model):
    descricao = models.CharField(max_length=120)
    validadedt = models.DateField(null=True)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

class Item(models.Model):
    descricao = models.CharField(max_length=250)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=5, blank=True, null=True)
    cor = models.CharField(max_length=120, blank=True, null=True)
    tipo_item = models.SmallIntegerField()
    descricaocompleta = models.TextField()
    codigobarras = models.CharField(max_length=100, blank=True, null=True)
    validadedt = models.DateField(blank=True, null=True)
    qtdeminima = models.IntegerField(default=0)
    qtdeideal = models.IntegerField(default=1)
    duracaoh = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)



    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Pessoa(models.Model):
    tipopessoa = models.SmallIntegerField()
    doccpfcnpj = models.CharField(max_length=20)
    nome = models.CharField(max_length=120)
    nomefantasia = models.CharField(max_length=120)
    docrg = models.CharField(max_length=20, blank=True, null=True)
    docpispasep = models.CharField(max_length=20, blank=True, null=True)
    docinscestadual = models.CharField(max_length=20, blank=True, null=True)
    docinscmunicipal = models.CharField(max_length=20, blank=True, null=True)
    criacaodt = models.DateField()
    encerramentodt = models.DateField(null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome


class ItemMovManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ItemMovManager,self)
    def vendas(self, *args, **kwargs):
        return super(ItemMovManager, self).filter(tipomovimento=-1)
    def compras(self, *args, **kwargs):
        return super(ItemMovManager, self).filter(tipomovimento=1)


class ItemMov(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    movimentodt = models.DateField()
    tipomovimento = models.SmallIntegerField()
    qtdemovimento = models.IntegerField()
    valormovimento = models.DecimalField(decimal_places=2, max_digits=12)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valorunitario = models.DecimalField(decimal_places=2, max_digits=12)
    valorsubtotal = models.DecimalField(decimal_places=2, max_digits=12)
    prdesconto = models.DecimalField(decimal_places=2, max_digits=4)
    valordesconto = models.DecimalField(decimal_places=2, max_digits=12)
    valorliquido = models.DecimalField(decimal_places=2, max_digits=12)
    valorimpostosdebito = models.DecimalField(decimal_places=2, max_digits=12)
    valorimpostoscredito = models.DecimalField(decimal_places=2, max_digits=12)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    objects = ItemMovManager()



    def get_absolute_url(self):
        return reverse('vendas:vendas_detalhe', kwargs={'pk': self.pk})

    def set_venda_defaults(self):
        if not self.tipomovimento:
            self.tipomovimento = -1
        if not self.movimentodt:
            self.movimentodt = timezone.now()
        if not self.valorimpostosdebito:
            self.valorimpostosdebito = 0
        if not self.valorimpostoscredito:
            self.valorimpostoscredito = 0
        if not self.valormovimento:
            self.valormovimento = self.valorliquido

                #def pode_vender(self):
