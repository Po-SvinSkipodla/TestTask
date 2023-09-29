from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from revenue.serializers import RevenueSerializer


class RevenueView(APIView):
    def get(self, request):
        queryset = RevenueStatistic.objects.values("date", "name").annotate(
            revenue_sum=Sum("revenue"),
            spend_sum=Sum("spend"),
            impressions_sum=Sum("spend__impressions"),
            clicks_sum=Sum("spend__clicks"),
            conversion_sum=Sum("spend__conversion"),
        )
        serializer = RevenueSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
