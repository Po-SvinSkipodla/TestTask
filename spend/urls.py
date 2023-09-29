from django.urls import path

from spend.views import SpendView

urlpatterns = [
    path("spends/", SpendView.as_view()),
]

app_name = "spend"
