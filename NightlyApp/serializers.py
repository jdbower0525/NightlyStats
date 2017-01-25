from rest_framework import serializers
from .models import Day

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('url', 'date', 'closing_manager', 'headwait')
