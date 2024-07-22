import os
from django.conf import settings
from PIL import Image
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    descricao = models.TextField()
    image = models.ImageField(
        upload_to='product_images/%Y/%m', blank=False, null=True)
    slug = models.SlugField(unique=True)
    price_mkt = models.FloatField(default=0)
    price_mkt_promo = models.FloatField(default=0)
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variation'),
            ('S', 'Simple'),
        )
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().sabe(*args, **kwargs)

        MAX_IMAGE_SIZE = 800

        if self.image:
            self.resize_image(self.image, MAX_IMAGE_SIZE)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_height)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name

    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'
