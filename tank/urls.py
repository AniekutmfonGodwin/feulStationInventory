from django.urls import path
from tank.views import (
    TankView,
    TankListCreateView,
    TankDetailUpdateView
    )

urlpatterns = [
    path('<int:id>', TankDetailUpdateView.as_view(),name="tank_details"),
    path('', TankListCreateView.as_view(),name="tank")
]