
from django.urls import path,include
from . import views
urlpatterns = [
   path('vs1',views.vs),
   path('fun1',views.fuc)
]
