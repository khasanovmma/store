from django.db import models


class CreatedAtAbstractModel(models.Model):
    created_at = models.DateTimeField(
        "Дата создания", auto_now_add=True, null=True
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class UpdatedAtAbstractModel(models.Model):
    updated_at = models.DateTimeField(
        "Дата обновления", auto_now=True, null=True
    )

    class Meta:
        abstract = True


class CreatedUpdatedAbstractModel(
    CreatedAtAbstractModel, UpdatedAtAbstractModel
):
    class Meta:
        abstract = True
        ordering = ["-created_at"]
