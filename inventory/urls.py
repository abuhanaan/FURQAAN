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
    url(r'^trans-list/(?P<pk>\d+)/$', views.TransactionDetailView.as_view(),
        name='trans-detail'),
    url(r'^print-reciept/(?P<pk>\d+)/$', views.PrintReceipt.as_view(),
        name='print-receipt'),
    url(r'^update-trans/(?P<pk>\d+)/$', views.TransactionUpdateView.as_view(),
        name='update-trans'),
    url(r'^delete-trans/(?P<pk>\d+)/$', views.TransactionDeleteView.as_view(),
        name='delete-trans'),
    url(r'^trans-list/my-trans/(?P<username>[-\w]+)/$',
        views.CashierTransactionList.as_view(), name='my-trans'),
    url(r'^create_cashierLog/$', views.LogCreateView.as_view(),
        name='create_cashierLog'),
    url(r'^list_cashierLog/', views.LogListView.as_view(),
        name='list_cashierLog'),
    url(r'^list_cashierLog/(?P<pk>\d+)/$', views.LogDetailView.
        as_view(), name='detail_cashierLog'),
    url(r'^update_cashierLog/(?P<pk>\d+)/$', views.LogUpdateView.
        as_view(), name='update_ashierLog'),
    url(r'^delete_cashierLog/(?P<pk>\d+)/$', views.LogDeleteView.
        as_view(), name='delete_cashierLog'),
]
