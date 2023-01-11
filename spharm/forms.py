from django import forms
from .models import BePartner, Recomendations, Delivery, Pharmacies


class DocumentForm(forms.ModelForm):
    class Meta:
        model = BePartner
        fields = ('pharm_name', 'pharm_email', 'pharm_phone', 'document',)


class RecommendForm(forms.ModelForm):
    class Meta:
        model = Recomendations
        fields = ('username', 'user_email', 'user_phone', 'recommendations',)


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = (
            'person_name',
            'person_email',
            'person_tel',
            'person_city',
            'person_Address',
            'person_wish',
            'drug_name',)


class Del(forms.Form):
    person_name = forms.CharField(label="ФИО", widget=forms.TextInput(attrs={'placeholder': 'Search'}))


class SearchForm(forms.ModelForm):
    class Meta:
        model = Pharmacies
        fields = ['address', ]
