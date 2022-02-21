# Generated by Django 3.2.9 on 2021-11-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211112_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tank',
            options={'verbose_name': 'танк', 'verbose_name_plural': 'танки'},
        ),
        migrations.AddField(
            model_name='tank',
            name='type',
            field=models.IntegerField(blank=True, choices=[(0, 'ЛТ'), (1, 'ПТ'), (2, 'СТ'), (3, 'ТТ'), (4, 'САУ'), (5, 'ПТСАУ')], null=True, verbose_name='класс'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='lvl',
            field=models.IntegerField(choices=[(None, 'не известно'), ('до 2023 года', ((1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X'))), ('после 2023 года', ((11, 'XI'), (12, 'XII'), (13, 'XIII')))], verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='name',
            field=models.CharField(blank=True, help_text='\n        <img src="https://s8.travelask.ru/system/images/files/000/042/524/wysiwyg_jpg/frog-photography-27__880.jpg?1486386835" width=100px>\n        ', max_length=50, unique=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='premium',
            field=models.BooleanField(default=False, verbose_name='премиумный'),
        ),
    ]