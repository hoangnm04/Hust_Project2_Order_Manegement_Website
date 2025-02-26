# Generated by Django 4.2.6 on 2023-10-13 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='Parent category of this category (if any).', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.category'),
        ),
    ]
