# Generated by Django 3.1 on 2021-02-28 15:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('research', '0001_initial'),
    ]

    def init_volumes(apps, schema_editor):
        volumes = [
            {'number': 1, 'published': True, 'published_at': '2021-04-27'},
            {'number': 2, 'published': True, 'published_at': '2021-05-04'},
            {'number': 3, 'published': False, 'published_at': '2021-05-11'},
        ]
        Volume = apps.get_model("research", "Volume")
        for i in range(len(volumes)):
            app = volumes[i]
            object = Volume(
                number=app['number'],
                published=app['published'],
                published_at=app['published_at'], )
            object.save()

    def init_boilerplate(apps, schema_editor):

        Volume = apps.get_model("research", "Volume")

        def link_volumes(vol_number):
            volumes = Volume.objects.filter(number=vol_number)
            return volumes.first()

        boilerplates = [
            {'active': True,
             'posted': '2021-04-27',
             'headline':
                 'Welcome',
             'description':
                 'Welcome to the Health Pass Insider published by members of the Health Pass Working Group ' \
                 'under the ACI-NA Business Information Technology (BIT) Committee. We’re just getting started ' \
                 'but have mapped out what we believe to be important initiatives and deliverables to keep the ' \
                 'ACI-NA membership well-informed with timely and actionable information.',
             'section': 'WE',
             'number': 2},
            {'active': True,
             'posted': '2021-04-27',
             'headline':
                 'Background',
             'description':
                 'The Health Pass newsletter is designed to ensure that the ACI-NA membership is kept informed ' \
                 'of the latest digital health pass information from around the globe in an organized and consistent ' \
                 'manner. While our goal is to provide valuable and timely information, we recognize that there ' \
                 'is an abundance of resources and data that may quickly become outdated due to the dynamic' \
                 'nature of this topic.',
             'section': 'BA',
             'number': 2},
            {'active': True,
             'posted': '2021-04-27',
             'headline':
                 'Disclaimer',
             'description':
                 'The articles and information in this newsletter are all taken directly from media sources ' \
                'published online and are available to the general public. The content has not been vetted' \
                 'for accuracy. The information provided in this newsletter is for situational awareness and ' \
                 'does not reflect the policy position, views, or recommendations of ACI-NA.',
             'section': 'DI',
             'number': 2},
        ]
        Boilerplate = apps.get_model("research", "Boilerplate")
        for i in range(len(boilerplates)):
            app = boilerplates[i]
            object = Boilerplate(id=i,
                                 active=app['active'],
                                 headline=app['headline'],
                                 posted=app['posted'],
                                 description=app["description"],
                                 section=app['section'],
                                 volume=link_volumes(app['number']))
            object.save()

    operations = [
        migrations.RunPython(init_volumes),
        migrations.RunPython(init_boilerplate),
    ]