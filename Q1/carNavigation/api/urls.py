from django.urls import path
from . import views


urlpatterns = [
    path("",views.apiOverview,name="api-overview"),
    path("records/",views.lastNavigationRecords,name="navigation-records"),  
]