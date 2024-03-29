from django.urls import path

from . import views

from .views import CreateStripeCheckoutSessionView, CancelView, SuccessView

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/<slug:slug_category>/<slug:slug_subcategory>/', views.category, name='category'),
    path('shop/<slug:slug_name>/', views.product_detail, name='product_detail'),
    path('shop/category/<int:product_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path("create-checkout-session/<int:cart_id>/", CreateStripeCheckoutSessionView.as_view(), name="create-checkout-session"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path('shop/category/<int:product_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cart/', views.cart, name='cart'),
    path('team/', views.team, name="team"),
    path('team/team-member', views.team_member, name='team_member'),
    path('checkout/', views.checkout, name='checkout'),
]