from django import forms
from .models import Charity
from .models import User

# https://docs.djangoproject.com/en/1.10/topics/forms/
# read this ^

class FriendForm(forms.Form):
	friend_name = forms.CharField(label='add friend',max_length=100)
	friend_list = forms.CharField(label='friends list',widget=forms.Textarea(attrs={'id':'reasonTextBox'}))
