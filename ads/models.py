from django.db import models
from phone_field import PhoneField


class DealType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип сделки'
        verbose_name_plural = 'Тип сделки'


class District(models.Model):
    name = models.CharField('Район', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Ads(models.Model):
    deal_type = models.ForeignKey(
        'DealType',
        verbose_name='Тип сделки',
        on_delete=models.CASCADE,
    )
    number_of_rooms = models.IntegerField('Количество комнат', default=1)
    apartment_area = models.IntegerField(
        'Площадь квартиры',
        help_text='Укажите без знака квадрата.'
    )
    house_floor = models.IntegerField(
        'Этажи дома',
        help_text='Укажите этажность дома',
    )
    apartment_floor = models.IntegerField('На каком этаже квартира')
    district = models.ForeignKey(
        'District',
        on_delete=models.CASCADE,
        verbose_name='Район',
    )
    address = models.CharField('Адрес', max_length=255)
    price_sm = models.DecimalField(
        'Цена за квадратный метр',
        max_digits=8,
        decimal_places=2,
    )
    price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=2,
    )
    phone = PhoneField("Номер", blank=True, help_text='Код-номер')
    special_offer = models.BooleanField('Предложение дня', default=False)

    class Meta:
        verbose_name = 'Обявление'
        verbose_name_plural = 'Объявления'
