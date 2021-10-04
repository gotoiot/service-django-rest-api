from rest_framework import serializers
from django.contrib.auth.models import User

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(lookup_field="pk", view_name='snippets:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')
        extra_kwargs = {
            'url': {'view_name': 'snippets:snippet-detail', 'lookup_field': 'pk'},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(lookup_field="pk", many=True, view_name='snippets:snippet-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='snippets:user-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
        extra_kwargs = {
            'url': {'view_name': 'snippet:user-detail', 'lookup_field': 'pk'},
        }