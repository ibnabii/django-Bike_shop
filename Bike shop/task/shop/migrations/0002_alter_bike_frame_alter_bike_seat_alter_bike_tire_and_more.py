# Generated by Django 4.0.4 on 2022-10-10 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.frame'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.seat'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='tire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.tire'),
        ),
        migrations.AlterField(
            model_name='order',
            name='bike',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.bike'),
        ),
    ]