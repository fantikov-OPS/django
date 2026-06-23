from django.contrib import admin

from app.models import Customer, Group, Student, Person, PersonGroup


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'profession')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'group')
    list_filter = ('group',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')

@admin.register(PersonGroup)
class PersonGroupAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'size', 'start_date', 'finish_date')