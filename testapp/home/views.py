from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Medicine  
from django.core.paginator import Paginator
from django.http import JsonResponse

@login_required
def welcome(request):
    medicines = Medicine.objects.all()  # Fetch all rows
    paginator = Paginator(medicines, 10)  # Show 10 medicines per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the corresponding page

    print(page_obj)  # Add this to check if page_obj is correct

    return render(request, 'home/inventory.html', {'page_obj': page_obj})


def stock_analysis(request):
    # Your logic here
    return render(request, 'stock_analysis.html')   

def alternate_medicine(request):
    # Your logic here
    return render(request, 'alternate_medicine.html')

def upload_prescription(request):
    # Your logic to handle the prescription upload goes here
    return render(request, 'upload_prescription.html')

def upload_medicine_image(request):
    # Your logic to handle image upload goes here
    return render(request, 'upload_medicine_image.html')

def side_effects(request):
    # Your logic for handling side effects page
    return render(request, 'side_effects.html')

def dashboard(request):
    # Your logic for handling dashboard page
    return render(request, 'dashboard.html')