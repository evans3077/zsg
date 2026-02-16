from django.core.management.base import BaseCommand

from gallery.services.social_sync import sync_all_social_posts


class Command(BaseCommand):
    help = "Fetches and syncs latest social posts (Instagram/TikTok)."

    def handle(self, *args, **options):
        total = sync_all_social_posts()
        self.stdout.write(self.style.SUCCESS(f"Synced social posts. Processed records: {total}"))
