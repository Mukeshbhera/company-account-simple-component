from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
# from .models import Record, Project, Payment, Company_Admin, Company_Name
from django.db import IntegrityError
from datetime import datetime, timedelta
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
import pandas as pd
from datetime import datetime
from django.db.models import Sum
from django.views.decorators.http import require_POST
from django.db import transaction
import json
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from home.models import *
from uuid import uuid4



def log_in(request):
     if request.method == "GET":
         return render(request, 'log_in.html')
     if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Email/Username or Password Incorrect")
            return redirect('log_in')
        if user is not None:
            messages.success(request, "User login successfully")
            return redirect('home')
        
        # return render(request, 'index.html')
        
def logout_view(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('log_in')
    # return render(request, 'log_in.html')
    

def home(request):
    users = Company_Admin.objects.all()
    return render(request, 'admin_user.html', {'users': users})



# def main_company_add(request):
#     if request.method == 'POST':
#         com_name = request.POST['com_name']
#         gst_no = request.POST['gst_no']
#         mobile = request.POST['mobile']
#         address = request.POST['address']
#         pincode = request.POST['pincode']
#         city = request.POST['city']
#         state = request.POST['state']

#         admin = Company_Admin.objects.create(
#             com_name=com_name,  
#             gst_no=gst_no,
#             mobile=mobile,
#             address=address,
#             pincode=pincode,
#             city=city,
#             state=state,
#         )
#         messages.success(request, "Company Created Successfully.")
#         return redirect('home')

#     context = {
#         'messages': messages.get_messages(request),
#     }
#     return render(request, 'admin_add.html', context)

def main_company_add(request):
    if request.method == 'POST':
        # Get POST data
        com_name = request.POST.get('com_name')
        gst_no = request.POST.get('gst_no')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        
        # Fetch the current admin ID from the session or use a unique value
        admin_id = request.session.get('admin_id', str(uuid4()))

        # Create a new company
        Company_Admin.objects.create(
            com_name=com_name,
            gst_no=gst_no,
            mobile=mobile,
            address=address,
            pincode=pincode,
            city=city,
            state=state,
            admin_id=admin_id,
        )
        messages.success(request, "Company Created Successfully.")
        return redirect('home')  # Redirect back to the same page

    # Fetch companies for the current admin ID
    admin_id = request.session.get('admin_id', str(uuid4()))  # Use session admin ID
    users = Company_Admin.objects.filter(admin_id=admin_id)

    context = {
        'users': users,
        'admin_id': admin_id,
    }
    return render(request, 'admin_add.html', context)


def edit_company(request, admin_id):
    company = get_object_or_404(Company_Admin, admin_id=admin_id)

    if request.method == 'POST':
        # Update company details
        company.com_name = request.POST.get('com_name', company.com_name)
        company.gst_no = request.POST.get('gst_no', company.gst_no)
        company.mobile = request.POST.get('mobile', company.mobile)
        company.address = request.POST.get('address', company.address)
        company.save()
        return redirect('home') 
        # return JsonResponse({'message': 'Company updated successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

    
    
def baluhome(request, admin_id):
    # Filter companies by the passed admin_id
    users = Company_Admin.objects.filter(admin_id=admin_id)
    # users = Company_Admin.objects.filter(admin_id=admin_id)
    
    return render(request, 'company/company_user.html', {'users': users, 'admin_id': admin_id})

# def balu_company_add(request):
   
#     return render(request, 'company/company_add.html', context)


# def balu_company_add(request):
#     if request.method == 'POST':
#         # Get POST data
#         new_company_name = request.POST.get('new_company_name')
#         company_gst_no = request.POST.get('company_gst_no')
#         company_mobile = request.POST.get('company_mobile')
#         company_address = request.POST.get('company_address')
#         company_pincode = request.POST.get('company_pincode')
#         company_city = request.POST.get('company_city')
#         company_state = request.POST.get('company_state')

#         # Fetch the current admin user
#         admin_id = request.session.get('company_id', str(uuid4()))
        
#         Company_Name.objects.create(
#             new_company_name=new_company_name,
#             company_gst_no=company_gst_no,
#             company_mobile=company_mobile,
#             company_address=company_address,
#             company_pincode=company_pincode,
#             company_city=company_city,
#             company_state=company_state,
#             company_admin_user=admin_user,
#             )
#         messages.success(request, "Company Created Successfully.")
#         company_id = request.session.get('company_id', str(uuid4()))
#     admin_user = Company_Admin.objects.get(admin_id=admin_id)
#     companies = Company_Name.objects.filter(company_admin_user=admin_user)

#     context = {
#         'companies': companies,
#     }
#     return render(request, 'company/company_add.html', context)


# def balu_company_add(request):
#     if request.method == 'POST':
#         # Get POST data
#         new_company_name = request.POST['new_company_name']
#         company_gst_no = request.POST['company_gst_no']
#         company_mobile = request.POST['company_mobile']
#         company_address = request.POST['company_address']
#         company_pincode = request.POST['company_pincode']
#         company_city = request.POST['company_city']
#         company_state = request.POST['company_state']

#         admin1 = Company_Admin.objects.get(com_name=com_name)
#         Company_Name.objects.create(
#                 new_company_name=admin1,
#                 company_gst_no=company_gst_no,
#                 company_mobile=company_mobile,
#                 company_address=company_address,
#                 company_pincode=company_pincode,
#                 company_city=company_city,
#                 company_state=company_state,
#                 company_admin_user=admin_user,  # Link to the fetched admin user
#             )
#             messages.success(request, "Company Created Successfully.")

#     context = {
#         'companies': companies,
#     }
#     return render(request, 'company/company_add.html')


# def balu_company_add(request):
#     if request.method == 'POST':
#         # Fetch POST data
#         new_company_name = request.POST.get('new_company_name')
#         company_gst_no = request.POST.get('company_gst_no')
#         company_mobile = request.POST.get('company_mobile')
#         company_address = request.POST.get('company_address')
#         company_pincode = request.POST.get('company_pincode')
#         company_city = request.POST.get('company_city')
#         company_state = request.POST.get('company_state')

#         # Fetch logged-in user's ID
#         # admin_id = request.user.id
        
#         # try:
#         #     project = Company_Admin.objects.get(id=admin_id)
#         # except Project.DoesNotExist:
#         #     messages.error(request, "Project not found.")
#         #     return redirect('index')


#         # all_admins = Company_Admin.objects.get(admin_id=request.admin_id.id)
#         # print("Available Company_Admin Records:")
#         # for admin in all_admins:
#         #     print(f"Admin ID: {admin.admin_id}, Name: {admin.com_name}")

#             # Fetch the Company_Admin instance for the logged-in user
#         admin_email = request.user.id
#         admin1 = Company_Admin.objects.get(admin_id=admin_email)

#         # admin1 = Company_Admin.objects.get(com_name=admin_id)
            
#             # Create a new Company_Name record
#         Company_Name.objects.create(
#             new_company_name=new_company_name,
#             company_gst_no=company_gst_no,
#             company_mobile=company_mobile,
#             company_address=company_address,
#             company_pincode=company_pincode,
#             company_city=company_city,
#             company_state=company_state,
#             company_admin_user=admin1  # Assuming this is the ForeignKey
#         )
#         messages.success(request, "Company created successfully!")
            
#     # projects = Company_Admin.objects.all()
#     context = {
#         # 'users': users,
#         # 'projects': projects,
#         'messages': messages.get_messages(request),
#     }

#             # Success message    
#     return render(request, 'company/company_add.html', context)

# from django.contrib import messages
# from django.shortcuts import render, redirect
# from .models import Company_Admin, Company_Name

# def balu_company_add(request, admin_id):
#     try:
#         # Fetch the Company_Admin instance based on the admin_id
#         admin1 = Company_Admin.objects.get(admin_id=admin_id)
#     except Company_Admin.DoesNotExist:
#         # If no admin is found, redirect with an error message
#         messages.error(request, "Admin not found!")
#         return redirect('desired_error_page')  # Replace with your error page

#     if request.method == 'POST':
#         # Fetch POST data
#         new_company_name = request.POST.get('new_company_name')
#         company_gst_no = request.POST.get('company_gst_no')
#         company_mobile = request.POST.get('company_mobile')
#         company_address = request.POST.get('company_address')
#         company_pincode = request.POST.get('company_pincode')
#         company_city = request.POST.get('company_city')
#         company_state = request.POST.get('company_state')

#         try:
#             # Create a new Company_Name record
#             Company_Name.objects.create(
#                 new_company_name=new_company_name,
#                 company_gst_no=company_gst_no,
#                 company_mobile=company_mobile,
#                 company_address=company_address,
#                 company_pincode=company_pincode,
#                 company_city=company_city,
#                 company_state=company_state,
#                 company_admin_user=admin1  # Link to the fetched admin user
#             )

#             # Success message
#             messages.success(request, "Company created successfully!")
#             return redirect('desired_success_page')  # Replace with your success page

#         except Exception as e:
#             # Handle any other unexpected errors
#             messages.error(request, f"An error occurred: {str(e)}")

#     return render(request, 'company/company_add.html', {'admin_id': admin_id})

# from django.contrib import messages
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Company_Admin, Company_Name

# def balu_company_add(request, admin_id):
#     print(f"Received admin_id: {admin_id}")
#     # Fetch the Company_Admin instance based on the admin_id
#     # admin1 = get_object_or_404(Company_Admin, admin_id=admin_id)

#     if request.method == 'POST':
#         # Fetch POST data
#         new_company_name = request.POST.get('new_company_name')
#         company_gst_no = request.POST.get('company_gst_no')
#         company_mobile = request.POST.get('company_mobile')
#         company_address = request.POST.get('company_address')
#         company_pincode = request.POST.get('company_pincode')
#         company_city = request.POST.get('company_city')
#         company_state = request.POST.get('company_state')

#         try:
#             # Create a new Company_Name record
#             Company_Name.objects.create(
#                 new_company_name=new_company_name,
#                 company_gst_no=company_gst_no,
#                 company_mobile=company_mobile,
#                 company_address=company_address,
#                 company_pincode=company_pincode,
#                 company_city=company_city,
#                 company_state=company_state,
#                 # company_admin_user=admin1  # Link to the fetched admin user
#             )

#             # Success message
#             messages.success(request, "Company created successfully!")
#             return redirect('desired_success_page')  # Replace with your success page

#         except Exception as e:
#             # Handle any other unexpected errors
#             messages.error(request, f"An error occurred: {str(e)}")

#     return render(request, 'company/company_add.html', {'admin_id': admin_id})

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Company_Admin, Company_Name

# def balu_company_add(request, admin_id):
#     try:
#         admin1 = Company_Admin.objects.get(admin_id=admin_id)
#     except Company_Admin.DoesNotExist:
#         messages.error(request, f"Admin with ID {admin_id} not found!")
#         return redirect('desired_error_page')  # Replace with your error page

#     if request.method == 'POST':
#         new_company_name = request.POST.get('new_company_name')
#         company_gst_no = request.POST.get('company_gst_no')
#         company_mobile = request.POST.get('company_mobile')
#         company_address = request.POST.get('company_address')
#         company_pincode = request.POST.get('company_pincode')
#         company_city = request.POST.get('company_city')
#         company_state = request.POST.get('company_state')

#         try:
#             Company_Name.objects.create(
#                 new_company_name=new_company_name,
#                 company_gst_no=company_gst_no,
#                 company_mobile=company_mobile,
#                 company_address=company_address,
#                 company_pincode=company_pincode,
#                 company_city=company_city,
#                 company_state=company_state,
#                 company_admin_user=admin1
#             )
#             messages.success(request, "Company created successfully!")
#             return redirect('desired_success_page')  # Replace with your success page

#         except Exception as e:
#             messages.error(request, f"An error occurred: {str(e)}")

#     return render(request, 'company/company_add.html', {'admin_id': admin_id, 'admin_name': admin1.com_name})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company_Admin, Company_Name

def balu_company_add(request, admin_id):
    try:
        # Ensure the admin_id corresponds to the field in your model
        admin1 = Company_Admin.objects.get(admin_id=admin_id)  # Make sure admin_id is unique and correct
    except Company_Admin.DoesNotExist:
        messages.error(request, f"Admin with ID not found!")
        return redirect('balu_company_add')  # Replace with your error page

    if request.method == 'POST':
        new_company_name = request.POST.get('new_company_name')
        company_gst_no = request.POST.get('company_gst_no')
        company_mobile = request.POST.get('company_mobile')
        company_address = request.POST.get('company_address')
        company_pincode = request.POST.get('company_pincode')
        company_city = request.POST.get('company_city')
        company_state = request.POST.get('company_state')

        try:
            Company_Name.objects.create(
                new_company_name=new_company_name,
                company_gst_no=company_gst_no,
                company_mobile=company_mobile,
                company_address=company_address,
                company_pincode=company_pincode,
                company_city=company_city,
                company_state=company_state,
                company_admin_user=admin1  # Linking to the correct admin
            )
            messages.success(request, "Company created successfully!")
            return redirect('balu_company_add')  # Replace with your success page

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    # Pass the necessary data to the template
    return render(request, 'company/company_add.html', {'admin_id': admin_id, 'admin_name': admin1.com_name})


# from django.contrib import messages
# from django.shortcuts import render, redirect
# from .models import Company_Admin, Company_Name

# def balu_company_add(request):
#     if request.method == 'POST':
#         # Fetch POST data
#         new_company_name = request.POST.get('new_company_name')
#         company_gst_no = request.POST.get('company_gst_no')
#         company_mobile = request.POST.get('company_mobile')
#         company_address = request.POST.get('company_address')
#         company_pincode = request.POST.get('company_pincode')
#         company_city = request.POST.get('company_city')
#         company_state = request.POST.get('company_state')
#         # admin_com_name = request.POST.get('admin_com_name')  # Assuming this is the name of the admin

#         try:
#             # Fetch the Company_Admin instance based on com_name
#             admin1 = Company_Admin.objects.get(com_name=new_company_name)

#             # Create a new Company_Name record
#             Company_Name.objects.create(
#                 new_company_name=new_company_name,
#                 company_gst_no=company_gst_no,
#                 company_mobile=company_mobile,
#                 company_address=company_address,
#                 company_pincode=company_pincode,
#                 company_city=company_city,
#                 company_state=company_state,
#                 company_admin_user=admin1  # Link to the fetched admin user
#             )

#             # Success message
#             messages.success(request, "Company created successfully!")
#             return redirect('desired_success_page')  # Replace with your success page

#         except Company_Admin.DoesNotExist:
#             # If no admin is found, provide helpful error information
#             messages.error(request, "No associated admin found. Please ensure the admin name is correct.")
#         except Exception as e:
#             # Handle any other unexpected errors
#             messages.error(request, f"An error occurred: {str(e)}")

#     return render(request, 'company/company_add.html')

# def balu_company_add(request):
#     if request.method == 'POST':
#         # Get POST data
#         new_company_name = request.POST['new_company_name']
#         company_gst_no = request.POST['company_gst_no']
#         company_mobile = request.POST['company_mobile']
#         company_address = request.POST['company_address']
#         company_pincode = request.POST['company_pincode']
#         company_city = request.POST['company_city']
#         company_state = request.POST['company_state']

#         # Fetch the admin object using the admin_id stored in the session
#         company_id = request.session.get('company_id', str(uuid4()))
#         print('jjjjjjjjjjjjjjjjjjjjj')
#         admin_user = Company_Admin.objects.get(admin_id=admin_id)
#         print('qqqqqqqqqqqqqqqqqqqq')
        
        
#             # Create the new company
#         Company_Name.objects.create(
#             new_company_name=new_company_name,
#             company_gst_no=company_gst_no,
#             company_mobile=company_mobile,
#             company_address=company_address,
#             company_pincode=company_pincode,
#             company_city=company_city,
#             company_state=company_state,
#             company_admin_user=admin_user,  # Link to the fetched admin user
#         )
#         messages.success(request, "Company Created Successfully.")
#     # Fetch all companies linked to the current admin
#     # admin_id = request.session.get('admin_id')
#         company_id = request.session.get('company_id', str(uuid4()))
#         print('jjjjjjjjjjjjjjjjjjjjj')
#     # admin_user = Company_Admin.objects.get(admin_id=admin_id)
#     # print('qqqqqqqqqqqqqqqqqqqqq')
    
#         companies = Company_Name.objects.filter(company_admin_user=admin_user)
#         print('wwwwwwwwwwwwwwwwwwwww')
    
#     return render(request, 'company/company_add.html')








    
    
    
    
    
    
    
def edit_record(request, id):
    record = get_object_or_404(Record, id=id)
    data = {
        'id': record.id,
        'team_leader_name': record.team_leader_name,
        'associate_name': record.associate_name,
        'project': record.project.project_name if record.project else '',
        'plot': record.plot,
        'client_name': record.client_name,
        'mobile': record.mobile,
        'total_price': record.total_price,
        'discount': record.discount,
        'agreement_values': record.agreement_values,
        'cash_amount': record.cash_amount,
        'cheque_amount': record.cheque_amount,
        'cheque_no': record.cheque_no,
        'sum_amount': record.sum_amount,
        'remaining_amount': record.remaining_amount,
        'deal_value': record.deal_values
    }
    return JsonResponse(data)
def update_record(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        record_id = data.get('id')
        sum_amount = data.get('sum_amount')
        remaining_amount = data.get('remaining_amount')
        cash_amount = data.get('cash_amount', 0)
        cheque_amount = data.get('cheque_amount', 0)
        cheque_no = data.get('cheque_no', 0)
        deal_value = data.get('deal_value', 0)
        agreement_values = data.get('agreement_values', 0)

        # Check if the cheque number is already registered
        if cheque_no and Payment.objects.filter(cheque_number=cheque_no).exists():
            return JsonResponse({'message': 'Cheque number is already registered'}, status=400)

        if not cash_amount:
            cash_amount = 0

        # Validate cheque amount and cheque number
        try:
            cheque_amount_value = int(cheque_amount)
            if cheque_amount_value > 0 and not cheque_no:
                return JsonResponse({'message': 'Cheque number is required'}, status=400)
        except ValueError:
            return JsonResponse({'message': 'Invalid cheque amount format'}, status=400)

        total_received_amount = int(sum_amount) + int(cash_amount) + int(cheque_amount)
        total_remaining_amount = int(remaining_amount) - int(cash_amount) - int(cheque_amount)
        total_agreement_amount = int(agreement_values) - int(cash_amount)

        record = get_object_or_404(Record, id=record_id)
        current_case_amount = record.cash_amount
        current_deal_amount = record.deal_values

        # Update record fields
        record.agreement_values = total_agreement_amount
        record.cash_amount = int(current_case_amount) + int(cash_amount)
        record.deal_values = int(current_deal_amount) + int(cash_amount)
        if cheque_no:
            record.cheque_no = cheque_no
        record.sum_amount = total_received_amount
        record.remaining_amount = total_remaining_amount
        record.save()

        # Create payment record
        payment = Payment.objects.create(
            records=record,
            cheque_number=cheque_no,
            cheque_amount=cheque_amount,
            case_amount=cash_amount,
            total_amount=int(data.get('total_price', 0)),
            remaining_amount=total_remaining_amount,
            received_amount=total_received_amount
        )

        return JsonResponse({'message': 'Record updated successfully', 'status': '200'})
    
    return JsonResponse({'message': 'Invalid request method'}, status=400)


def payment_details(request, id):
    myrecord = Record.objects.filter(id=id).last()
    payment = Payment.objects.filter(records=myrecord.id).order_by('-created_date')
    return render(request, 'payment_details.html', {'payment': payment})



def home_index(request):
    users = Record.objects.all().order_by('-created_date')

    # users_list = Record.objects.all().order_by('-created_date')
    # search_query = request.GET.get('search2', '')
    # if search_query:
    #     users_list = users_list.filter(client_name__icontains=search_query) 

    # paginator = Paginator(users_list, 50)
    # page_number = request.GET.get('page')
    # users = paginator.get_page(page_number)
    
    if request.method == 'POST':
        team_leader_name = request.POST.get('team_leader_name')
        associate_name = request.POST.get('associate_name')
        project_id = request.POST.get('project')
        client_name = request.POST.get('client_name')
        mobile = request.POST.get('mobile')
        total_price = request.POST.get('total_price')
        discount = request.POST.get('discount')
        agreement_values = request.POST.get('agreement_values')
        deal_value = request.POST.get('deal_value')
        cash_amount = request.POST.get('cash_amount')
        cheque_amount = request.POST.get('cheque_amount')
        cheque_no = request.POST.get('cheque_no')
        sum_amount = request.POST.get('sum_amount')
        remaining_amount = request.POST.get('remaining_amount')

        plot_numbers = request.POST.getlist('plot')
        plot_sizes = request.POST.getlist('plot_size')

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            messages.error(request, "Project not found.")
            return redirect('index')

        if Record.objects.filter(mobile=mobile).exists():
            messages.error(request, "A customer with this mobile number already exists.")
        else:
            try:
                myrecord = Record.objects.create(
                    team_leader_name=team_leader_name,
                    associate_name=associate_name,
                    project=project,
                    plot=plot_numbers,
                    plot_size=plot_sizes,
                    client_name=client_name,
                    mobile=mobile,
                    total_price=total_price,
                    discount=discount,
                    agreement_values=agreement_values,
                    deal_values = deal_value,
                    cash_amount=cash_amount,
                    cheque_amount=cheque_amount,
                    cheque_no=cheque_no,
                    sum_amount=sum_amount,
                    remaining_amount=remaining_amount,
                )

                payment = Payment.objects.create(
                    records=myrecord,
                    cheque_number=cheque_no,
                    cheque_amount=cheque_amount,
                    case_amount=cash_amount,
                    total_amount=total_price,
                    remaining_amount=remaining_amount,
                    received_amount=sum_amount
                )

                messages.success(request, "Customer Created Successfully.")
                return redirect('index')
            except IntegrityError as e:
                messages.error(request, f"An error occurred while creating the customer: {e}. Please try again.")

    projects = Project.objects.all()

    context = {
        # 'users': users,
        'users': users,
        'projects': projects,
        'messages': messages.get_messages(request),
    }
    return render(request, 'index.html', context)

    
def export_users(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        if selected_ids:
            # Query the selected records
            users = Record.objects.filter(id__in=selected_ids).values(
                'team_leader_name', 'associate_name', 'project__project_name', 'plot', 
                'client_name', 'mobile', 'total_price', 'discount', 
                'agreement_values', 'sum_amount', 'remaining_amount', 'created_date'
            )
        else:
            # Query all records if no selection is made
            users = Record.objects.all().values(
                'team_leader_name', 'associate_name', 'project__project_name', 'plot', 
                'client_name', 'mobile', 'total_price', 'discount', 
                'agreement_values', 'sum_amount', 'remaining_amount', 'created_date'
            )

        # Create a DataFrame from the query
        df = pd.DataFrame(list(users))

        # Create the response object and set the content type for CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'

        # Write the DataFrame to the response
        df.to_csv(path_or_buf=response, index=False)

        return response
    else:
        return HttpResponse("Invalid request method.")

def get_team_leader_name(request):
    associate_name = request.GET.get('associate_name')
    try:
        record = Record.objects.get(associate_name=associate_name)
        team_leader_name = record.team_leader_name
        return JsonResponse({'team_leader_name': team_leader_name})
    except Record.DoesNotExist:
        return JsonResponse({'error': 'Associate not found'}, status=404)
    
# admin_id=request.user.id


def balu_company_index(request):
    users = InvoiceRecord.objects.all().order_by('-created_date')

    if request.method == 'POST':
        company_id = request.POST.get('company_na')
        invoice = request.POST.get('invoice')
        invoice_no = request.POST.get('invoice_no')
        product_service = request.POST.get('product_service')
        hsn_code = request.POST.get('hsn_code')
        qty = request.POST.get('qty')
        rate = request.POST.get('rate')
        amount = request.POST.get('amount')
        gst_rate = request.POST.get('gst_rate')
        total_amount = request.POST.get('total_amount')

        try:
            company = Company_Name.objects.get(id=company_id)
        except Company_Name.DoesNotExist:
            messages.error(request, "Company not found.")
            return redirect('balu_company_index')

        if InvoiceRecord.objects.filter(invoice_no=invoice_no).exists():
            messages.error(request, "An invoice with this number already exists.")
        else:
            try:
                InvoiceRecord.objects.create(
                    company_na=company,
                    invoice=invoice,
                    invoice_no=invoice_no,
                    product_service=product_service,
                    hsn_code=hsn_code,
                    qty=qty,
                    rate=rate,
                    amount=amount,
                    gst_rate=gst_rate,
                    total_amount=total_amount,
                )
                messages.success(request, "Invoice record added successfully!")
            except Exception as e:
                messages.error(request, f"An error occurred while saving the record: {str(e)}")

    projects = Company_Name.objects.all()
    context = {
        'users': users,
        'projects': projects,
        'invoice_choices': InvoiceRecord.Invoice_CHOICES,
        'gst_choices': InvoiceRecord.GST_CHOICES,
        'messages': messages.get_messages(request),
    }

    return render(request, 'company/company_index.html', context)

# def balu_company_index(request):
#     users = InvoiceRecord.objects.all().order_by('-created_date')

#     if request.method == 'POST':
#         company_id = request.POST.get('company_na')
#         invoice = request.POST.get('invoice')
#         invoice_no = request.POST.get('invoice_no')
#         product_service = request.POST.get('product_service')
#         hsn_code = request.POST.get('hsn_code')
#         qty = request.POST.get('qty')
#         rate = request.POST.get('rate')
#         amount = request.POST.get('amount')
#         gst_rate = request.POST.get('gst_rate')
#         total_amount = request.POST.get('total_amount')

#         try:
#             company = Company_Name.objects.get(id=company_id)
#         except Company_Name.DoesNotExist:
#             messages.error(request, "Company not found.")
#             return redirect('balu_company_index')

#         # Assuming 'mobile' is a required field in the model; ensure it's fetched from POST
#         mobile = request.POST.get('mobile')

#         if not mobile:
#             messages.error(request, "Mobile number is required.")
#             return redirect('balu_company_index')

#         if InvoiceRecord.objects.filter(mobile=mobile).exists():
#             messages.error(request, "A customer with this mobile number already exists.")
#         else:
#             try:
#                 InvoiceRecord.objects.create(
#                     company_na=company,  # Ensure foreign key or related field is used correctly
#                     invoice=invoice,
#                     invoice_no=invoice_no,
#                     product_service=product_service,
#                     hsn_code=hsn_code,
#                     qty=qty,
#                     rate=rate,
#                     amount=amount,
#                     gst_rate=gst_rate,
#                     total_amount=total_amount,
#                     # mobile=mobile  # Add mobile if it exists in the model
#                 )
#                 messages.success(request, "Invoice record added successfully!")
#             except Exception as e:
#                 messages.error(request, f"An error occurred while saving the record: {str(e)}")
#     projects = Company_Name.objects.all()
#     context = {
#         'users': users,
#         'projects':projects,
#         'messages': messages.get_messages(request),
#     }

#     return render(request, 'company/company_index.html', context)
