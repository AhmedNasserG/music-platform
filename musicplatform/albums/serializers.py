from rest_framework.serializers import ModelSerializer

from .models import Album


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
