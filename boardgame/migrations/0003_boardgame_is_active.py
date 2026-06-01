from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgame', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
