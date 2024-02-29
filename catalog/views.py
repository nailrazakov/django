from django.shortcuts import render

from catalog.models import Product, ContactDetails


# Create your views here.
def contacts(request):
    try:
        contact_info = ContactDetails.objects.all()[0]
    except:
        contact_info = []
    context = {
        'object_list': contact_info
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Имя: {name} - e-mail: {email}\nСообщение: {message}")
    return render(request, 'catalog/contacts.html', context)


def main(request):
    #  выборка последних пяти товаров
    product_list = Product.objects.all().order_by("time_create")[:5]
    context = {
       'object_list': product_list
    }
    return render(request, 'catalog/main.html', context)
