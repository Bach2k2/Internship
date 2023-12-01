from django import forms
from .models import Novel,Category

class NovelForm(forms.Form):
    title = forms.CharField(max_length=200)
    published_date = forms.DateTimeField(label="Date Published",widget=forms.DateInput(attrs={'type': 'date'})) # dung widget de tao form
    year = forms.IntegerField(initial=0)
    status = forms.BooleanField(initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.values_list('name', flat=True), empty_label="Select a category")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")