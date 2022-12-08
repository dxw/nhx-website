# Generated by Django 3.2.9 on 2022-12-08 12:04

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('core', '0049_homepagebannersettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteWideBannerSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_enabled', models.BooleanField(default=False, verbose_name='Enable banner')),
                ('site_wide_banner_theme', models.CharField(choices=[('nhs-dark-pink', 'NHS Dark Pink'), ('nhs-dark-grey', 'NHS Dark Grey'), ('nhs-pale-grey', 'NHS Pale Grey'), ('nhs-light-blue', 'NHS Light Blue')], default='nhs-dark-pink', max_length=15, verbose_name='Banner colour scheme')),
                ('site_wide_banner_body', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Banner content')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Site wide banner settings',
            },
        ),
    ]
