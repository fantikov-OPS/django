from django.shortcuts import render

from app.forms import UserForm

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
            length, vowels, consonants = analyze_comment(comment)
            stats = {
                'length': length,
                'vowels': vowels,
                'consonants': consonants,
            }
    else:
        form = UserForm()

    return render(request, 'app/index.html', {
        'form': form,
        'stats': stats,
    })
