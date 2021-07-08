from django.urls import path
from .views import home, products, checkout
# from .views import (
#     ItemDetailView,
#     CheckoutView,
#     HomeView,
#     OrderSummaryView,
#     add_to_cart,
#     remove_from_cart,
#     remove_single_item_from_cart,
#     PaymentView,
#     AddCouponView,
#     RequestRefundView
# )

app_name = 'core'

urlpatterns = [
    path('', home, name='item-list'),
    path('checkout/', checkout, name='checkout'),
    path('product/', products, name='product'),
]