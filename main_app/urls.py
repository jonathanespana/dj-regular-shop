from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/category/', views.category, name='category'),
    path('shop/category/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/category/<int:product_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cart/', views.cart, name='cart'),
    path('team/', views.team, name="team"),
    path('team/team-member', views.team_member, name='team_member'),
    path('checkout/', views.checkout, name='checkout'),
]