from django import forms
from home.models import Company, Job, InterviewExperience, Selection, StudentJob
class addCompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=('companyName','companyType', 'companyCategory','companyDesc')
        widgets={
            'companyName': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title'}),
            'companyType': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Company Type'}),
            'companyName': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Company Name'}),
            'companyDesc': forms.TextInput(attrs={'class':'form-control'}),
        }
class updateCompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=('companyName','companyType', 'companyCategory','companyDesc')
        widgets={
            'companyName': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Title'}),
            'companyType': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Company Type'}),
            'companyName': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Company Name'}),
            'companyDesc': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the Company Description'}),
        }
