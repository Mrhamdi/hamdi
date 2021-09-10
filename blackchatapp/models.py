

from django.db import models

# Create your models here.
def product_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/actual/<filename>
    return 'actual/{0}'.format(filename)

def product_thumb_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/thumb/<filename>
    return 'thumb/{0}'.format(filename)


class Product(models.Model):
    product_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    product_image = models.FileField(upload_to=product_image_path, max_length=100)
    product_thumb = models.FileField(upload_to=product_thumb_path, max_length=100)

    def __str__(self):
        return self.title

# Create your models here.
