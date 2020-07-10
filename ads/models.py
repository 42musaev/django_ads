from django.db import models


class Applications(models.Model):
    user_name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Номер', max_length=15)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class DealType(models.Model):
    name = models.CharField('Тип сделки', max_length=255, unique=True)

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


class HousingType(models.Model):
    name = models.CharField('Тип жилья', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип жилья'
        verbose_name_plural = 'Тип жилья'


class ProperType(models.Model):
    name = models.CharField('Тип недвижимости', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Тип недвижимости'


class Finishing(models.Model):
    name = models.CharField('Отделка', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделка'
        verbose_name_plural = 'Отделки'


class Ads(models.Model):
    image = models.ImageField('Главная фотография', upload_to='apartments')
    deal_type = models.ForeignKey(
        'DealType',
        verbose_name='Типы сделки',
        on_delete=models.CASCADE,
        related_name='deal_type'
    )
    housing_type = models.ForeignKey(
        'HousingType',
        on_delete=models.CASCADE,
        verbose_name='Тип жилья'
    )
    proper_type = models.ForeignKey(
        'ProperType',
        verbose_name='Тип недвижимости',
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
    finishing = models.ForeignKey(
        'Finishing',
        verbose_name='Отделка',
        on_delete=models.CASCADE,
    )
    address = models.CharField('Адрес', max_length=255)
    price_sm = models.DecimalField(
        'Цена за квадратный метр',
        max_digits=14,
        decimal_places=2,
    )
    price = models.DecimalField(
        'Цена',
        max_digits=14,
        decimal_places=2,
    )
    phone = models.CharField(
        "Номер",
        help_text="Введите номер в формате: 8 (999) 999 99 99",
        max_length=15
    )
    special_offer = models.BooleanField('Предложение дня', default=False)

    class Meta:
        verbose_name = 'Обявление'
        verbose_name_plural = 'Объявления'
