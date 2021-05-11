from rest_framework import serializers

from .models import Researcher, Roles


# Serializers define the API representation.
class ResearcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Researcher
        fields = ['name', 'active', 'get_role_display', 'organization', 'public_allowed', 'email', 'website']

