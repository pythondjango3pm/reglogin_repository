from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='Enter First Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Enter Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class':'form-control'
            }
        )
    )
    username = forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'User Name',
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile Number',
                'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email',
                'class':'form-control'
            }
        )
    )



class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )





