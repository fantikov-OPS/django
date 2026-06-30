from copy import deepcopy
import string
from typing import Any
import functools
from collections.abc import Callable
from typing import TypeVar
from dataclasses import dataclass
import sys

a = [1,2,3,4]
b=deepcopy(a)
F = TypeVar("F",  bound=Callable)

c = a
#print(id(a))
#print(id(b))
#print(id(c))

def log_calls(func: F):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} args={args}, kwargs= {kwargs} -> result {result}')
        return result
    return wrapper

def calc_average(numbers):
  total = 0
  for i in numbers:
    total += i
  return total / len(numbers)

#data = input("Введите числа через пробел: ")
#nums = [float(x) for x in data.split()]
#nums = data.split()
#print(f"Среднее: {calc_average(nums)}")


def even_squares(n: int) -> list[int]:
    return [x**2 for x in range(n) if x % 2 ==0]


def count_words(words: list[str]):
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def unique_preserve_order(items: list):
    seen: set = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def analize_text(text: str):
    puct = string.punctuation
    raw_words = text.split()
    words = [w.strip(puct).lower() for w in raw_words if w.strip(puct)]
    word_freq: dict[str, int] = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return {
        'words': len(words),
        'unique_words':len(word_freq),
        'longest_word': max(words, key=len) if words else "",
        'word_freq':word_freq,
    }


def is_prime(n:int):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main_primes():
    while True:
        raw = input('Введите число N: ')
        try:
            n = int(raw)
        except ValueError:
            print('Введите целое число >=2')
            continue
        if n < 2:
            print('Введите целое число >=2')
            continue
        break
    primes = [x for x in range(2, n + 1) if is_prime(x)]
    print(primes)
    print(sum(primes))


def summarize_actions(actions: list[tuple[str, str]]):
    unique_user: set[str] = set()
    action_count: dict[str, int] = {}
    user_purchases: dict[str, int] = {}
    
    for user, action in actions:
        unique_user.add(user)
        action_count[action] = action_count.get(action, 0) + 1
        if user not in user_purchases:
            user_purchases[user] = 0
        if action == 'purchase':
            user_purchases[user] += 1
    return {
        "unique_user" : unique_user,
        "action_count" : action_count,
        "user_purchases" : user_purchases,
    }

@log_calls
def format_report(student: dict):
    name = student['name']
    group = student['group']
    avg = sum(student["grades"]) / len(student["grades"])
    
    line_percent = 'Студент: %s, группа: %s, средний балл: %.2f' % (name, group, avg)
    line_format = 'Студент: {}, группа: {}, средний балл: {:.2f}'.format(name, group, avg)
    line_fstring = f'Студент: {name}, группа: {group}, средний балл: {avg:.2f}'
    return [ line_format, line_fstring, line_percent]


def flatten(data: list, *, depth: int = -1):
    if depth == 0:
        return list(data)
    result: list[Any] = []
    for item in data:
        if isinstance(item, list) and depth != 0:
            next_depth = depth - 1 if depth > 0 else -1
            result.extend(flatten(item, depth=next_depth))
        else:
            result.append(item)
    return result


def apply_operations(*args:float, **kwargs:bool):
    numbers = list(args)
    if not numbers:
        return {}
    
    result: dict[str, float] = {}
    if kwargs.get('sum'):
        result['sum'] = sum(numbers)
    if kwargs.get('max'):
        result['max'] = max(numbers)
    if kwargs.get('min'):
        result['min'] = min(numbers)
    if kwargs.get('avg'):
        result['avg']= sum(numbers) / len(numbers)
    return result


def make_multiplier(factor:float):
    def multiple(x:float):
        return x*factor
    return multiple


class ItemNotFoundError(Exception):
    def __init__(self, title):
        super().__init__(f'Item not found {title}')
        self.title = title


@dataclass
class BorrowRecord:
    title: str
    borrower: str
    due_date: str

class Item:

    def __init__(self, title:str):
        self.__title = title
    
    @property
    def title(self):
        return self.__title
    
    def __str__(self):
        return self.__title

    def __repr__(self):
        return f'{self.__class__.__name__} title {self.__title}'


class Book(Item):

    def __init__(self, title, *, author, isbn):
        super().__init__(title)
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f'Book {self.__title} author {self.author}'

    def __repr__(self):
        return f'Book {self.__title} author {self.author} isbn {self.isbn}'


class DVD(Item):
    def __init__(self, title, *, duration_minutes, rating):
        super().__init__(title)
        self.duration_minutes = duration_minutes
        self.rating = rating

    def __str__(self):
        return f'DVD {self.__title} {self.duration_minutes} min'

    def __repr__(self):
        return f'DVD {self.__title} {self.duration_minutes} min rating {self.rating}'

class Library:
    def __init__(self):
        self._items: list[Item] = []

    def add(self, item):
        self._items.append(item)
        
    def find_by_title(self, title):
        for item in self._items:
            if item.title == title:
                return item
        return None

    def checkout(self, title):
        item = self.find_by_title(title)
        if item is None:
            raise ItemNotFoundError(title)
        self._items.remove(item)
        return item

def fibonacci(n:int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class Countdown:
    
    def __init__(self, start:int):
        self._current = start


    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current < 1:
            raise StopIteration
        value = self._current
        self._current -=1
        return value

class Vector2D:

    def __init__(self, x: float , y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector2D ({self.x}, {self.y})' 


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError as exc:
        raise ValueError('Аргументы должны быть числами')


def read_numbers_from_file(path: str):
    numbers: list[float] = []
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    numbers.append(float(stripped))
                except ValueError:
                    print(f'пропущена строка {stripped}')
    except OSError as e:
        print('Ошибка чтения файла')
    finally:
        print('Ok')
    return numbers
                 
import json
                    
def save_student_json(students, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def load_students_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)
    
import csv
def save_sudents_cvs(students, path):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'group', 'grade'])
        writer.writeheader()
        writer.writerows(students)

import os
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return os.path.abspath(path)

import re
PHONE_PATTERN = re.compile(r"\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}")
EMAIL_PATTERN = re.compile(f"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+$")


def extract_phones(text):
    return PHONE_PATTERN.findall(text)

def validation_email(email):
    return bool(EMAIL_PATTERN.match(email))




#SELECT p.name, p.price from products p 
#join categories c on p.category_id = c.id 
#where c.name = 'Электроника' and p.price  > 5000

#select u.email from "users" u 
#join orders o on o.user_id u.id 
#where o.status = 'completed'
#roup BY u.id, u.email 
#HAVING coount(o.id) > 3

#select p.name , sum(oi.quantity ) as total_solid
#from products p 
#join order_items oi on oi.product_id = p.id 
#group by p.id, p.name 
#order by total_solid DESC
#LIMIT 5

#select p.name
#from products p 
#left join order_items oi on oi.product_id = p.id 
#WHERE oi.id is null

if __name__ == '__main__':
    #print(even_squares(6))
    #print(count_words(["a", "b", "a", "c", "b", "a"]))
    #print(unique_preserve_order([3, 1, 2, 1, 3, 2]))
    #print(analize_text("Helloo hello world! World."))
    #main_primes()
    #actions = [
  #("alice", "login"), ("bob", "login"), ("alice", "purchase"),
  #("bob", "logout"), ("alice", "purchase"), ("charlie", "login"),
  #("alice", "logout"), ("bob", "login"),
#]
    #print(summarize_actions(actions))
    #student = {"name": "Иван", "group": "ПИ-21", "grades": [4, 5, 3, 5]}
    #print(format_report(student))
    #print(flatten([1, [2, 3], [[4], 5]]))
    #print(apply_operations(1, 2, 3, 4, sum=True, max=True, avg=True))
    #products = [
  #{"name": "Ноутбук", "price": 75000, "category": "electronics"},
  #{"name": "Книга", "price": 500, "category": "books"},
  #{"name": "Наушники", "price": 3000, "category": "electronics"},
  #{"name": "Ручка", "price": 50, "category": "office"},
  #{"name": "Монитор", "price": 15000, "category": "electronics"},
#]
   # electronics_names = [p['name'] for p in products if p['category'] == 'electronics']
   # expensive = {p['name']: p['price'] for p in products if p['price'] > 1000}
   # electronics_prices = [p['price'] for p in products if p['category'] == 'electronics']
   # avg_electronics = sum(electronics_prices) / len(electronics_prices)
   # print(electronics_names)
  #  print(expensive)
   # print(avg_electronics)
   # double = make_multiplier(2)
   # print(double(5))   # 10
   # triple = make_multiplier(3)
    #print(triple(4))   # 12
    #lib = Library()
    #lib.add(Book("1984", author="Orwell", isbn="978-0-452-28423-4"))
    #lib.add(DVD("Matrix", duration_minutes=136, rating=8.7))
    #lib.checkout("1984")          # возвращает Book, в библиотеке его больше нет
    #lib.checkout("Несуществующая")  # ItemNotFoundError
    #print(extract_phones("Звоните: +7 (999) 123-45-67"))
    print(validation_email("user@mlocalhost"))

