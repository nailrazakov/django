from django.shortcuts import render

from catalog.models import Product, ContactDetails, Category


# Create your views here.
def contacts(request):
    """Контролер страницы с контактами если введены данные и обратной связью"""
    try:
        contact_info = ContactDetails.objects.all()[0]
    except:
        contact_info = []
    context = {
        'object_list': contact_info,
        'actions': "Контактная информация"
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Имя: {name} - e-mail: {email}\nСообщение: {message}")
    return render(request, 'catalog/contacts.html', context)


def main(request):
    """Контролер главной страницы с выводом нескольких продуктов"""
    #  выборка последних пяти товаров
    product_list = Product.objects.all().order_by("time_create")[:5]
    context = {
        'object_list': product_list,
        'actions': "Главное меню"
    }
    return render(request, 'catalog/main.html', context)


def cards(request, product_id):
    """Контролер страницы продукта выбранного по pk"""
    product_list = Product.objects.get(pk=product_id)
    context = {
        'object_list': product_list,
        'title': product_list.category,
        'product_id': product_id,
        'actions': "Каталог товаров"
    }
    return render(request, 'catalog/cards.html', context=context)


def card(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'object_list': product_list,
        'category': category_list,
        'title': 'CARD LIST',
    }
    return render(request, 'catalog/card.html', context=context)
