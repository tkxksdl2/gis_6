from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscription'

urlpatterns = [
    path('subcribe/<int:project_pk>', SubscriptionView.as_view(), name='subscription'),

]