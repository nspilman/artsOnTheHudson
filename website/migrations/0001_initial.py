# Generated by Django 2.2 on 2019-04-23 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('bulletin', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blurb', models.CharField(max_length=300)),
                ('photo', models.ImageField(default='website/static/website/images/davidStaffLogo.jpg', upload_to='images')),
                ('body', models.TextField(default='Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?')),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blurb', models.CharField(max_length=300)),
                ('photo', models.ImageField(default='website/static/website/images/davidStaffLogo.jpg', upload_to='images')),
                ('body', models.TextField(default='Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?')),
                ('url', models.CharField(max_length=100)),
                ('fb_url', models.CharField(blank=True, max_length=100, null=True)),
                ('ticket_url', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(default='', max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Incomingmessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('sub_time', models.TimeField()),
                ('sub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blurb', models.CharField(max_length=300)),
                ('photo', models.ImageField(default='website/static/website/images/davidStaffLogo.jpg', upload_to='images')),
                ('body', models.TextField(default='Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?')),
                ('url', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('medialink', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('blurb', models.TextField(default='')),
                ('publication', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(null=True, upload_to='images')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='website/static/website/images/davidStaffLogo.jpg', upload_to='website/static/website/images')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('parent_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Events')),
                ('students', models.ManyToManyField(blank=True, null=True, to='people.Person')),
            ],
        ),
    ]
