from rest_framework import serializers
from rest_framework.serializers import Serializer
from location.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Location
        fields = ['id', 'latitude', 'longitude']

    def create(self, validated_data, *args, **kwargs):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance_to_update = Location.objects.filter(pk=instance.pk)
        if instance_to_update.exists():
            instance_to_update.update(**validated_data)
            return instance_to_update.first()
        else:
            raise serializers.ValidationError("Instance not found")