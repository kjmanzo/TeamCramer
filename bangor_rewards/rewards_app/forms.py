from django import forms

# https://docs.djangoproject.com/en/1.10/topics/forms/
# read this ^

class FriendForm(forms.Form):
	friend_name = forms.CharField(label='add friend',max_length=100)