from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True)
    description = models.CharField(max_length=255, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True)
    video_link = models.URLField(verbose_name='ссылка на видео', null=True)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='lesson', verbose_name='курс')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    class PaymentMethods(models.TextChoices):
        CASH = 'CA', 'Cash'
        TRANSFER = 'TR', 'Transfer'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='payment', verbose_name='пользователь', null=True)
    paid_at = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, verbose_name='оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=2, choices=PaymentMethods.choices, default=PaymentMethods.CASH, verbose_name='способ оплаты')

    def __str__(self):
        return f'Дата платежа {self.paid_at}, размер платежа {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


