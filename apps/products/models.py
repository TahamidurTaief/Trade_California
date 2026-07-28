from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    icon_svg = models.TextField(blank=True, help_text="SVG code for main categories")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Categories"
        
    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(400, 400)],
                                     format='JPEG',
                                     options={'quality': 85})
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Product #{self.id}"
        
    @property
    def category_ids(self):
        """Returns comma-separated IDs of this category and all its ancestors for filtering."""
        ids = []
        cat = self.category
        while cat:
            ids.append(str(cat.id))
            cat = cat.parent
        return ",".join(ids)
