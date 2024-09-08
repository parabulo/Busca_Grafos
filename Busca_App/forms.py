from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

TIPOS_DE_BUSCA = [
    ('a', 'Amplitude'),
    ('p', 'Profundidade'),
    ('pl', 'Profunidade Limitada'),
    ('ai', 'Aprofundamento Iterativo'),
    ('b', 'Bidirecional'),
]

class Form_Busca(forms.Form):
    tipo_busca = forms.ChoiceField(choices=TIPOS_DE_BUSCA)
    node_start = forms.CharField(label='Nó de Entrada', max_length=100)
    node_end = forms.CharField(label="Nó de Chegada", max_length=100)
    limite_busca = forms.IntegerField(label="Limite(PL)/Limite Máximo(AI)", required=False)

    def __init__(self, *args, **kwargs):
        super(Form_Busca, self).__init__(*args, **kwargs)
        if 'tipo_busca' in self.data and self.data['tipo_busca'] == 'pl' or 'ai':
            self.fields['limite_busca'].required = True
        else:
            self.fields['limite_busca'].widget = forms.HiddenInput()
