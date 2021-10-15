from rest_framework import serializers
from django.contrib.auth.models import User

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    The value extra_kwargs is needed when the app is namespaced like 'snippets:XX' 
    to link the object URL with the correct view
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippets:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')
        extra_kwargs = {
            'url': {'view_name': 'snippets:snippet-detail', 'lookup_field': 'pk'},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    The value extra_kwargs is needed when the app is namespaced like 'snippets:XX' 
    to link the object URL with the correct view
    """
    
    snippets = serializers.HyperlinkedRelatedField(view_name='snippets:snippet-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
        extra_kwargs = {
            'url': {'view_name': 'snippets:user-detail', 'lookup_field': 'pk'},
        }