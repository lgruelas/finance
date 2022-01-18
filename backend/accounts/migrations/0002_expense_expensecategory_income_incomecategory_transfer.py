# Generated by Django 3.2.7 on 2022-01-18 06:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Expense Categories',
            },
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Income Categories',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('is_payed', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('account_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfers_origin', to='accounts.account')),
                ('account_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfers_destiny', to='accounts.account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('is_payed', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incomes', to='accounts.account')),
                ('income_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incomes', to='accounts.incomecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('is_payed', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenses', to='accounts.account')),
                ('expense_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenses', to='accounts.expensecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]