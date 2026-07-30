from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OfficeLocation
from .forms import ContactForm

def contact(request):
    locations = OfficeLocation.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        # Check if product is passed in query params
        initial = {}
        if 'product' in request.GET:
            initial['message'] = f"I am interested in {request.GET['product']}. Please send more information."
        form = ContactForm(initial=initial)

    return render(request, "contact/contact.html", {"locations": locations, "form": form})

def connect(request, role):
    valid_roles = {
        'buyer': 'Buyer',
        'supplier': 'U.S. Supplier',
        'partner': 'Business Partnership',
        'distributor': 'Distributorship'
    }
    
    if role not in valid_roles:
        return redirect('contact')
        
    title = valid_roles[role]
    
    if request.method == 'POST':
        from .models import ConnectSubmission
        data = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}
        ConnectSubmission.objects.create(role=role, data=data)
        messages.success(request, 'Your submission has been received successfully!')
        return redirect('contact')
        
    return render(request, "contact/connect.html", {"role": role, "title": title})
