from django.urls import path
from tank.views import TankView

urlpatterns = [
    path('', TankView,name="tank"),
    path('<int:id>', TankView,name="Tank_details")
]