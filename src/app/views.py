from django.shortcuts import render

from app.forms import UserForm


def index(request):
    message = None

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            message = 'В доступе отказано' if age < 18 else 'Добро пожаловать'
    else:
        form = UserForm()

    return render(request, 'app/index.html', {
        'form': form,
        'message': message,
    })
