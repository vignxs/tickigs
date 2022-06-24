# Generated by Django 3.2.12 on 2022-03-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_delete_customertechnology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CreatedOn',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Status',
            field=models.CharField(default='Open', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='UpdatedOn',
            field=models.DateField(default='Null'),
        ),
    ]