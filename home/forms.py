from dataclasses import fields
from django import forms
from home.models import Company, Job, InterviewExperience, Selection, StudentJob


class addCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('companyName', 'companyType',
                  'companyCategory', 'companyDesc')
        widgets = {
            'companyName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Title'}),
            'companyType': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Type'}),
            'companyName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Company Name'}),
            'companyDesc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class updateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('companyName', 'companyType',
                  'companyCategory', 'companyDesc')
        widgets = {
            'companyName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Title'}),
            'companyType': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Type'}),
            'companyName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Company Name'}),
            'companyDesc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Company Description'}),
        }



class jobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'role',
                  'description', 'ctc', 'profile', 'location', 'open', 'pr')
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Company'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Role'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Description'}),
            'ctc': forms.TextInput(attrs={'class': 'form-control', 'type': 'number','placeholder': 'Enter the Company Description'}),
            'profile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Profile'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Profile'}),
            'open': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Open for Courses'}),
            'pr': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assigned PR'}),
        }

class interviewExperience(forms.ModelForm):
    class Meta:
        model = InterviewExperience
        fields = ('user', 'company',
                  'jobProfile', 'experience')
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User Name'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Name'}),
            'jobProfile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Profile'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your interview experience here'}),
        }

class selection(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ('student', 'job')
        widgets = {
            'student': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job'}),
        }

class studentJob(forms.ModelForm):
    class Meta:
        model = StudentJob
        fields = ('student', 'job',
                  'verdict_choice', 'verdict')
        widgets = {
            'student': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job'}),
            'verdict_choice': forms.Select(attrs={'class': 'form-control'}),
            'verdict': forms.Select(attrs={'class': 'form-control'}),
        }        