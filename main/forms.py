from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import  User
class signUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'image')



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )


   


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'is_customer', 'is_employee', 'is_admin', 'image')
        widgets = {
            'password': forms.PasswordInput(),
        }
    

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_admin', 'is_customer', 'is_employee', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'autocomplete': 'new-password'})

class UserFormUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'image']
 




class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)

# class FoodmenuForm(forms.ModelForm):
#     class Meta:
#         model = FoodItem
#         fields = ['category','name', 'price', 'description','available']      
