from django.contrib import admin

from app.models import Customer, Group, Student, Diary, Book, Person, PersonGroup, ContactInfo, ContactPerson


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


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('student', 'average_score')
    list_filter = ('student__group',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pages')
    filter_horizontal = ('students',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')

@admin.register(PersonGroup)
class PersonGroupAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'size', 'start_date', 'finish_date')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address')

@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'profession', 'contact_info')