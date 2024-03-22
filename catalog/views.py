from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, ContactDetails, Category, Blog


class ProductTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
    try:
        contact_info = ContactDetails.objects.all()[0]
    except:
        contact_info = []
    extra_context = {
        'object': contact_info,
        'actions': "Контактная информация"
    }


# Create your views here.
# def contacts(request):
#     """Контролер страницы с контактами если введены данные и обратной связью"""
#     try:
#         contact_info = ContactDetails.objects.all()[0]
#     except:
#         contact_info = []
#     context = {
#         'object_list': contact_info,
#         'actions': "Контактная информация"
#     }
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f"Имя: {name} - e-mail: {email}\nСообщение: {message}")
#     return render(request, 'catalog/contacts.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/main.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/cards.html'


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'is_published', 'view_count', ]
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        """Добавляет slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'is_published', 'view_count', ]
    # success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        """Добавляет slug"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')
