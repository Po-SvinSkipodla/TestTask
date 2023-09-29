from rest_framework import serializers


class SpendSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    spend_sum = serializers.DecimalField(max_digits=10, decimal_places=2)
    impressions_sum = serializers.IntegerField()
    clicks_sum = serializers.IntegerField()
    conversion_sum = serializers.IntegerField()
    revenue_sum = serializers.DecimalField(max_digits=9, decimal_places=2)
