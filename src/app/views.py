from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from app.forms import UserForm, NameForm, ProfileForm, CustomerForm
from app.models import Customer, Comment
from app.serializers import CommentSerializer

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


def profile_form(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(f"{data['firstname']}|{data['lastname']}|{data['age']}|{data['comment']}")
            form = ProfileForm()
    else:
        form = ProfileForm()

    return render(request, 'app/profile_form.html', {'form': form})


def customers(request):
    if Customer.objects.count() == 0:
        Customer.objects.bulk_create([
            Customer(firstname='Alex', lastname='Smith', age=30, profession='Engineer'),
            Customer(firstname='Alex', lastname='Johnson', age=25, profession='Designer'),
            Customer(firstname='Maria', lastname='Brown', age=28, profession='Doctor'),
        ])

    alex_users = Customer.objects.filter(firstname='Alex')
    user_by_id = Customer.objects.get(id=1)

    return render(request, 'app/customers.html', {
        'alex_users': alex_users,
        'user_by_id': user_by_id,
    })


def home(request):
    customers = Customer.objects.all()
    return render(request, 'app/home.html', {'customers': customers})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()

    return render(request, 'app/add_customer.html', {'form': form})

def api_comments(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many = True)
        return JsonResponse(serializer.data, safe=False)