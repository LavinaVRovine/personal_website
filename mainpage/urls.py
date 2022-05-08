from django.conf.urls import url
from .views import ProjectListAndFormView, TinderView

urlpatterns = [
    url(r'^$', ProjectListAndFormView.as_view(), name='main'),
    # url(r'^tinder$', TinderView.as_view(), )
]
