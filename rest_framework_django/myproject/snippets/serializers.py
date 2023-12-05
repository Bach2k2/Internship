from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ["id","url" , 'highlight',"title", "code", "linenos", "language", "style", "owner"]

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get("title", instance.title)
        instance.code = validated_data.get("code", instance.code)
        instance.linenos = validated_data.get("linenos", instance.linenos)
        instance.language = validated_data.get("language", instance.language)
        instance.style = validated_data.get("style", instance.style)
        instance.save()
        return instance


from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Snippet.objects.all()
#     )

#     class Meta:
#         model = User
#         fields = ["id", "username", "snippets"]
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']