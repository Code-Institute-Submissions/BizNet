from django.urls import path
from . import views 
from .views import (
    MembershipSelectView,
    PaymentView,
    updateTransactionRecords,
    cancelSubscription,
    # CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    )


urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('membership_profile', views.membership_profile, name='membership_profile'),
    # path('subscription/', views.Subscription, name='subscription'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', updateTransactionRecords, name='update-transactions'),
    path('cancel/', cancelSubscription, name='cancel'),


    # path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView, name='create-checkout-session'),

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    # path('user_subscription/', views.get_user_subscription, name='user_subscription'),
    # path('user_membership', views.user_membership, name='user_membership'),
    # path('', views.membership_list, name='membership_list'),

    # Stripe
    path('payment_history/', views.payment_history, name='payment_history'),
    path("config/", views.stripe_config),

    # path("webhook/", views.stripe_webhook, name='stripe_webhook'),
]
