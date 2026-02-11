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
            "title": "Outdoor Wedding Reception Layout",
            "category": "weddings",
            "image_path": "/static/images/gallery/wedding-reception-layout-machakos.webp",
            "alt_text": "Outdoor wedding ceremony setup in garden venue in Machakos",
            "caption": "Elegant reception arrangement for wedding guests",
            "display_order": 1,
        },
        {
            "title": "Garden Wedding Ceremony Setup",
            "category": "weddings",
            "image_path": "/static/images/gallery/garden-wedding-ceremony-machakos.webp",
            "alt_text": "Garden wedding ceremony arrangement at Zamar Springs Gardens in Machakos",
            "caption": "Ceremony-ready wedding space in landscaped gardens",
            "display_order": 2,
        },
        {
            "title": "Romantic Pergola Event Setup",
            "category": "weddings",
            "image_path": "/static/images/gallery/presentation-room-setup-machakos.webp",
            "alt_text": "Romantic pergola event setup for special celebrations in Machakos",
            "caption": "Pergola-style romantic setup for private events",
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
            "title": "Farm to Fork Dining Presentation",
            "category": "dining",
            "image_path": "/static/images/gallery/indoor-corporate-conference-machakos.webp",
            "alt_text": "Dining presentation setup for farm-to-fork experience in Machakos",
            "caption": "Premium dining arrangement at Zamar Springs Gardens",
            "display_order": 1,
        },
        {
            "title": "BBQ and Choma Zone Highlights",
            "category": "dining",
            "image_path": "/static/images/gallery/outdoor-corporate-event-machakos.webp",
            "alt_text": "BBQ grill and choma zone setup at Zamar Springs Gardens",
            "caption": "Open grill atmosphere for social dining",
            "display_order": 2,
        },
        {
            "title": "Platter and Drink Board",
            "category": "dining",
            "image_path": "/static/images/gallery/kids-bouncing-castle-machakos.jpg",
            "alt_text": "Platter menu and drink options at Zamar Springs Gardens in Machakos",
            "caption": "Menu and platter highlights from current offerings",
            "display_order": 3,
        },
        {
            "title": "Kids Bouncing Castle",
            "category": "kids_family",
            "image_path": "/static/images/gallery/kids-bouncing-castle-machakos.jpg",
            "alt_text": "Kids playing on bouncing castle at family hotel in Machakos",
            "caption": "Safe and active play area for children",
            "display_order": 1,
        },
        {
            "title": "Family Play and Activity Area",
            "category": "kids_family",
            "image_path": "/static/images/gallery/team-building-conference-space-machakos.webp",
            "alt_text": "Family activity setup with games at Zamar Springs Gardens",
            "caption": "Family bonding activities in open spaces",
            "display_order": 2,
        },
        {
            "title": "Kids Zone Play Setup",
            "category": "kids_family",
            "image_path": "/static/images/gallery/presentation-room-setup-machakos.webp",
            "alt_text": "Kids zone setup with supervised play activities in Machakos",
            "caption": "Structured kids zone environment",
            "display_order": 3,
        },
        {
            "title": "Garden Outdoor Seating",
            "category": "gardens",
            "image_path": "/static/images/gallery/garden-wedding-ceremony-machakos.webp",
            "alt_text": "Outdoor seating arrangement in landscaped garden venue in Machakos",
            "caption": "Garden ambiance for outdoor gatherings",
            "display_order": 1,
        },
        {
            "title": "Pergola and Gazebo Atmosphere",
            "category": "gardens",
            "image_path": "/static/images/gallery/wedding-reception-layout-machakos.webp",
            "alt_text": "Pergola and gazebo setup in outdoor event venue in Machakos",
            "caption": "Premium outdoor setup for events and leisure",
            "display_order": 2,
        },
        {
            "title": "Sunset and Open Space Experience",
            "category": "gardens",
            "image_path": "/static/images/gallery/outdoor-corporate-event-machakos.webp",
            "alt_text": "Open outdoor event space with scenic garden views in Machakos",
            "caption": "Versatile open-air venue visual",
            "display_order": 3,
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

