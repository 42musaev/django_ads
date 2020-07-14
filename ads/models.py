from django.db import models
from django.urls import reverse


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


class Repair(models.Model):
    name = models.CharField('Ремонт', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонт'


class Bathroom(models.Model):
    name = models.CharField('Санузел', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Санузел'
        verbose_name_plural = 'Санузел'


class Balcony(models.Model):
    name = models.CharField('Балкон', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Балкон'
        verbose_name_plural = 'Балконы'


class SunnySide(models.Model):
    name = models.CharField(
        'Солнечная сторона',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Солнечная сторона'
        verbose_name = 'Солнечная сторона'


class ViewFromWindows(models.Model):
    name = models.CharField(
        'Вид из окна',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид из окна'
        verbose_name_plural = 'Виды из окон'


class Door(models.Model):
    name = models.CharField('Дверь', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'


class ConnectedServices(models.Model):
    name = models.CharField('Сервисы', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сервисы'
        verbose_name_plural = 'Сервисы'


class Yard(models.Model):
    name = models.CharField('Двор', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Двор'
        verbose_name_plural = 'Дворы'


class WindowMaterial(models.Model):
    name = models.CharField('Материал окон', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Матертал окна'
        verbose_name_plural = 'Матерталы окон'


class Parking(models.Model):
    name = models.CharField('Паркинг', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Паркинг'
        verbose_name_plural = 'Паркинги'


class Series(models.Model):
    name = models.CharField('Серия', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'


class YearConstruction(models.Model):
    name = models.CharField('Год постройки', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Год постройки'
        verbose_name_plural = 'Год постройки'


class Walls(models.Model):
    name = models.CharField('Стены', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стены'
        verbose_name_plural = 'Стены'


class Elevator(models.Model):
    name = models.CharField('Лифт', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лифт'
        verbose_name_plural = 'Лифт'


class HouseNumber(models.Model):
    name = models.CharField('Номер дома', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номер дома'
        verbose_name_plural = 'Номера домов'


class Ads(models.Model):
    image = models.ImageField('Главная фотография', blank=True)
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
    number_of_rooms = models.IntegerField(
        'Количество комнат',
        default=1
    )
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
    height_of_ceilings = models.DecimalField(
        'Высота потолков',
        max_digits=3,
        decimal_places=2,
        help_text="Укажите просто цифры, пример: \"2.5\""
    )
    repair = models.ForeignKey(
        'Repair',
        on_delete=models.CASCADE,
        verbose_name='Ремонт',
    )
    bathroom = models.ForeignKey(
        'Bathroom',
        on_delete=models.CASCADE,
        verbose_name="Санузел",
    )
    balcony = models.ForeignKey(
        'Balcony',
        on_delete=models.CASCADE,
        verbose_name='Балкон',
    )
    sunny_side = models.ForeignKey(
        'SunnySide',
        on_delete=models.CASCADE,
        verbose_name='Солнечная сторона',
    )
    view_from_windows = models.ForeignKey(
        'ViewFromWindows',
        on_delete=models.CASCADE,
        verbose_name='Вид из окон',
    )
    door = models.ForeignKey(
        'Door',
        on_delete=models.CASCADE,
        verbose_name='Дверь',
    )
    window_material = models.ForeignKey(
        'WindowMaterial',
        on_delete=models.CASCADE,
        verbose_name='Материал окна',
    )
    connected_services = models.ManyToManyField(
        'ConnectedServices',
        verbose_name='Подлкюченные сервисы',
    )
    yard = models.ForeignKey(
        'Yard',
        on_delete=models.CASCADE,
        verbose_name='Двор',
    )
    parking = models.ForeignKey(
        'Parking',
        on_delete=models.CASCADE,
        verbose_name='Паркинг'
    )
    series = models.ForeignKey(
        'Series',
        on_delete=models.CASCADE,
        verbose_name='Серия',
        default='1',
    )
    year_construction = models.ForeignKey(
        'YearConstruction',
        on_delete=models.CASCADE,
        verbose_name='Год постройки',
        default="2020",
    )
    walls = models.ForeignKey(
        'Walls',
        on_delete=models.CASCADE,
        verbose_name='Сетны',
    )
    elevator = models.ForeignKey(
        'Elevator',
        on_delete=models.CASCADE,
        verbose_name='Лифт',
    )
    house_number = models.ForeignKey(
        'HouseNumber',
        on_delete=models.CASCADE,
        verbose_name='Номер дома',
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
        max_length=20
    )
    description = models.TextField(verbose_name="Описание", max_length=5000)
    special_offer = models.BooleanField('Предложение дня', default=False)

    def get_absolute_url(self):
        return reverse('ads_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Обявление'
        verbose_name_plural = 'Объявления'
