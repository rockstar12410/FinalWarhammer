from django import forms
from .models import usedBuy

class usedForm(forms.ModelForm):
    class Meta:
        model = usedBuy
        fields = ['product', 'description', 'price','condition', 'seller', 'email', 'phone']