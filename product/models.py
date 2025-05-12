from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django_minio_backend import MinioBackend
from mptt.models import MPTTModel, TreeForeignKey

from core.models import CreatedUpdatedAbstractModel, UpdatedAtAbstractModel
from product.upload_paths import get_product_photo_upload_path


class Category(MPTTModel, CreatedUpdatedAbstractModel):
    name = models.CharField("Наименование", max_length=256, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField("Активен", default=True)
    order = models.PositiveIntegerField("Порядок", default=0)
    parent = TreeForeignKey(
        "self",
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Родительская категория",
    )

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["order"]


class Brand(CreatedUpdatedAbstractModel):
    name = models.CharField("Наименование", max_length=256, unique=True)
    short_name = models.CharField(
        "Краткое название", max_length=50, null=True, blank=True
    )
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Product(CreatedUpdatedAbstractModel):
    name = models.CharField("Наименование", max_length=256)
    article = models.CharField(
        "Артикул", max_length=256, null=True, blank=True, editable=False
    )
    description = RichTextField("Описание")
    quantity = models.PositiveIntegerField("Количество")
    is_active = models.BooleanField("Активен", default=True)
    barcode = models.CharField("Штрих-код", max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Категория"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, verbose_name="Бренд"
    )

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductPrice(CreatedUpdatedAbstractModel):
    product = models.OneToOneField(
        Product, on_delete=models.PROTECT, verbose_name="Продукт"
    )
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.product} - {self.price}"

    class Meta:
        verbose_name = "Цена продукта"
        verbose_name_plural = "Цены продуктов"


class ProductImage(UpdatedAtAbstractModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    photo = models.ImageField(
        verbose_name="Картина",
        storage=MinioBackend(
            bucket_name=settings.MINIO_BUCKET_NAME,
        ),
        upload_to=get_product_photo_upload_path,
        null=True,
        blank=True,
    )
    order = models.PositiveIntegerField("Порядок", default=0)

    def __str__(self):
        return f"{self.product.name} - {self.photo.name}"

    def photo_preview(self):
        from django.utils.html import format_html

        if self.photo:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit:contain;" />',
                self.photo.url,
            )
        return "No image"

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"
        ordering = ["order"]
