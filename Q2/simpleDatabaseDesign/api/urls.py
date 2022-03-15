from django.urls import path
from . import views


urlpatterns = [
    path("",views.apiOverview,name="api-overview"),
    path("bin-operation/",views.binOperationPairs,name="bin-operation-pairs"),
]