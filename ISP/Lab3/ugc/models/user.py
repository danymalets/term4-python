from django.db import models
from ugc.tgbot.state import State


class User(models.Model):
    chat_id = models.PositiveIntegerField(
        verbose_name="ID пользователя в тг",
        null=True,
    )
    name = models.CharField(
        max_length=32,
        verbose_name="Имя пользователя в тг",
        null=True,
        blank=True,
    )
    display_name = models.CharField(
        max_length=32,
        verbose_name="Отображаемое имя пользователя",
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        'Group',
        verbose_name="Группа",
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True,
    )
    tmp_queue = models.ForeignKey(
        'Queue',
        verbose_name="Текушая очередь",
        on_delete=models.CASCADE,
        related_name="users0",
        null=True,
        blank=True,
    )
    state = models.CharField(
        verbose_name="Текущее состояние чата",
        max_length=30,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
