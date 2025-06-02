from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, PartnerPreference


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'religion', 'location', 'profession','mobile_no','profile_image']
        widgets = {
            'gender': forms.Select(),
            'religion': forms.Select(),
            'location': forms.Select(),
            'profession': forms.Select(),
        }


class PartnerPreferenceForm(forms.ModelForm):
    class Meta:
        model = PartnerPreference
        fields = ['min_age', 'max_age', 'preferred_religion', 'preferred_location', 'preferred_profession']
        widgets = {
            'preferred_religion': forms.Select(),
            'preferred_location': forms.Select(),
            'preferred_profession': forms.Select(),
        }

class SearchForm(forms.Form):
    min_age = forms.IntegerField(required=False, label='Min Age')
    max_age = forms.IntegerField(required=False, label='Max Age')
    religion = forms.ChoiceField(
        choices=[('', 'Any')] + list(UserProfile.RELIGION_CHOICES),
        required=False
    )
    location = forms.ChoiceField(
        choices=[('', 'Any')] + list(UserProfile.LOCATION_CHOICES),
        required=False
    )
    profession = forms.ChoiceField(
        choices=[('', 'Any')] + list(UserProfile.PROFESSION_CHOICES),
        required=False
    )
