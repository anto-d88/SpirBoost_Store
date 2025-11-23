from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    if not User.objects.filter(username='antonio').exists():
        User.objects.create_superuser(
            username='antonio',
            email='antonio@example.com',
            password='Antonio12345'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
