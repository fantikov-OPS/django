from django import forms

from app.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'age', 'profession']


class NameForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
    )


class ProfileForm(forms.Form):
    firstname = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
    )
    lastname = forms.CharField(
        label='Фамилия',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
    )
    age = forms.IntegerField(
        label='Возраст',
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Введите возраст'}),
    )
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(attrs={'placeholder': 'Введите комментарий', 'rows': 4}),
    )


class UserForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
    )
    surname = forms.CharField(
        label='Фамилия',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
    )
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(attrs={'placeholder': 'Введите комментарий', 'rows': 4}),
    )
