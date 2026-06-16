from django import forms


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
    age = forms.IntegerField(
        label='Возраст',
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Введите возраст'}),
    )
