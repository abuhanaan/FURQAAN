from django.conf.urls import url
from . import views

app_name = 'inventory'

urlpatterns = [
    url('^$', views.ItemListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name='detail'),
    url(r'^create-item/$', views.ItemCreateView.as_view(), name='create-item'),
    url(r'^update/(?P<pk>\d+)/$', views.ItemUpdateView.as_view(),
        name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ItemDeleteView.as_view(),
        name='delete'),
    url(r'^create-trans/$', views.TransactionCreateView.as_view(),
        name='create-trans'),
    url('^trans-list/$', views.TransactionListView.as_view(),
        name='trans-list'),
    url(r'^(?P<pk>\d+)/$', views.TransactionDetailView.as_view(),
        name='trans-detail'),
    url(r'^update-trans/(?P<pk>\d+)/$', views.TransactionUpdateView.as_view(),
        name='update'),
]
