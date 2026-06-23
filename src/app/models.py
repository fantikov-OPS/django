from django.db import models


class Customer(models.Model):
    firstname = models.CharField('Имя', max_length=255)
    lastname = models.CharField('Фамилия', max_length=255)
    age = models.PositiveIntegerField('Возраст')
    profession = models.CharField('Профессия', max_length=255)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Group(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname = models.CharField('Имя', max_length=255)
    lastname = models.CharField('Фамилия', max_length=255)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='Группа',
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Diary(models.Model):
    average_score = models.DecimalField('Средний балл', max_digits=4, decimal_places=2)
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='diary',
        verbose_name='Студент',
    )

    class Meta:
        verbose_name = 'Школьный дневник'
        verbose_name_plural = 'Школьные дневники'

    def __str__(self):
        return f'Дневник {self.student}'


class Book(models.Model):
    title = models.CharField('Название', max_length=255)
    pages = models.PositiveIntegerField('Количество страниц')
    students = models.ManyToManyField(
        Student,
        related_name='books',
        blank=True,
        verbose_name='Студенты',
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество')
    comment = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    group = models.ForeignKey('PersonGroup', null=True, on_delete=models.SET_NULL, related_name='pesons')
    hobbies = models.ManyToManyField('Hobbies', related_name='persons')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class PersonGroup(models.Model):
    serial_number = models.CharField(max_length=4, default=None)
    size = models.PositiveSmallIntegerField()
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=False)

    class Meta:
        verbose_name = 'Группа пользователя'
        verbose_name_plural = 'Группы пользователя'
        
        
class ContactInfo(models.Model):
   phone = models.CharField(max_length=50, null=True, default=None)
   address = models.CharField(max_length=50, null=True, default=None)


class ContactPerson(models.Model):
   firstname = models.CharField(max_length=255, default=None)
   lastname = models.CharField(max_length=255, default=None)
   age = models.IntegerField()
   profession = models.CharField(max_length=255, default=None)
   contact_info = models.OneToOneField(
       ContactInfo, null=True,
       related_name='contactperson',
       on_delete=models.SET_NULL,
   )

class Hobbies(models.Model):
   name = models.CharField(max_length=255, default=None)