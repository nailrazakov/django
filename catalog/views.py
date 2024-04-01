from django import forms
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, ContactDetails, Blog, Version


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


class ProductListView(ListView):
    """Класс представления списка продуктов"""
    model = Product
    template_name = 'catalog/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        for product in products:
            product.version = product.versions.filter(is_active=1).first()

        context['actions'] = "Выберете товар"
        context['object_list'] = products
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:main')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        is_active_count = 0
        context_data = self.get_context_data()
        formset = context_data['formset']
        for form_ in formset.forms:
            if 'checked' in str(form_['is_active']):
                is_active_count += 1
        if is_active_count > 1:
            raise forms.ValidationError('Может быть только одна активная версия')
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:main')


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'actions': "Статьи"
    }

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
