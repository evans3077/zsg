from django.core.cache import cache
from django.db import transaction

from gallery.models import SocialPost
from gallery.services.social_fetcher import SocialFetcher


def sync_platform_posts(platform, limit=3, fetch_limit=6):
    fetcher = SocialFetcher()
    fetched = fetcher.fetch_latest(platform=platform, limit=fetch_limit)
    if not fetched:
        return 0

    with transaction.atomic():
        seen_ids = []
        for row in fetched:
            SocialPost.objects.update_or_create(
                platform=platform,
                post_id=row["post_id"],
                defaults={
                    "caption": row.get("caption", ""),
                    "media_url": row.get("media_url", ""),
                    "permalink": row["permalink"],
                    "timestamp": row["timestamp"],
                    "archived": False,
                },
            )
            seen_ids.append(row["post_id"])

        if seen_ids:
            SocialPost.objects.filter(platform=platform).exclude(post_id__in=seen_ids).update(archived=True)

        latest_ids = list(
            SocialPost.objects.filter(platform=platform)
            .order_by("-timestamp")
            .values_list("id", flat=True)[:limit]
        )
        if latest_ids:
            SocialPost.objects.filter(platform=platform).exclude(id__in=latest_ids).update(archived=True)
            SocialPost.objects.filter(id__in=latest_ids).update(archived=False)

    cache.delete(f"gallery:social:{platform}:latest")
    return len(fetched)


def sync_all_social_posts():
    total = 0
    for platform in ("instagram", "tiktok"):
        total += sync_platform_posts(platform=platform, limit=3, fetch_limit=6)
    return total
