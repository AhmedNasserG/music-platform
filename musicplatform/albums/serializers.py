from rest_framework.serializers import ModelSerializer

from .models import Album, Song


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.release_date = validated_data.get(
            'release_date', instance.release_date)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.reviewed_by_admin = validated_data.get(
            'reviewed_by_admin', instance.reviewed_by_admin)
        instance.save()
        return instance


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.album = validated_data.get('album', instance.album)
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.audio = validated_data.get('audio', instance.audio)
        instance.save()
        return instance
