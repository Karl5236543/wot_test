from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinValueValidator
from .choices import *

class Player(models.Model):
    """Игрок"""

    name = models.CharField(
        max_length=50,
    )

    battle_count = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        blank=True,
        verbose_name='количество боёв',
    )

    wins_count = models.IntegerField(
        validators=[MinValueValidator(
            0,
            message="""
            это значение должно быть положительным целым числом
            """)],
        default=0,
        blank=True,
        verbose_name='количество побед',
    )

    tanks = models.ManyToManyField(
        'Tank',
        related_name='players',
        blank=True,
        verbose_name='танки',
    )

    photo = models.ImageField(
        verbose_name='фото',
        upload_to='players/',
        null=True,
    )

    @property
    def vn8(self):
        return self.wins_count / self.battle_count + 777

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
             


class TankProperties(models.Model):
    """ТТХ танка"""

    hp = models.IntegerField(verbose_name='количество ХП')

    speed = models.IntegerField(
        help_text='укажыте пожалуйста адекватные цыфры, а не как у колёснуков',
        verbose_name='скорость',
    )

    tank = models.OneToOneField(
        'Tank',
        on_delete=models.CASCADE,
        related_name='properties',
        null=True,
    )

    class Meta:
        verbose_name = 'ТТХ'
        verbose_name_plural = 'ТТХ'



class Tank(models.Model):
    """танк"""

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='название',
        help_text="""
        <img src="https://s8.travelask.ru/system/images/files/000/042/524/wysiwyg_jpg/frog-photography-27__880.jpg?1486386835" width=100px>
        """,
        error_messages={
            'unique': 'танк с таким названием уже есть'
        },
        validators=[
            MaxLengthValidator(10, message="""
            название не должно превышать 10 символов
            """)
        ]
    )

    lvl = models.IntegerField(
        verbose_name='уровень',
        choices=LVL,
        default=8,
    )

    premium = models.BooleanField(
        default=False,
        verbose_name='премиумный'
    )

    type = models.IntegerField(
        verbose_name='класс',
        choices=CLASSSES,
        null=True
    )

    photo = models.ImageField(
        verbose_name='фото',
        upload_to='tanks/',
        null=True,
    )

    class Meta:
        verbose_name = 'танк'
        verbose_name_plural = 'танки'

    def __str__(self):
        return self.name

