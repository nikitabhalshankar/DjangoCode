from django.urls import path

from .views import ListProduct,DetailProduct,PurchaseListProduct,PurchaseDetailProduct


urlpatterns = [
    path('', ListProduct.as_view()),
    path('<int:pk>/', DetailProduct.as_view()),
    path('purchase/<int:pk>/', PurchaseListProduct.as_view()),
    path('purchaseorder/<int:pk>/', PurchaseDetailProduct.as_view()),
]
