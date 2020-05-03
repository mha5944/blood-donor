from django import forms
from basicapp.models import UserProfile
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


BLOOD_TYPES = [
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
]
CASE = [
    ('Reciver','Reciver'),
    ('Blood Donor','Blood Donor'),
]

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'password','first_name', 'last_name',)
        labels = {
            'username':'',
            'email':'',
            'password':'',
            'first_name':'',
            'last_name':'',
        }
        help_texts = {
            'username':'',  
        }
        widgets = {
           'username': forms.TextInput(attrs={'placeholder':'  Username'}),
           'email': forms.TextInput(attrs={'placeholder':'  Email'}),
           'password': forms.PasswordInput(attrs={'placeholder':'  Password'}),
           'first_name': forms.TextInput(attrs={'placeholder':'  First name'}),
           'last_name': forms.TextInput(attrs={'placeholder':'  Last name'}),
        }


class UserProfileForm(forms.ModelForm):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(
            validators=[phone_regex], max_length=17,
            widget=forms.TextInput(attrs={'placeholder':'  Phone number',})
            )

    class Meta():
        model = UserProfile
        fields = ('case', 'blood_type', 'phone_number','description')

        labels = {
            'description': '',
            'case':'',
            'blood_type':'',
            'phone_number':'',
        }
        widgets = {
            'blood_type': forms.Select(choices=BLOOD_TYPES),
            'case': forms.Select(choices=CASE),
            'description': forms.Textarea(attrs={'class':'customtext', 'placeholder':' Please write your ilness...'}),
        }