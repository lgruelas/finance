# Generated by Django 2.2.10 on 2020-06-04 01:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('balance', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('expected', models.DecimalField(decimal_places=4, max_digits=12)),
                ('must_show', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finance.Account')),
                ('bank', models.CharField(max_length=120)),
                ('is_investment', models.BooleanField(default=0)),
            ],
            bases=('finance.account',),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finance.Account')),
                ('cut', models.IntegerField()),
                ('pay', models.IntegerField()),
                ('bank', models.CharField(max_length=120)),
                ('credit', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
            bases=('finance.account',),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finance.Account')),
            ],
            bases=('finance.account',),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='account_from', to='finance.Account')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='account_to', to='finance.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('is_payed', models.BooleanField(default=1)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Category')),
            ],
        ),
    ]
