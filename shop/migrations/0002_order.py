# Generated by Django 3.1.7 on 2021-04-16 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('despatched', 'despatched'), ('cancelled', 'cancelled')], default='ordered', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.mobile')),
            ],
        ),
    ]
