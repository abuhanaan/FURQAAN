from django.shortcuts import render
from django.contrib import messages
from easy_pdf.views import PDFTemplateResponseMixin
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from inventory import models
from inventory.models import Log, Item, Transaction
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

# Create your views here.

User = get_user_model()


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


class TransactionCreateView(LoginRequiredMixin, CreateView,):
    fields = ('quantity', 'item', 'sellPrice', 'imei', 'custName', 'custAdd',
              'cusPhone', 'custEmail', 'note')
    model = models.Transaction

    # def cashierDataMgmt(self, *args, **kwargs,):
    #    if self.item == log.item and self.quantity < log.quantity_assigned:
    #        log.quantity_sold += self.quantity
    #    return log.quantity_sold
    # def sortData(request, self, *args, **kwargs):
    # import pdb
    # pdb.set_trace()

    def sortData(self, request, quantity, log_id):
        log = Log.objects.get(pk=log_id)
        quantity = request.POST.get('quantity')

        if self.item.item_id == log.item.item_id and self.quantity < log.quantity_inStock:
            log.quantity_sold += quantity
        else:
            messages.warning(request, 'The quantity you intend to sell out is lower than the pieces in your stock')
        log.save()
        return log.quantity_sold

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.sortData(self.request, 'quantity', Log.log_id)
        self.object.save()
        return super().form_valid(form)


"""
def transactionView(request):
    item = Item.objects.get(pk=Item.item_id)
    quantity = request.POST.get('quantity')
    sellPrice = request.POST.get('sellPrice')
    imei = request.POST.get('imei')
    custName = request.POST.get('custName')
    custAdd = request.POST.get('custAdd')
    cusPhone = request.POST.get('cusPhone')
    custEmail = request.POST.get('custEmail')
    note = request.POST.get('note')

    transaction = Transaction(item=item, quantity=quantity,
                              sellPrice=sellPrice, imei=imei,
                              custName=custName, custAdd=custAdd,
                              cusPhone=cusPhone, custEmail=custEmail,
                              note=note)

    log = Log.objects.get(pk=Log.log_id)
    object.user = request.user
    if item.item_id == log.item.item_id and quantity < log.quantity_inStock:
        log.quantity_sold += quantity
    else:
        messages.warning(request, 'The quantity you intend to sell out is lower than the pieces in your stock')
    log.save()
    transaction.save()
    # return log.quantity_sold
    return render(request, 'inventory/transaction_form.html',
                  {'transaction': transaction})
"""


class TransactionListView(LoginRequiredMixin, ListView):
    context_object_name = 'transactions'
    model = models.Transaction


class TransactionDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'transaction_detail'
    model = models.Transaction
    template_name = 'inventory/transaction_detail.html'


class PrintReceipt(PDFTemplateResponseMixin, DetailView, LoginRequiredMixin):
    model = models.Transaction
    template_name = 'inventory/trans_receipt.html'

    """
    def print(self):
        self.object = self.get_object()
        return self.object
    """


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('quantity', 'sellPrice', 'custName', 'custAdd', 'cusPhone',
              'custEmail')
    model = models.Transaction


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Transaction
    success_url = reverse_lazy('inventory:trans-list')


class CashierTransactionList(LoginRequiredMixin, ListView):
    model = models.Transaction
    template_name = 'inventory/log_list.html'

    def get_queryset(self):
        try:
            self.transaction.user = User.objects.prefetch_related(
                'transactions').get(username__iexact=self.kwargs.get(
                    'username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.transaction_user.transactions.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transaction_user'] = self.transaction_user
        return context


class LogCreateView(LoginRequiredMixin, CreateView):
    fields = ('user', 'item', 'quantity_assigned', 'quantity_sold', 'date')
    model = models.Log

    """
    def get_remainder(self):
        log.quantity_inStock = log.quantity_assigned - log.quantity_sold
        return log.quantity_inStock
    """


class LogDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Log
    success_url = reverse_lazy('inventory:list_cashierLog')


class LogUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Log
    fields = ('quantity_assigned')


class LogListView(LoginRequiredMixin, ListView):
    model = models.Log
    context_object_name = 'logs'


class LogDetailView(LoginRequiredMixin, DetailView):
    model = models.Log
    context_object_name = 'cashier_daily_log_detail'
