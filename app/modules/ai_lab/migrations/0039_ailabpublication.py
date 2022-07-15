# Generated by Django 3.2.5 on 2021-07-02 14:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
        ('images', '0001_initial'),
        ('documents', '0001_initial'),
        ('ai_lab', '0038_auto_20210412_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiLabPublication',
            fields=[
                ('publicationpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='publications.publicationpage')),
                ('summary', models.CharField(max_length=255)),
                ('featured_resources', wagtail.fields.StreamField([('link', wagtail.blocks.PageChooserBlock(label='Page', page_type=['ai_lab.AiLabCaseStudy', 'ai_lab.AiLabGuidance', 'ai_lab.AiLabReport', 'ai_lab.AiLabExternalResource'], required=True))], blank=True)),
                ('download', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='documents.nhsxdocument')),
                ('featured_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.nhsximage')),
                ('topics', modelcluster.fields.ParentalManyToManyField(to='ai_lab.AiLabTopic')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
            bases=('publications.publicationpage', models.Model),
        ),
    ]
