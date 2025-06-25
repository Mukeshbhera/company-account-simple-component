from django.db import models
from uuid import uuid4
from home.models import *





class Company_Admin(models.Model):
    com_name        = models.CharField(max_length=200, null=True, blank=True)
    admin_id        = models.CharField(max_length=200, unique=True, default=uuid4,)
    gst_no          = models.CharField(max_length=200, unique=True)
    mobile          = models.CharField(max_length=200, null=True, blank=True)
    address         = models.CharField(max_length=200, null=True, blank=True)
    city            = models.CharField(max_length=25, null=True, blank=True)
    pincode         = models.CharField(max_length=6, null=True, blank=True)
    state           = models.CharField(max_length=30, null=True, blank=True)
    bank_name       = models.CharField(max_length=30, null=True, blank=True)
    account_name    = models.CharField(max_length=30, null=True, blank=True)
    account_no    = models.CharField(max_length=30, null=True, blank=True)
    ifc             = models.CharField(max_length=30, null=True, blank=True)
    bank_address    = models.CharField(max_length=30, null=True, blank=True)        
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.com_name



class Company_Name(models.Model):
    new_company_name        = models.CharField(max_length=200, null=True, blank=True)
    company_admin_user      = models.ForeignKey(Company_Admin, on_delete=models.CASCADE, null=True, blank=True)
    company_id              = models.CharField(max_length=200, unique=True, default=uuid4,)
    company_gst_no          = models.CharField(max_length=200, unique=True)
    company_mobile          = models.CharField(max_length=200, null=True, blank=True)
    company_address         = models.CharField(max_length=200, null=True, blank=True)
    company_city            = models.CharField(max_length=25, null=True, blank=True)
    company_pincode         = models.CharField(max_length=6, null=True, blank=True)
    company_state           = models.CharField(max_length=30, null=True, blank=True)
    created_date            = models.DateTimeField(auto_now_add=True)
    updated_date            = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.new_company_name

    # def save(self, *args, **kwargs):
    #     if self.company_admin_user and not self.company_id:  
    #         self.company_id = f"{self.company_admin_user.admin_id}_{uuid4()}"
    #     super().save(*args, **kwargs)



# class Invoice(models.Model):
#     sale = models.CharField(max_length=50)
#     purchase = models.CharField(max_length=100)


# class Invoice(models.Model):
#     GST_CHOICES = [
#         (12, '12%'),
#         (18, '18%'),
#         (28, '28%'),
#     ]

#     sale = models.CharField(max_length=50)
#     purchase = models.CharField(max_length=100)
#     date = models.DateField(auto_now_add=True)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     gst_rate = models.IntegerField(choices=GST_CHOICES, default=18) 

    # @property
    # def gst_amount(self):
    #     """Calculate GST amount based on the selected GST rate."""
    #     return (self.total_amount * self.gst_rate) / 100

    # @property
    # def total_with_gst(self):
    #     """Calculate the total amount including GST."""
    #     return self.total_amount + self.gst_amount

    # def __str__(self):
    #     return f"Invoice: {self.sale} - {self.purchase} - {self.total_amount}"




# class InvoiceRecord(models.Model):
#     GST_CHOICES = [
#         (12, '12%'),
#         (18, '18%'),
#         (28, '28%'),
#     ]
    
#     Invoice_CHOICES = [
#         (sales , 'Sales'),
#         (purchase, 'Purchases'),
#     ]

    
#     company_na          = models.ForeignKey(Company_Name, on_delete=models.CASCADE, null=True, blank=True)
#     invoice             = models.CharField(max_length=255, default='Sales', choices=Invoice_CHOICES)
#     invoice_no          = models.CharField(max_length=200, null=True, blank=True)
#     product_service     = models.CharField(max_length=200, null=True, blank=True)
#     hsn_code            = models.CharField(max_length=200, null=True, blank=True)
#     qty                 = models.CharField(max_length=200, null=True, blank=True)
#     rate                = models.CharField(max_length=200, null=True, blank=True)
#     amount              = models.CharField(max_length=200, null=True, blank=True)
#     gst_rate            = models.IntegerField(choices=GST_CHOICES, default=18)
#     total_amount        = models.IntegerField(null=True, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date        = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.invoice


class InvoiceRecord(models.Model):
    GST_CHOICES = [
        (12, '12%'),
        (18, '18%'),
        (28, '28%'),
    ]
    
    Invoice_CHOICES = [
        ('sales', 'Sales'),
        ('purchase', 'Purchases'),
    ]

    company_na = models.ForeignKey(Company_Name, on_delete=models.CASCADE, null=True, blank=True)
    invoice = models.CharField(max_length=255, default='Sales', choices=Invoice_CHOICES)
    invoice_no = models.CharField(max_length=200, null=True, blank=True)
    product_service = models.CharField(max_length=200, null=True, blank=True)
    hsn_code = models.CharField(max_length=200, null=True, blank=True)
    qty = models.CharField(max_length=200, null=True, blank=True)
    rate = models.CharField(max_length=200, null=True, blank=True)
    amount = models.CharField(max_length=200, null=True, blank=True)
    gst_rate = models.IntegerField(choices=GST_CHOICES, default=18)
    total_amount = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice

    
    
        # agreement_values    = models.CharField(max_length=15, null=True, blank=True)
    # deal_values         = models.CharField(max_length=15, null=True, blank=True)
    # cash_amount         = models.CharField(max_length=15, null=True, blank=True)
    # cheque_amount       = models.CharField(max_length=15, null=True, blank=True)
    # cheque_no           = models.CharField(max_length=6, null=True, blank=True)
    # sum_amount          = models.CharField(max_length=15, null=True, blank=True)
    # remaining_amount    = models.CharField(max_length=15, null=True, blank=True)
    
    
    
    
    
    
# class Payment(models.Model):
#     records             = models.ForeignKey(Record, on_delete=models.CASCADE, null=True, blank=True)
#     payment_type        = models.CharField(max_length=10, null=True, blank=True)
#     cheque_number       = models.CharField(max_length=15, null=True, blank=True)
#     cheque_amount       = models.CharField(max_length=15, null=True, blank=True)
#     case_amount         = models.CharField(max_length=20, null=True, blank=True)
#     total_amount        = models.CharField(max_length=20, null=True, blank=True)
#     remaining_amount    = models.CharField(max_length=20, null=True, blank=True)
#     received_amount     = models.CharField(max_length=20, null=True, blank=True)
#     payment_description = models.TextField(null=True, blank=True)
#     created_date        = models.DateTimeField(auto_now_add=True)
#     updated_date        = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.total_amount
































class Project(models.Model):
    project_name = models.CharField(max_length=200, null=True, blank=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name



class Record(models.Model):
    team_leader_name    = models.CharField(max_length=200, null=True, blank=True)
    associate_name      = models.CharField(max_length=200, null=True, blank=True)
    project             = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    plot                = models.CharField(max_length=200,  null=True, blank=True)
    plot_size           = models.CharField(max_length=200,  null=True, blank=True)
    client_name         = models.CharField(max_length=200, null=True, blank=True)
    mobile              = models.CharField(max_length=13)
    total_price         = models.IntegerField(null=True, blank=True)
    discount            = models.CharField(max_length=15, null=True, blank=True)
    agreement_values    = models.CharField(max_length=15, null=True, blank=True)
    deal_values         = models.CharField(max_length=15, null=True, blank=True)
    cash_amount         = models.CharField(max_length=15, null=True, blank=True)
    cheque_amount       = models.CharField(max_length=15, null=True, blank=True)
    cheque_no           = models.CharField(max_length=6, null=True, blank=True)
    sum_amount          = models.CharField(max_length=15, null=True, blank=True)
    remaining_amount    = models.CharField(max_length=15, null=True, blank=True)
    # created_date        = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
    
class Payment(models.Model):
    records             = models.ForeignKey(Record, on_delete=models.CASCADE, null=True, blank=True)
    payment_type        = models.CharField(max_length=10, null=True, blank=True)
    cheque_number       = models.CharField(max_length=15, null=True, blank=True)
    cheque_amount       = models.CharField(max_length=15, null=True, blank=True)
    case_amount         = models.CharField(max_length=20, null=True, blank=True)
    total_amount        = models.CharField(max_length=20, null=True, blank=True)
    remaining_amount    = models.CharField(max_length=20, null=True, blank=True)
    received_amount     = models.CharField(max_length=20, null=True, blank=True)
    payment_description = models.TextField(null=True, blank=True)
    created_date        = models.DateTimeField(auto_now_add=True)
    updated_date        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.total_amount




