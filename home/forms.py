from dataclasses import fields
from django import forms
from home.models import Company, Job, InterviewExperience, Selection, StudentJob


class addCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("companyName", "companyType", "companyCategory", "companyDesc")
        widgets = {
            "companyName": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter the Title"}
            ),
            "companyType": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Company Type"}
            ),
            "companyName": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter the Company Name"}
            ),
            "companyDesc": forms.TextInput(attrs={"class": "form-control"}),
        }


class updateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("companyName", "companyType", "companyCategory", "companyDesc")
        widgets = {
            "companyName": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter the Title"}
            ),
            "companyType": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Company Type"}
            ),
            "companyName": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter the Company Name"}
            ),
            "companyDesc": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the Company Description",
                }
            ),
        }


companies = Company.objects.all().values_list("companyName", "companyName")
com_choices_list = []
for item in companies:
    com_choices_list.append(item)


class addJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            "company",
            "role",
            "description",
            "ctc",
            "profile",
            "location",
            "deadline",
            "opens",
        )
        print(com_choices_list)
        widgets = {
            "company": forms.Select(
                choices=com_choices_list, attrs={"class": "form-control"}
            ),
            "role": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Role"}
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Job Description"}
            ),
            "ctc": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "number",
                    "placeholder": "Enter the Company CTC",
                }
            ),
            "profile": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Job Profile"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Job Locations"}
            ),
            "deadline": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "opens": forms.Select(choices=(("True", "True"), ("False", "False"))),
        }


class addInterviewExperienceForm(forms.ModelForm):
    class Meta:
        model = InterviewExperience
        fields = ("user", "company", "jobProfile", "experience")
        widgets = {
            "user": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "user_id",
                    "type": "hidden",
                }
            ),
            "company": forms.Select(
                choices=com_choices_list, attrs={"class": "form-control"}
            ),
            "jobProfile": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Job Profile"}
            ),
            "experience": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your interview experience here",
                }
            ),
        }

        def get_object(self):
            return self.request.user


class selection(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ("student", "job")
        widgets = {
            "student": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Student Name"}
            ),
            "job": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Job"}
            ),
        }


class studentJob(forms.ModelForm):
    class Meta:
        model = StudentJob
        fields = ("student", "job", "verdict")
        widgets = {
            "student": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Student Name"}
            ),
            "job": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Job"}
            ),
            "verdict": forms.Select(attrs={"class": "form-control"}),
        }
