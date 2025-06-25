from django.contrib import admin
from .models import *

from django.contrib import admin
from .models import Project, Record, Company_Admin, Company_Name, InvoiceRecord


class RecordUser(admin.ModelAdmin):
    list_display = ['team_leader_name', 'associate_name', 'project','plot', 'plot_size', 'client_name', 'mobile', 'total_price', 'agreement_values', 'discount', 'cash_amount', 'cheque_amount', 'cheque_no', 'sum_amount', 'remaining_amount']


class ProjectUser(admin.ModelAdmin):
    list_display = ['project_name']

# class InvoiceUser(admin.ModelAdmin):
#     list_display = ['sale', 'purchase', 'date', 'total_amount']
    
class Company_AdminUser(admin.ModelAdmin):
    list_display = ['com_name', 'admin_id', 'gst_no', 'mobile', 'address', 'city', 'pincode', 'state', 'bank_name', 'account_name', 'account_no', 'ifc', 'bank_address', 'created_date', 'updated_date']

class Company_NameUser(admin.ModelAdmin):
    list_display = ['new_company_name', 'company_admin_user', 'company_id', 'company_gst_no', 'company_mobile','company_address', 'company_city', 'company_pincode', 'company_state', 'created_date', 'updated_date']

class InvoiceRecordUser(admin.ModelAdmin):
    list_display = ['company_na','invoice','invoice_no','product_service','hsn_code','qty', 'rate', 'amount', 'gst_rate', 'total_amount', 'created_date', 'updated_date']



admin.site.register(Company_Admin, Company_AdminUser)
admin.site.register(Project, ProjectUser)
admin.site.register(Record, RecordUser)
admin.site.register(Payment)
admin.site.register(Company_Name, Company_NameUser)
admin.site.register(InvoiceRecord, InvoiceRecordUser)





