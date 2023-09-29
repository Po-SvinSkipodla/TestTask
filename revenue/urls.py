from django.urls import path

from revenue.views import RevenueView

urlpatterns = [
    path("revenues/", RevenueView.as_view()),
]

app_name = "revenue"
