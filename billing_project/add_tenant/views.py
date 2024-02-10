from django.shortcuts import render
from .models import Contract, ShoppingComplex
from django.views import generic
from .forms import CreateClientForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

sc_menu = ShoppingComplex.objects.all()
c_type_menu = Contract.CONTRACT_TYPE_CHOICES

# Create your views here.
# def add_tenant_view(request):
#     if request.method == 'POST':
#         client = Client.objects.create(
#             # user = request.user,
#             shopping_complex = ShoppingComplex.objects.get(complex_name=request.POST['shopping_complex']),
#         )
#         contract = Contract.objects.create(
#             contract_num= request.POST['contract_num'],
#             start_date = request.POST['start_date'],
#             finish_date = request.POST['finish_date'],
#             contract_date = request.POST['contract_date'],
#             contract_type = request.POST['contract-type'],
#             advertising_tax = request.POST['advertising_tax'],
#             is_closed = request.POST['is_closed'],
#             at_work = request.POST['at_work'],
#             comment = request.POST['comment'],
#             invoice_num = request.POST['invoice_num'],
#             # basic_contract = request.POST['basic_contract'],
#             # basic_lot = request.POST['basic_lot'],
#             client = client,
#         )
#     return render(request, "add_tenant/index.html", {'shopping_complex_menu': sc_menu, 'contract_type_menu': c_type_menu})
# sdacvvcfsacfv1234e341

class AddTenant(LoginRequiredMixin, generic.CreateView):
    template_name = "add_tenant/index.html"
    form_class = CreateClientForm
    login_url = reverse_lazy("auth_reg:login")
    success_url = '/'
    def form_valid(self, form):
        contract = form.save(commit=False)
        contract.client = self.request.user
        return super().form_valid(form)