# Generated by Django 3.0.8 on 2020-07-14 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dalil', '0003_cate'),
    ]

    operations = [
        migrations.AddField(
            model_name='numbers',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dalil.cate'),
            preserve_default=False,
        ),
    ]
