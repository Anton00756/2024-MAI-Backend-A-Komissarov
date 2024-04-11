from django.db import models


class Course(models.Model):
    uid = models.UUIDField(verbose_name='ID курса')
    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    paid = models.BooleanField(verbose_name='Платный курс')

    def __str__(self):
        return f'{self.name} [{self.uid}]'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    uid = models.UUIDField(verbose_name='ID занятия')
    theme = models.CharField(max_length=150, verbose_name='Тема занятия')
    material = models.TextField(verbose_name='Материал занятия')
    time = models.IntegerField(verbose_name='Продолжительность занятия (мин)')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.theme} [{self.uid}]'

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
