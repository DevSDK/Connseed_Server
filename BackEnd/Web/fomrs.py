from django import forms


class LoginForm(forms.Form):
    id = forms.CharField( max_length=255,  widget=forms.TextInput(attrs={'name':'user_id','id':'username', 'class':'form-control', 'placeholder' : 'Username'} ))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'name':'password','id':'password', 'class':'form-control', 'placeholder' : 'Password'}))
