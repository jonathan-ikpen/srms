from django import forms
from django.contrib.auth.models import User
from .models import Student, Department, Faculty


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    matric_no = forms.CharField(max_length=20, required=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    # Additional fields from the Student model
    surname = forms.CharField(max_length=100, required=True)
    other_names = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=100, required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=True)
    nationality = forms.CharField(max_length=100, required=True)
    state_of_origin = forms.CharField(max_length=100, required=True)
    local_government_area = forms.CharField(max_length=100, required=True)
    home_address = forms.CharField(widget=forms.TextInput, required=True)
    marital_status = forms.CharField(max_length=100, required=True)

    # Academic Information
    hall_of_residence = forms.ChoiceField(choices=Student.HALL_CHOICES, required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=True)
    faculty = forms.ModelChoiceField(queryset=Faculty.objects.all(), required=False)
    level = forms.ChoiceField(choices=Student.LEVEL_CHOICES, required=True)
    study_mode = forms.ChoiceField(choices=Student.STUDY_MODE_CHOICES, required=True)
    profile_picture = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'matric_no', 'email', 'password', 'confirm_password', 'surname', 'other_names', 'phone_number', 'date_of_birth', 'gender', 'nationality', 'state_of_origin', 'local_government_area', 'home_address','marital_status', 'profile_picture', 'hall_of_residence', 'department', 'faculty', 'level', 'study_mode']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data