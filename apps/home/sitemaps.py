from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from conferences.models import ConferenceCategory, ConferenceRoom
from dining.models import DiningSpace
from gardens.models import Garden


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            "home:index",
            "conferences:overview",
            "conferences:packages",
            "gardens:overview",
            "gardens:gardens_list",
            "gardens:weddings",
            "gardens:private_events",
            "gardens:general_events",
            "home:outdoor_events",
            "dining:overview",
            "dining:menu",
            "dining:farm_to_fork",
            "kids:overview",
            "gallery:overview",
            "home:careers",
            "home:privacy_policy",
            "home:terms_of_service",
            "home:sitemap_page",
        ]

    def location(self, item):
        return reverse(item)


class ConferenceCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ConferenceCategory.objects.filter(is_active=True)

    def location(self, item):
        return reverse("conferences:category_detail", args=[item.slug])


class ConferenceRoomSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ConferenceRoom.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return reverse("conferences:room_detail", args=[item.slug])


class GardenSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Garden.objects.filter(is_active=True)

    def location(self, item):
        return reverse("gardens:garden_detail", args=[item.slug])


class DiningSpaceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return DiningSpace.objects.filter(is_active=True)

    def location(self, item):
        return reverse("dining:space_detail", args=[item.slug])


sitemaps = {
    "static": StaticViewSitemap,
    "conference_categories": ConferenceCategorySitemap,
    "conference_rooms": ConferenceRoomSitemap,
    "gardens": GardenSitemap,
    "dining_spaces": DiningSpaceSitemap,
}
