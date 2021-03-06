from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목:',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder': 'Enter the title',
            }),
        )
    content = forms.CharField(
        label='내용:',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content form-control',
                'placeholder' : 'Enter the content',
            })
        )
    
    class Meta:
        model=Article
        fields='__all__'
