from django.db import models

from users.models import User


class Bread(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название породы', help_text='Введите название породы')
    description = models.TextField(verbose_name='Описание порода', help_text='Введите описание породы', blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кличка', help_text='Введите кличку')
    description = models.TextField(verbose_name='Описание собаки', help_text='Введите описание собаки', blank=True,
                                   null=True)
    bread = models.ForeignKey(Bread, on_delete=models.SET_NULL, verbose_name='Порода', help_text='Введите породу',
                              blank=True,
                              null=True, related_name='dogs')
    photo = models.ImageField(upload_to='dogs/photo', blank=True, null=True, verbose_name='Фото',
                              help_text='Вставьте фото')
    date_born = models.DateField(blank=True, null=True, verbose_name='Дата рождения',
                                 help_text='Укажите дату рождения')

    view_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите колличество просмотров',
        default=0
    )
    owner = models.ForeignKey(User, verbose_name='Владелец', help_text='Укажите владельца', blank=True, null=True,
                              on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ['bread', 'name']
        permissions = [
            ("can_edit_bread", "Can edit bread"),
            ("can_edit_description", "Can edit description"),
        ]

    def __str__(self):
        return self.name


class Parent(models.Model):
    dog = models.ForeignKey(Dog, related_name='parents', on_delete=models.SET_NULL, null=True, blank=True,
                            verbose_name='Собака', )
    name = models.CharField(max_length=100, verbose_name='Кличка', help_text='Введите кличку', )
    bread = models.ForeignKey(Bread, on_delete=models.SET_NULL, verbose_name='Порода', help_text='Введите породу',
                              blank=True,
                              null=True, related_name='parentsdogs', )
    date_born = models.PositiveIntegerField(blank=True, null=True, verbose_name='Дата рождения',
                                            help_text='Укажите дату рождения', default=0, )

    class Meta:
        verbose_name = 'Собака родитель'
        verbose_name_plural = 'Собаки родители'
        ordering = ['bread', 'name']

    def __str__(self):
        return self.name
