from django import forms


class NameForm(forms.Form):
    name = forms.CharField(
        label = 'Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Введите имя'})
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
