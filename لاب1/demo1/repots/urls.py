


from django.urls import path

from .views import liststudent ,insertliststudents

urlpatterns = [
    path('list',liststudent),
    path('insert',insertliststudents),

]
