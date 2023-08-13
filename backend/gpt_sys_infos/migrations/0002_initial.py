# Generated by Django 4.2 on 2023-08-13 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("gpt_sys_infos", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="systeminfo",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="system_infos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="refdata",
            name="system_info",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ref_datas",
                to="gpt_sys_infos.systeminfo",
            ),
        ),
        migrations.AddField(
            model_name="refdata",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ref_datas",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="refbook",
            name="system_info",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ref_books",
                to="gpt_sys_infos.systeminfo",
            ),
        ),
        migrations.AddField(
            model_name="refbook",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ref_books",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="content",
            name="data",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="content",
                to="gpt_sys_infos.refdata",
            ),
        ),
    ]
