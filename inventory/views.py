from django.shortcuts import render
from django.urls import reverse_lazy
from inventory import models
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

# Create your views here.


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class ItemListView(ListView):
    context_object_name = 'items'
    model = models.Item


class ItemDetailView(DetailView):
    context_object_name = 'item_detail'
    model = models.Item
    template_name = 'inventory/item_detail.html'


class ItemCreateView(CreateView):
    fields = ('item_name', 'maker', 'quantity', 'priceByDefault')
    model = models.Item


class ItemUpdateView(UpdateView):
    fields = ('quantity', 'priceByDefault')
    model = models.Item


class ItemDeleteView(DeleteView):
    model = models.Item
    success_url = reverse_lazy('inventory:list')


class TransactionCreateView(CreateView):
    fields = ('quantity', 'item', 'sellPrice', 'imei', 'custName', 'custAdd',
              'cusPhone', 'custEmail', 'note')
    model = models.Transaction


class TransactionListView(ListView):
    context_object_name = 'transactions'
    model = models.Transaction


class TransactionDetailView(DetailView):
    context_object_name = 'transaction_detail'
    model = models.Item
    template_name = 'inventory/transaction_detail.html'


class TransactionUpdateView(UpdateView):
    fields = ('quantity', 'sellPrice', 'custName', 'custAdd', 'cusPhone',
              'custEmail')
    model = models.Transaction


class TransactionDeleteView(DeleteView):
    model = models.Transaction
    success_url = reverse_lazy('inventory:trans-list')
