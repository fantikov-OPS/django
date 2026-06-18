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
