from django import forms
from core.models import ItemMov


class VendaForm(forms.ModelForm):
    class Meta:
        model = ItemMov
        fields = [
            'local',
            'pessoa',
            'item',
            'valorunitario',
            'qtdemovimento',
            'valorsubtotal',
            'prdesconto',
            'valordesconto',
            'valorliquido'
        ]

        #, 'movimentodt' , 'tipomovimento', 'valormovimento', 'valorimpostosdebito','valorimpostoscredito'

    def clean_valorunitario(self):
        valor = self.cleaned_data.get('valorunitario')
        if valor <= 0:
            raise forms.ValidationError('Informe um valor maior do que zero.', code='negativozero')
        return valor

    def clean_qtdemovimento(self):
        valor = self.cleaned_data.get('qtdemovimento')
        if valor <= 0:
            raise forms.ValidationError('Informe um valor maior do que zero.', code='negativozero')
        return valor

    def clean_valorsubtotal(self):
        valor = self.cleaned_data.get('valorsubtotal')
        if valor <= 0:
            raise forms.ValidationError('Informe um valor maior do que zero.', code='negativozero')
        return valor

    def clean_prdesconto(self):
        valor = self.cleaned_data.get('prdesconto')
        if valor < 0:
            raise forms.ValidationError('Informe um valor maior ou igual a zero.', code='negativo')
        return valor

    def clean_valordesconto(self):
        valor = self.cleaned_data.get('valordesconto')
        if valor < 0:
            raise forms.ValidationError('Informe um valor maior ou igual a zero.', code='negativo')
        return valor


    def clean_valorliquido(self):
        valor = self.cleaned_data.get('valorliquido')
        if valor <= 0:
            raise forms.ValidationError('Informe um valor maior do que zero.', code='negativozero')
        return valor

#ValidationError(_('Invalid value: %(value)s'), params={'value': '42'},)






