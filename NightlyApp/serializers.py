from rest_framework import serializers
from .models import Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('url', 'date', 'food_sales', 'beverage_sales',
                  'liquor_sales', 'beer_sales', 'wine_sales', 'net_sales',
                  'forecast', 'last_year', 'vs_lastyear' 'WTD_sales', 'WTD_budget',
                  'WTD_sales_last_year', 'week_vs_lastyear', 'LBW_sales',
                  'liquor_mix', 'foh_actual', 'foh_target', 'foh_variance',
                  'boh_actual', 'boh_target', 'boh_variance', 'comp_2',
                  'comp_11', 'comp_6', 'comp_4', 'comp_7', 'comp_8',
                  'takeaway_sales', 'takeaway_percentage', 'deliveries_sales',
                  'headwait', 'drop_variance', 'managers', 'food_harvest',
                  'TCI_percentage', 'TCI_variance', 'lunch_sales', 'PC_drawer'
                  )
