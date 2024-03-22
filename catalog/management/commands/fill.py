import json

from django.core.management import BaseCommand

from catalog.models import Category, Product, Blog


class Command(BaseCommand):
    @staticmethod
    def from_file(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    """Запись чистой базы данных"""
    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()
        # Удалите все статьи
        Blog.objects.all().delete()

        data = self.from_file("data.json")
        category_list = []
        product_list = []
        blog_list = []
        category_dict = {}
        for item in data:
            if item['model'] == 'catalog.category':
                object_category = Category(pk=item["pk"], **item["fields"])
                category_list.append(object_category)
                category_dict[item['pk']] = object_category
            elif item['model'] == 'catalog.product':
                pk = item["fields"]["category"]
                fields = item["fields"]
                fields.pop("category")
                product_list.append(Product(pk=item["pk"], category=category_dict.get(pk), **fields))
            elif item['model'] == 'catalog.blog':
                object_blog = Blog(pk=item["pk"], **item["fields"])
                blog_list.append(object_blog)

        Category.objects.bulk_create(category_list)
        Product.objects.bulk_create(product_list)
        Blog.objects.bulk_create(blog_list)
