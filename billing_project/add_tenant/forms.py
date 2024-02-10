from django import forms
from .models import Contract

class CreateClientForm(forms.ModelForm):
    client = forms.HiddenInput()
    class Meta:
        model = Contract
        fields = ['shopping_complex', 'contract_num', 'start_date', 'finish_date', 'contract_date', 'contract_type', 'advertising_tax', 'is_closed', 'at_work', 'comment', 'invoice_num', 'basic_contract', 'basic_lot']
        widgets = {
            'shopping_complex': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'start_date': forms.SelectDateWidget(),
            'finish_date': forms.SelectDateWidget(),
            'contract_date': forms.SelectDateWidget(),
            'contract_num': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'invoice_num': forms.TextInput(attrs={'class': 'form-control'}),
            'basic_contract': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'basic_lot': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['basic_contract'].required = False
        self.fields['basic_lot'].required = False
