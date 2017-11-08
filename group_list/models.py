from django.db import models


class Group(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name='Название',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class GroupMate(models.Model):
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя',
        blank=True,
        null=True,
    )
    facebook_link = models.CharField(
        max_length=500,
        verbose_name='Ссылка на фейсбук',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учащийся'
        verbose_name_plural = 'Учащиеся'
