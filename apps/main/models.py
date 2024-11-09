from django.db import models

# Create your models here.
class NewsKg(models.Model):
    title=models.TextField(verbose_name="заголовок")
    description=models.TextField(verbose_name="описание")
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'