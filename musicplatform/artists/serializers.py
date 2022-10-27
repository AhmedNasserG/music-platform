from rest_framework.serializers import ModelSerializer

from .models import Artist


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.social_media_link = validated_data.get(
            'social_media_link', instance.social_media_link)
        instance.save()
        return instance
