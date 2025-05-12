from modeltranslation.translator import TranslationOptions, register

from product.models import Category, Product


class BaseTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru",)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description")
    required_languages = ("ru",)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
    required_languages = ("ru",)
