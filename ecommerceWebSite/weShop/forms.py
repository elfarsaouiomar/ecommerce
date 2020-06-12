from django import forms
from django.forms import ModelForm, Textarea
from .models import Country, Order

class ossrderForm(forms.Form):
    lName = forms.CharField(max_length=100, label='Last name :', required=True, widget=forms.TextInput(attrs={'class': "form-control"}), error_messages={'required': 'Please enter your name'})
    fName = forms.CharField(max_length=100, label='First name :',  required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    phone = forms.IntegerField(label='Phone :', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=70, label='Email :', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.ModelChoiceField(required=True, label='Contry :', queryset=Country.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=40, label='State :', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    codePostal = forms.CharField(max_length=40, label='Code Postal :', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(max_length=300, label='Note :', widget=forms.Textarea(attrs={"rows": 5, "cols": 30, "class": "form-control", "placeholder": "Write your notes here..."}))




class orderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ('lName', 'fName', 'phone', 'email', 'country', 'state', 'codePostal', 'note')

        widgets = {
            'lName': forms.TextInput(attrs={'class': "form-control"}),
            'fName': forms.TextInput(attrs={'class': "form-control"}),
            'phone': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'country': forms.Select(attrs={'class': "form-control"}),
            'state': forms.TextInput(attrs={'class': "form-control"}),
            'codePostal': forms.TextInput(attrs={'class': "form-control"}),
            'note': forms.Textarea(attrs={'class': "form-control", "rows": 5, "cols": 30, "placeholder": "Write your notes here..."}),
        }

        labels = {
            'lName': 'last name',
            'fName': 'first name',
            'phone': 'phone',
            'email': 'email',
            'country': 'country',
            'state': 'state',
            'codePostal': 'code Postal',
            'note': 'note',
        }

        error_messages = {
            'lName': {
                'max_length': "This last name is too long.",
                'required': 'Please enter your last name'
            },
            'fName': {
                'max_length': "This first name is too long.",
                'required': 'Please enter your fisrt name'
            },
            'phone': {
                'max_length': "This phone is too long.",
                'required': 'Please enter phone'
            },
            'email': {
                'max_length': "This writer's name is too long.",
                'required': 'Please enter your fisrt name'
            },
            'country': {
                'max_length': "This writer's name is too long.",
                'required': 'Please enter your fisrt name'
            },
            'state': {
                'max_length': "This writer's name is too long.",
                'required': 'Please enter your fisrt name'
            },
            'codePostal': {
                'max_length': "This writer's name is too long.",
                'required': 'Please enter your fisrt name'
            },
            'note': {
                'max_length': "This writer's name is too long.",
                'required': 'Please enter your fisrt name'
            }

        }


