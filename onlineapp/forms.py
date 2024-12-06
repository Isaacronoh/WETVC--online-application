from django import forms
from .models import Result,Application

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'marks']
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'