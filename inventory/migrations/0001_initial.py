# Generated by Django 3.0.2 on 2020-05-14 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=15)),
                ('quantity', models.IntegerField(default=0)),
                ('priceByDefault', models.IntegerField(blank=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sellPrice', models.IntegerField(default=1)),
                ('imei', models.CharField(max_length=15)),
                ('custName', models.CharField(max_length=50)),
                ('custAdd', models.TextField(max_length=100)),
                ('cusPhone', models.CharField(blank=True, max_length=11)),
                ('custEmail', models.EmailField(blank=True, max_length=254)),
                ('note', models.TextField(blank=True, max_length=200)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_assigned', models.IntegerField(default=0)),
                ('quantity_sold', models.IntegerField(default=0)),
                ('quantity_inStock', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Manufacturer'),
        ),
    ]
