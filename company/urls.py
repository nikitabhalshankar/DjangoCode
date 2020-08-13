from django.urls import path

from .views import ListCompany,DetailCompany


urlpatterns = [
    path('', ListCompany.as_view()),
    path('<int:pk>/', DetailCompany.as_view()),
]
