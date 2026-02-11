from django.shortcuts import render
from .models import GalleryPage, GalleryImage


SECTION_CONTENT = {
    "weddings": {
        "title": "Weddings & Special Events",
        "description": (
            "Garden ceremonies, romantic pergola moments, and premium reception layouts. "
            "Zamar Springs Gardens is built for memorable weddings and milestone celebrations in Machakos."
        ),
    },
    "conferences": {
        "title": "Conferences & Corporate Events",
        "description": (
            "Professional conference setups with natural surroundings. "
            "Ideal for executive meetings, team sessions, and corporate functions."
        ),
    },
    "dining": {
        "title": "Dining & Farm-to-Fork Experience",
        "description": (
            "Visual highlights from our kitchen, coffee service, platter setups, and grill offering. "
            "Fresh ingredients and strong presentation quality are central to the dining experience."
        ),
    },
    "kids_family": {
        "title": "Kids & Family Fun",
        "description": (
            "A safe and energetic environment for children and family activities. "
            "Play-focused setups support active fun, supervised engagement, and quality bonding time."
        ),
    },
    "gardens": {
        "title": "Gardens & Outdoor Spaces",
        "description": (
            "Landscaped gardens, gazebos, pergola scenes, and open-air setups for events and leisure. "
            "A premium outdoor atmosphere for photos, gatherings, and evening experiences."
        ),
    },
}


def overview(request):
    page_settings = GalleryPage.objects.filter(is_active=True).first()
    if not page_settings:
        page_settings = GalleryPage.objects.create(
            hero_title="Hotel Gallery",
            hero_subtitle=(
                "A visual story of weddings, conferences, dining, family fun, and gardens at Zamar Springs Gardens."
            ),
            meta_title="Hotel Gallery - Weddings, Dining, Family Fun & Events in Machakos",
            meta_description=(
                "Explore our beautiful gardens, wedding setups, farm-to-fork dining, kids play areas, and corporate event spaces in Machakos. See why families and event planners choose us."
            ),
            meta_keywords=(
                "hotel gallery machakos, wedding gallery machakos, family hotel photos, conference venue photos, farm to fork dining images"
            ),
        )

    images = GalleryImage.objects.filter(is_active=True).order_by("category", "display_order")
    grouped_sections = []
    for section_key, data in SECTION_CONTENT.items():
        section_images = [img for img in images if img.category == section_key]
        grouped_sections.append(
            {
                "key": section_key,
                "title": data["title"],
                "description": data["description"],
                "images": section_images,
            }
        )

    return render(
        request,
        "gallery/overview.html",
        {
            "page_settings": page_settings,
            "grouped_sections": grouped_sections,
        },
    )
