# Generated by Django 2.2.12 on 2022-04-01 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20220331_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_Section',
        ),
        migrations.RemoveField(
            model_name='coursesection',
            name='episodes',
        ),
        migrations.RemoveField(
            model_name='sector',
            name='sectorIMG',
        ),
        migrations.AddField(
            model_name='course',
            name='courseSectionData',
            field=models.ManyToManyField(blank=True, to='courses.CourseSection'),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='episodeData',
            field=models.ManyToManyField(blank=True, to='courses.EpisodeCourse'),
        ),
        migrations.AddField(
            model_name='sector',
            name='sectorLoadedIMG',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='sector_img_upload_absolute'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sector',
            name='relatedCourse',
            field=models.ManyToManyField(blank=True, to='courses.Course'),
        ),
    ]
