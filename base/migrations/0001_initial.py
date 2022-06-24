# Generated by Django 3.2.12 on 2022-02-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('TechnologyId', models.IntegerField(primary_key=True, serialize=False)),
                ('TechnologyName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.BigAutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('MobileNumber', models.CharField(max_length=15)),
                ('IsProjectStarted', models.BooleanField()),
                ('Description', models.TextField()),
                ('Status', models.CharField(max_length=100)),
                ('CreatedOn', models.DateField()),
                ('UpdatedOn', models.DateField()),
                ('TechnologyName', models.ManyToManyField(to='base.Technology')),
            ],
        ),
    ]
