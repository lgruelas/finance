# Generated by Django 3.2.7 on 2022-01-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_expense_expensecategory_income_incomecategory_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='', max_length=120),
        ),
    ]