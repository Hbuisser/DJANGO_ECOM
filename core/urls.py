from django.urls import path
from .views import products, checkout
from .views import (
    checkout,
    ItemDetailView,
    # CheckoutView,
     HomeView,
    # OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    # remove_single_item_from_cart,
    # PaymentView,
    # AddCouponView,
    # RequestRefundView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
]