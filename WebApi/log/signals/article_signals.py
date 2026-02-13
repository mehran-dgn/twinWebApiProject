from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Article
from log.helpers.log_helpers import create_log

@receiver(post_save, sender=Article)
def article_post_save(sender, instance, created, **kwargs):
    if created:
        create_log(
            action="CREATE_ARTICLE",
            content_type="Article",
            object_id=instance.id,
            message=f"Article '{instance.Title}' created"
        )
    else:
        create_log(
            action="UPDATE_ARTICLE",
            content_type="Article",
            object_id=instance.id,
            message=f"Article '{instance.Title}' updated"
        )
