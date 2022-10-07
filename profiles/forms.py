from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # avatar = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('bio', 'avatar',)
