
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_anonce', models.IntegerField()),
                ('type_maison', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prix_location', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
