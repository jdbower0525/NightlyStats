from rest_framework import serializers
from .models import Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('url', 'date', 'food_sales', 'beverage_sales',
                  'liquor_sales', 'beer_sales', 'wine_sales', 'net sales',
                  'forecast', 'last year', 'WTD sales', 'WTD Budget',
                  'WTD Sales Last Year', '+/- vs. last year', 'LBW sales',
                  'liquor mix', 'foh actual', 'foh target', 'foh variance',
                  'boh actual', 'boh target', 'boh variance', 'comp 2',
                  'comp 11', 'comp 6', 'comp 4', 'comp 7', 'comp 8',
                  'takeaway sales', 'takeaway %', 'deliveries/sales',
                  'headwait', 'drop variance', 'managers', 'food harvest',
                  'TCI %', 'TCI variance', 'lunch sales', 'PC drawer'
                  )
