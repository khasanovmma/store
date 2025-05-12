import os

from django.db import models


def get_product_photo_upload_path(instance: models.Model, filename: str):
    return os.path.join(
        "products", str(instance.product.id), "images", str(filename)
    ).replace("\\", "/")
