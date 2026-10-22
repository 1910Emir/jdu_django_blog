from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields ro'yxatiga 'image' qo'shildi:
        fields = ['title', 'category', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post sarlavhasi'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Post matni'}),
            # Rasm tanlash inputi uchun widget (ixtiyoriy, chiroyli ko'rinishi uchun):
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['category'].required = True
        self.fields['content'].required = True
        # Rasm har doim ham shart bo'lmasligi uchun required=False qilib qo'yamiz:
        self.fields['image'].required = False