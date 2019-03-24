# Generated by Django 2.1.7 on 2019-03-22 17:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Roll Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dept_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.Department', verbose_name='Department Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstName',
            field=models.CharField(max_length=200, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(max_length=200, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_img',
            field=models.ImageField(upload_to='media/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tot_cred',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Total Credits'),
        ),
    ]
