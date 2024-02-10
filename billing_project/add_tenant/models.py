from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
    
class ShoppingComplex(models.Model):
    complex_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.complex_name
    
class Contract(models.Model):
    CONTRACT_TYPE_CHOICES = {
        'EC': 'Договор энергетики',
        'HC': 'Договор отопления',
        'SC': 'Какой то договор',
    }
    shopping_complex = models.ManyToManyField(ShoppingComplex)
    contract_num = models.CharField(verbose_name="Номер договора", max_length=50)
    start_date = models.DateField(verbose_name="Начало договора")
    finish_date = models.DateField(verbose_name="Конец договора")
    contract_date = models.DateField(verbose_name="Дата договора")
    contract_type = models.CharField(max_length=100, choices = CONTRACT_TYPE_CHOICES)
    advertising_tax = models.BooleanField(verbose_name = "Налог на рекламу", default=False)
    is_closed = models.BooleanField(verbose_name = "Закрыт(Архив)", default=False)
    at_work = models.BooleanField(verbose_name = "В работе", default=False)
    comment = models.TextField(verbose_name = "Комментарий")
    invoice_num = models.CharField(verbose_name="Номер договора в счете", max_length=50)
    basic_contract = models.ManyToManyField("Contract", blank=True, verbose_name = "Основной договор", related_name="contract_basic")
    basic_lot = models.IntegerField(verbose_name = "Основной лот", blank=True, null=True)
    client = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="contract_client", null=True)
    
    def __str__(self) -> str:
        return f'Договор номер {self.contract_num}, Cоздан - {self.contract_date}'