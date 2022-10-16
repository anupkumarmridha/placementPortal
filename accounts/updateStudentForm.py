from dataclasses import fields
from django import forms
from accounts.models import Student


class updateStudentDetails(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "user",
            "phone",
            "personalEmail",
            "gender",
            # "profile_pic",
            "dob",
            "homeAddress",
            "localAddress",
            "jobType",
            "fatherName",
            "motherName",
            "guardianPhone",
            "degreeLevel",
            "currentDept",
            "currentCourse",
            "currentCgpa",
            "currentCourseGraduationYear",
            "class10Percentage",
            "class12Percentage",
            "ugDegree",
            "ugCgpa",
            "ugCollege",
            "ugGraduationYear",
        )
        widgets = {
            "phone": forms.NumberInput(),
            "personalEmail": forms.EmailInput(attrs={"class": "form-control"}),
            "gender": forms.TextInput(attrs={"class": "form-control"}),
            "profile_pic": forms.FileInput(attrs={"class": "rounded_list"}),
            "dob": forms.DateInput(attrs={"class": "form-control"}),
            "homeAddress": forms.TextInput(attrs={"class": "form-control"}),
            "localAddress": forms.TextInput(attrs={"class": "form-control"}),
            "jobType": forms.Select(attrs={"class": "form-control"}),
            "fatherName": forms.TextInput(attrs={"class": "form-control"}),
            "motherName": forms.TextInput(attrs={"class": "form-control"}),
            "guardianPhone": forms.NumberInput(),
            "degreeLevel": forms.Select(attrs={"class": "form-control"}),
            "currentDept": forms.TextInput(attrs={"class": "form-control"}),
            "currentCourse": forms.TextInput(attrs={"class": "form-control"}),
            "currentCgpa": forms.TextInput(attrs={"class": "form-control"}),
            "currentCourseGraduationYear": forms.DateInput(
                attrs={"class": "form-control"}
            ),
            "class10Percentage": forms.TextInput(attrs={"class": "form-control"}),
            "class12Percentage": forms.TextInput(attrs={"class": "form-control"}),
            "ugDegree": forms.TextInput(attrs={"class": "form-control"}),
            "ugCgpa": forms.TextInput(attrs={"class": "form-control"}),
            "ugCollege": forms.TextInput(attrs={"class": "form-control"}),
            "ugGraduationYear": forms.DateInput(attrs={"class": "form-control"}),
        }
