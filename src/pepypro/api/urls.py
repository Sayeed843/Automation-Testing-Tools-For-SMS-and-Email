from django.conf.urls import url
from .views import (UserEmailListAPIView)
                               # UserEmailCreateAPIView,
                               # UserMessageListAPIView,
                               # UserMessageCreateAPIView)

urlpatterns = [
    url(r'^emails/$', UserEmailListAPIView.as_view()),
    # url(r'^emails/create/$', UserEmailCreateAPIView.as_view()),
    # url(r'^messages/$', UserMessageListAPIView.as_view()),
    # url(r'^messages/create/$', UserMessageCreateAPIView.as_view()),
]
