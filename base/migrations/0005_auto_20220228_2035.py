# Generated by Django 3.2.12 on 2022-02-28 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220228_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertechnology',
            name='TechnologyId',
            field=models.ForeignKey(db_column='Technology_Id', on_delete=django.db.models.deletion.CASCADE, related_name='Technology_Id', to='base.technology'),
        ),
        migrations.AlterField(
            model_name='customertechnology',
            name='TechnologyName',
            field=models.ForeignKey(db_column='Technology_Name', on_delete=django.db.models.deletion.CASCADE, related_name='Technology_Name', to='base.technology'),
        ),
    ]
