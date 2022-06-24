



from django.urls import path

from .views import liststaff , insertliststaff

urlpatterns = [
    path('stafflist',liststaff),
    path('insertstaff',insertliststaff),

]