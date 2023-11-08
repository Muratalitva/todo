from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    status = models.BooleanField(
        default = False
    )
    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задание"