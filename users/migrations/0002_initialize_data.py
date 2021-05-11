from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    def init_researchers(apps, schema_editor):
        researchers = [
            {'name': 'Dave Wilson', 'active': True, 'role': 'CO',
             'organization': 'Port of Seattle',
             'public_allowed': True, 'email': 'wilson.d@portseattle.org',
             'website': 'https://www.portseattle.org'},
            {'name': 'Danielle Aiello', 'active': True, 'role': 'CO',
             'organization': 'Boingo Wireless',
             'public_allowed': True, 'email': 'daiello@boingo.com',
             'website': 'https://www.boingo.com'},

            {'name': 'Eduardo Valencia', 'active': True, 'role': 'AI',
             'organization': 'Minneapolis–Saint Paul International Airport',
             'public_allowed': True, 'email': 'eduardo.valencia@mspmac.org',
             'website': 'https://www.mspairport.com'},
            {'name': 'Ana Zivanovic', 'active': True, 'role': 'AI',
             'organization': 'San Francisco International Airport',
             'public_allowed': True, 'email': 'ana.zivanovic@flysfo.com',
             'website': 'https://www.flysfo.com'},
            {'name': 'Sarosh Bhatti', 'active': True, 'role': 'AI',
             'organization': 'Edmonton International Airport',
             'public_allowed': True, 'email': 'sbhatti@flyeia.com',
             'website': 'https://flyeia.com'},

            {'name': 'Bryan Helaire', 'active': True, 'role': 'AS',
             'organization': 'GCR Inc.',
             'public_allowed': True, 'email': 'bhelaire@gocivix.com',
             'website': 'https://gocivix.com'},
            {'name': 'Tony Chapman', 'active': True, 'role': 'AS',
             'organization': 'Collins Aerospace',
             'public_allowed': True, 'email': 'tony.chapman@pulse.aero',
             'website': 'https://gocivix.com'},
        ]

        Researcher = apps.get_model('users', 'Researcher')
        for i in range(len(researchers)):
            app = researchers[i]
            object = Researcher(
                name=app['name'],
                active=app['active'],
                role=app['role'],
                organization=app['organization'],
                public_allowed=app['public_allowed'],
                email=app['email'],
                website=app['website'],
            )
            object.save()


    operations = [
        migrations.RunPython(init_researchers),
    ]
