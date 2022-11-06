# Generated by Django 3.2.16 on 2022-11-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_fuser_l_t'),
    ]

    operations = [
        migrations.CreateModel(
            name='SCHOOL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=20, verbose_name='学校名称')),
            ],
            options={
                'db_table': 'schools_table',
            },
        ),
    ]