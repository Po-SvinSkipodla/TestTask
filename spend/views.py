from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from spend.models import SpendStatistic
from spend.serializers import SpendSerializer


class SpendView(APIView):
    def get(self, request):
        queryset = SpendStatistic.objects.values("date", "name").annotate(
            spend_sum=Sum("spend"),
            impressions_sum=Sum("impressions"),
            clicks_sum=Sum("clicks"),
            conversion_sum=Sum("conversion"),
            revenue_sum=Sum("revenuestatistic__revenue", default=0),
        )
        serializer = SpendSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
