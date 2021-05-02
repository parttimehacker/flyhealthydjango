from rest_framework import serializers

from .models import Content, Volume, Boilerplate


# Serializers define the API representation.
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['volume', 'get_section_display', 'headline', 'posted', 'source', 'description', 'link']


# Serializers define the API representation.
class VolumeSerializer(serializers.ModelSerializer):
    articles = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Volume
        fields = ('number', 'published', 'published_at', 'articles')


class BoilerplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boilerplate
        fields = ['volume', 'active', 'posted', 'headline', 'description', 'get_section_display']
