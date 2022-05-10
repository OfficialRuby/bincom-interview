from django.urls import path
from bincom.views import PollingUnitResultView, SummedPollingUnitResultView, AddNewPollingUnit

urlpatterns = [
    path('', PollingUnitResultView.as_view(), name='poll-result'),
    path('polling-unit-sum/', SummedPollingUnitResultView.as_view(), name='poll-sum'),
    path('add-polling-unit/', AddNewPollingUnit.as_view(), name='add-unit'),

]
