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

NOS_POSSIVEIS = [
    ('APARECIDA', 'APARECIDA'),
    ('ARAPEI', 'ARAPEÍ'),
    ('AREIAS', 'AREIAS'),
    ('BANANAL', 'BANANAL'),
    ('CACAPAVA', 'CAÇAPAVA'),
    ('CACHOEIRA PAULISTA', 'CACHOEIRA PAULISTA'),
    ('CAMPOS DO JORDAO', 'CAMPOS DO JORDÃO'),
    ('CANAS', 'CANAS'),
    ('CARAGUATATUBA', 'CARAGUATATUBA'),
    ('CRUZEIRO', 'CRUZEIRO'),
    ('CUNHA', 'CUNHA'),
    ('GUARATINGUETA', 'GUARATINGUETA'),
    ('IGARATA', 'IGARATA'),
    ('ILHABELA', 'ILHABELA'),
    ('JACAREI', 'JACAREÍ'),
    ('JAMBEIRO', 'JAMBEIRO'),
    ('LAGOINHA', 'LAGOINHA'),
    ('LAVRINHAS', 'LAVRINHAS'),
    ('LORENA', 'LORENA'),
    ('MONTEIRO LOBATO', 'MONTEIRO LOBATO'),
    ('NATIVIDADE DA SERRA', 'NATIVIDADE DA SERRA'),
    ('PARAIBUNA', 'PARAIBUNA'),
    ('PINDAMONHANGABA', 'PINDAMONHANGABA'),
    ('PIQUETE', 'PIQUETE'),
    ('POTIM', 'POTIM'),
    ('QUELUZ', 'QUELUZ'),
    ('REDENCAO DA SERRA', 'REDENÇÃO DA SERRA'),
    ('ROSEIRA', 'ROSEIRA'),
    ('SANTA BRANCA', 'SANTA BRANCA'),
    ('SANTO ANTONIO DO PINHAL', 'SANTO ANTÔNIO DO PINHAL'),
    ('SAO BENTO DO SAPUCAI', 'SÃO BENTO DO SAPUCAI'),
    ('SAO JOSE DO BARREIRO', 'SÃO JOSÉ DO BARREIRO'),
    ('SAO JOSE DOS CAMPOS', 'SÃO JOSÉ DOS CAMPOS'),
    ('SAO LUIZ DO PARAITINGA', 'SÃO LUIZ DO PARAITINGA'),
    ('SAO SEBASTIAO', 'SÃO SEBASTIÃO'),
    ('SILVEIRAS', 'SILVEIRAS'),
    ('TAUBATE', 'TAUBATÉ'),
    ('TREMEMBE', 'TREMEMBÉ'),
    ('UBATUBA', 'UBATUBA')
]

class Form_Busca(forms.Form):
    tipo_busca = forms.ChoiceField(choices=TIPOS_DE_BUSCA)
    node_start = forms.ChoiceField(choices=NOS_POSSIVEIS)
    node_end = forms.ChoiceField(choices=NOS_POSSIVEIS)
    limite_busca = forms.IntegerField(label="Limite(PL)/Limite Máximo(AI)", required=False)

    def __init__(self, *args, **kwargs):
        super(Form_Busca, self).__init__(*args, **kwargs)
        if 'tipo_busca' in self.data and self.data['tipo_busca'] == 'pl' or 'ai':
            self.fields['limite_busca'].required = True
        else:
            self.fields['limite_busca'].widget = forms.HiddenInput()