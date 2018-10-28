from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from projeto import settings
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('projeto_id', 'autor', 'nomeprojeto', 'linguagem')

    projeto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    autor = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '120'}),
    )

    java = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    c = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    python = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    javascript = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    html = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    php = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    ruby = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    vb = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    sql = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )
    swift = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'maxlength': '120'}),
    )

    nomeprojeto = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '120'}),
    )