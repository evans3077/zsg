#!/usr/bin/env python
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
apps_path = os.path.join(BASE_DIR, "apps")
sys.path.insert(0, apps_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zamar_springs.settings")
django.setup()

from gallery.models import GalleryPage, GalleryImage


def create_gallery_data():
    GalleryPage.objects.update_or_create(
        pk=1,
        defaults={
            "hero_title": "Hotel Gallery",
            "hero_subtitle": (
                "A visual storytelling page covering weddings, conferences, dining, kids activities, and outdoor spaces at Zamar Springs Gardens."
            ),
            "meta_title": "Hotel Gallery - Weddings, Dining, Family Fun & Events in Machakos",
            "meta_description": (
                "Explore our beautiful gardens, wedding setups, farm-to-fork dining, kids play areas, and corporate event spaces in Machakos. See why families and event planners choose us."
            ),
            "meta_keywords": (
                "kids play area in machakos, family-friendly hotel in machakos, kids activities machakos, bouncing castle machakos, family fun zone machakos"
            ),
            "is_active": True,
        },
    )

    records = [
        {
            "title": "Wedding Garden Setup",
            "category": "weddings",
            "image_path": "/static/images/web-pictures/best-outdoor-setup-machakos.webp",
            "alt_text": "Outdoor wedding and special event setup at Zamar Springs Gardens in Machakos",
            "caption": "Premium outdoor setup for weddings and milestone events",
            "display_order": 1,
        },
        {
            "title": "Reception Table Decor",
            "category": "weddings",
            "image_path": "/static/images/web-pictures/table-setup.webp",
            "alt_text": "Wedding reception table layout at garden venue in Machakos",
            "caption": "Elegant reception table arrangement",
            "display_order": 2,
        },
        {
            "title": "Pergola Romantic Setup",
            "category": "weddings",
            "image_path": "/static/images/web-pictures/pergola-outdoor-zamar-springs-gardens.webp",
            "alt_text": "Romantic pergola setup for private celebrations at Zamar Springs Gardens",
            "caption": "Pergola space for intimate ceremonies and dinners",
            "display_order": 3,
        },
        {
            "title": "Conference Boardroom Setup",
            "category": "conferences",
            "image_path": "/static/images/gallery/conference-boardroom-setup-machakos.webp",
            "alt_text": "Professional conference boardroom setup in Machakos",
            "caption": "Executive boardroom arrangement for strategic sessions",
            "display_order": 1,
        },
        {
            "title": "Corporate Boardroom Meeting",
            "category": "conferences",
            "image_path": "/static/images/gallery/corporate-boardroom-meeting-machakos.webp",
            "alt_text": "Corporate meeting setup with premium seating in Machakos",
            "caption": "Corporate-ready boardroom visual",
            "display_order": 2,
        },
        {
            "title": "U-Shape Meeting Layout",
            "category": "conferences",
            "image_path": "/static/images/gallery/corporate-u-shape-meeting-layout-machakos.webp",
            "alt_text": "U-shape conference room setup for team workshops in Machakos",
            "caption": "Ideal layout for collaborative corporate sessions",
            "display_order": 3,
        },
        {
            "title": "Classroom Conference Event",
            "category": "conferences",
            "image_path": "/static/images/gallery/classroom-conference-event-machakos.webp",
            "alt_text": "Classroom style conference event setup in Machakos",
            "caption": "Training and seminar-ready classroom format",
            "display_order": 4,
        },
        {
            "title": "Large Event Hall Setup",
            "category": "conferences",
            "image_path": "/static/images/gallery/large-event-hall-machakos.webp",
            "alt_text": "Large corporate event hall setup in Machakos",
            "caption": "Spacious hall for conferences and team events",
            "display_order": 5,
        },
        {
            "title": "Outdoor Dining Setup",
            "category": "dining",
            "image_path": "/static/images/web-pictures/dining-setups-machakos-1.webp",
            "alt_text": "Outdoor dining setup at Zamar Springs Gardens in Machakos",
            "caption": "Farm-to-fork dining service in a garden setting",
            "display_order": 1,
        },
        {
            "title": "Open Air Dining Space",
            "category": "dining",
            "image_path": "/static/images/web-pictures/open-air-dining-machakos.webp",
            "alt_text": "Open air dining and table setup in Machakos",
            "caption": "Open dining field for groups and events",
            "display_order": 2,
        },
        {
            "title": "Dining Table Layout",
            "category": "dining",
            "image_path": "/static/images/web-pictures/outdoor-table-setup-machakos.webp",
            "alt_text": "Dining table setup for guests at Zamar Springs Gardens",
            "caption": "Prepared table arrangement for meal service",
            "display_order": 3,
        },
        {
            "title": "Gazebo Dining Experience",
            "category": "dining",
            "image_path": "/static/images/web-pictures/gazebo-setup-machakos.webp",
            "alt_text": "Gazebo dining setup at Zamar Springs Gardens in Machakos",
            "caption": "Private gazebo dining with garden views",
            "display_order": 4,
        },
        {
            "title": "Kids Outdoor Play Area",
            "category": "kids_family",
            "image_path": "/static/images/web-pictures/outdoor-kids-playarea-1.webp",
            "alt_text": "Kids outdoor play area at family-friendly hotel in Machakos",
            "caption": "Safe and active kids zone space",
            "display_order": 1,
        },
        {
            "title": "Kids Games and Activity Zone",
            "category": "kids_family",
            "image_path": "/static/images/web-pictures/kids-outdoor-games-machakos-1.webp",
            "alt_text": "Kids participating in outdoor games at Zamar Springs Gardens",
            "caption": "Structured games and family-friendly activities",
            "display_order": 2,
        },
        {
            "title": "Family Table Tennis Setup",
            "category": "kids_family",
            "image_path": "/static/images/web-pictures/table-tennis-machakos-1.webp",
            "alt_text": "Family table tennis recreation activity in Machakos",
            "caption": "Family and adult game activity space",
            "display_order": 3,
        },
        {
            "title": "Family Darts Activity",
            "category": "kids_family",
            "image_path": "/static/images/web-pictures/darts-outdoor-machakos.webp",
            "alt_text": "Family darts and outdoor recreational games at Zamar Springs Gardens",
            "caption": "Relaxed outdoor activity for adults and families",
            "display_order": 4,
        },
        {
            "title": "Garden Entrance View",
            "category": "gardens",
            "image_path": "/static/images/web-pictures/zamar-springs-gardens-entrance.webp",
            "alt_text": "Main entrance view at Zamar Springs Gardens in Machakos",
            "caption": "Welcome view of Zamar Springs Gardens",
            "display_order": 1,
        },
        {
            "title": "Muuo Grounds",
            "category": "gardens",
            "image_path": "/static/images/web-pictures/muuo-grounds-zamarsprings.webp",
            "alt_text": "Muuo garden grounds at Zamar Springs Gardens",
            "caption": "Open grounds ideal for family and event setups",
            "display_order": 2,
        },
        {
            "title": "Wendo Event Garden",
            "category": "gardens",
            "image_path": "/static/images/web-pictures/wendo-events-gardens-machakos-2.webp",
            "alt_text": "Wendo event garden setup in Machakos",
            "caption": "Large-capacity garden area for events",
            "display_order": 3,
        },
        {
            "title": "Utanu Garden View",
            "category": "gardens",
            "image_path": "/static/images/web-pictures/utanu-event-gardens-machakos.webp",
            "alt_text": "Utanu garden outdoor setup in Machakos",
            "caption": "Intimate garden space for private events",
            "display_order": 4,
        },
        {
            "title": "Pergola and Gazebo Outdoors",
            "category": "gardens",
            "image_path": "/static/images/web-pictures/pergola-outdoor-zamar-springs-gardens-1.webp",
            "alt_text": "Pergola and gazebo outdoor spaces at Zamar Springs Gardens",
            "caption": "Versatile outdoor spaces for dining and events",
            "display_order": 5,
        },
    ]

    keep_titles = []
    for item in records:
        keep_titles.append(item["title"])
        GalleryImage.objects.update_or_create(
            title=item["title"],
            defaults={**item, "is_active": True},
        )

    GalleryImage.objects.exclude(title__in=keep_titles).delete()

    print(f"Gallery page settings: {GalleryPage.objects.count()}")
    print(f"Gallery images: {GalleryImage.objects.count()}")


if __name__ == "__main__":
    create_gallery_data()
