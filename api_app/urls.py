from django.urls import path
from api_app import views


urlpatterns = [
    path('cart-items/', views.CartItemViews.as_view()),
    path('cart-items/<int:id>', views.CartItemDetailViews.as_view())
]
