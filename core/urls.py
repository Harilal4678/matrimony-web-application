from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_setup, name='profile_setup'),
    path('preferences/', views.preference_setup, name='preference_setup'),
    path('search/', views.search_profiles, name='search_profiles'),
    path('suggestions/', views.suggestions_view, name='suggestions'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('payment/', views.payment_page, name='payment_page'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('chat/<str:username>/', views.chat_view, name='chat'),
    
]