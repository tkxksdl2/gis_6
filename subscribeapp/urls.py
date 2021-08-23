from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscription'

urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscription'),
    path('list', SubscriptionListView.as_view(), name='list'),

]