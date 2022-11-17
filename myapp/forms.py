from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # title = forms.CharField(
    #     label="Post Title",
    #     max_length=50,
    #     required=True)
    # description = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={"rows":6}
    #     )
    # )
    # created_date =  forms.DateTimeField()
    # attachment = forms.FileField()

    class Meta:
        model= Post
        fields="__all__"