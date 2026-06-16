from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from app.forms import UserForm, NameForm

VOWELS = set('аеёиоуыэюяaeiouy')


def analyze_comment(comment):
    vowels = consonants = 0
    for char in comment.lower():
        if char in VOWELS:
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return len(comment), vowels, consonants


def index(request):
    stats = None

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            name = form.cleaned_data['name']
            length, vowels, consonants = analyze_comment(comment)
            formated_lines = [f"{line} (c) {name}" for line in comment.splitlines()]
            stats = {
                'length': length,
                'vowels': vowels,
                'consonants': consonants,
                'formated_lines': formated_lines,
            }
    else:
        form = UserForm()

    return render(request, 'app/index.html', {
        'form': form,
        'stats': stats,
    })


def name_form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'app/name_display.html', {'name':form.cleaned_data['name']})
    else:
        form = NameForm()
    return render(request, 'app/name_from.html', {'form': form})


def greet(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            template = loader.get_template('app/greet.html')
            html = template.render({'name': form.cleaned_data['name']}, request)
            return HttpResponse(html)
    else:
        form = NameForm()
    
    template = loader.get_template('app/greet_form.html')
    html = template.render({'form': form}, request)
    return HttpResponse(html)