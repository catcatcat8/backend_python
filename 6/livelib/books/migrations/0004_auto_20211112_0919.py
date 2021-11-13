# Generated by Django 3.2.8 on 2021-11-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20211111_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('name',), 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название книги'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('name', 'author')},
        ),
    ]
