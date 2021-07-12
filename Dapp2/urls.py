
from django.urls import path,include
from . import views
urlpatterns = [
   path('vs1',views.vs),
   path('login',views.fuc),
   path('home',views.home1),
   path('about',views.about1),
   path('products',views.products1),
   path('services',views.services1),
   path('msi gaming s1',views.msi1),
   path('msi gaming s2',views.msi2),
   path('msi gaming s3',views.msi3),
   
   path('msi gaming s5',views.msi5),
   path('contact us',views.contactus1)
]
