from rest_framework import serializers
from api.models import photo_card, LANGUAGE_CHOICES, STYLE_CHOICES


class PhotoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo_card
        fields = ('id', 'label', 'url', 'swipe_val', 'date_created', 'date_modified')