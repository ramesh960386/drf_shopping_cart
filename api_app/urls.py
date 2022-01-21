from django.db import router
from django.urls import path
from api_app import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('cart-items/', views.CartItemViews.as_view()),
    path('cart-items/<int:id>', views.CartItemDetailViews.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
