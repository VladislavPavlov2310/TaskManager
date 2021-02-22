from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    reminder = models.DateTimeField('Напоминание', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_details', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
