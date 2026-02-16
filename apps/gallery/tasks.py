from celery import shared_task

from gallery.services.social_sync import sync_all_social_posts


@shared_task(name="gallery.sync_social_posts")
def sync_social_posts_task():
    return sync_all_social_posts()
