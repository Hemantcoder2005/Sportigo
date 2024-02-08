from django.urls import path
from .views import home,issueEquipment,ava
urlpatterns = [
    path('',home,name="home"),
    path('issue',issueEquipment),
    path('issue/ava',ava)
]
