from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Book


@receiver(post_delete, sender=Book)
def delete_cover_img_pn_book_delete(sender, instance: Book, **kwargs):
    if instance.cover_image:
        instance.cover_image.delete(save=False)


@receiver(pre_save, sender=Book)
def delete_old_cover_image_on_update(sender, instance: Book, **kwargs):
    if not instance.pk:
        return #when book does not exist yet in the db

    try:
        old_book = Book.objects.get(pk=instance.pk)
        if old_book.cover_image and old_book.cover_image.name != instance.cover_image.name:
            old_book.cover_image.delete(save=False)

    except Book.DoesNotExist:
        return










