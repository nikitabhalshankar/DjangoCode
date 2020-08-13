from django.urls import path

from .views import ListProduct,DetailProduct


urlpatterns = [
    path('', ListProduct.as_view()),
    path('<int:pk>/', DetailProduct.as_view()),
]
