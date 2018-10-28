from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from projeto import settings
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    """class Meta:
        model = Projeto
        fields = ('projeto_id', 'autor', 'nomeprojeto', 'linguagem')"""

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    autor = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '120'}),
    )

    nomeprojeto = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '120'}),
    )