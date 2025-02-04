from rest_framework import serializers
from .models import AcidInfo, RecksonInfo, Gameprogress, MainInfo

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainInfo
        fields = ('paragraph', 'new_paragraph', 'date_update')


class AcidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcidInfo
        fields = ('name', 'bio', 'vk_link', 'tg_link')


class RecksonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecksonInfo
        fields = ('name', 'bio', 'vk_link', 'tg_link')

