import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import HomePageSettings, Feature, Service

def home_view(request):
    # Get or create settings
    settings = HomePageSettings.objects.first()
    if not settings:
        settings = HomePageSettings.objects.create()
    
    # Get active features
    features = Feature.objects.filter(is_active=True).order_by('display_order')[:4]
    
    # Get active services
    services = Service.objects.filter(is_active=True).order_by('display_order')[:6]
    
    context = {
        'settings': settings,
        'features': features,
        'services': services,
    }
    
    return render(request, 'home/index.html', context)


def privacy_policy_view(request):
    return render(request, "home/privacy_policy.html")


def outdoor_events_view(request):
    absolute_base = f"{request.scheme}://{request.get_host()}"
    page_url = request.build_absolute_uri()

    seo = {
        "title": "Outdoor Activities in Machakos | Hiking, Cycling & Nature Trails",
        "description": (
            "Discover outdoor activities in Machakos at Zamar Springs Gardens including guided hiking in Mua Hills, "
            "organized cycling routes and free nature trails in a secure garden setting near Nairobi."
        ),
        "keywords": (
            "outdoor activities Machakos, hiking in Mua Hills, cycling routes Machakos, nature trails Machakos, "
            "outdoor events near Nairobi, corporate team building Machakos"
        ),
    }

    hero = {
        "title": "Outdoor Activities & Nature Experiences in Machakos",
        "subtitle": "Experience guided hiking, scenic cycling and serene nature trails at Zamar Springs Gardens.",
        "cta_label": "Plan Your Outdoor Event",
        "cta_target": "#outdoor-inquiry",
        "image": f"{absolute_base}/static/images/web-pictures/garden-walkway-zamarsprings.webp",
        "image_alt": "Outdoor activities at Zamar Springs Gardens in Machakos",
    }

    nature_trail = {
        "title": "Nature Trails in Machakos",
        "description": (
            "At Zamar Springs Gardens, we host peaceful and secure nature trails in Machakos within our beautifully "
            "maintained garden environment. The trail is fully fenced, pollution-free and designed to offer a calm "
            "escape from busy urban surroundings.\n\nEach round of the trail covers approximately 800 meters, making "
            "it suitable for casual walkers, families and small groups. The environment is serene, safe and surrounded "
            "by natural greenery, ideal for relaxation and light fitness activities.\n\nThe nature trail is free of "
            "charge. Visitors are only required to purchase a bottle of water or any refreshment of their choice from "
            "our facility. Ample parking is available on-site for convenience."
        ),
        "features": [
            "800m per round",
            "Fully fenced and secure",
            "Pollution-free environment",
            "Free access (with refreshment purchase)",
            "Ample parking",
        ],
        "cta_label": "Visit for a Nature Walk",
        "cta_target": "tel:+254112394681",
        "image": f"{absolute_base}/static/images/web-pictures/zamar-springs-gardens-entrance-1.webp",
        "image_alt": "Nature trail inside Zamar Springs Gardens Machakos",
    }

    guided_hiking = {
        "title": "Guided Hiking in Mua Hills, Machakos",
        "description": (
            "We organize guided hiking experiences through the scenic Mua Hills in Machakos. Each hiking session is led "
            "by a trained and qualified guide to ensure safety, navigation and an engaging outdoor experience.\n\nThe "
            "hiking journey begins from Zamar Springs Gardens and extends through the beautiful terrain of Mua Hills. "
            "For safety assurance, we also provide a qualified first aider to accompany hiking groups.\n\nThis "
            "experience is ideal for corporate teams, fitness groups, families and adventure seekers."
        ),
        "distances": ["5 km", "10 km", "14 km"],
        "note": "Call to request for a customized quote.",
        "cta_label": "Request a Hiking Quote",
        "cta_target": "#outdoor-inquiry",
        "image": f"{absolute_base}/static/images/web-pictures/muuo-grounds-zamarsprings.webp",
        "image_alt": "Guided hiking in Mua Hills Machakos",
    }

    organized_cycling = {
        "title": "Organized Cycling Routes in Machakos",
        "description": (
            "Zamar Springs Gardens offers organized cycling experiences both within our garden premises and along scenic "
            "routes around Machakos.\n\nDistances range from 20 km to 40 km depending on the selected route.\n\n"
            "Participants are required to bring their own bicycles. Our team includes trained guides and qualified first "
            "aiders to ensure a safe and well-coordinated cycling experience.\n\nIdeal for fitness clubs, corporate "
            "wellness programs and cycling enthusiasts."
        ),
        "routes": [
            "Zamar to Vota and back",
            "Zamar to Vota to Mombasa Road and back",
            "Custom cycling routes upon request",
        ],
        "cta_label": "Plan a Cycling Event",
        "cta_target": "#outdoor-inquiry",
        "image": f"{absolute_base}/static/images/web-pictures/outdoor-table-setup-machakos.webp",
        "image_alt": "Organized cycling route from Zamar Springs",
    }

    internal_links = [
        {
            "label": "Explore Dining Experiences",
            "description": "Farm-to-fork dining spaces and menu experiences after your activity.",
            "url": "/dining/",
        },
        {
            "label": "View Gardens & Event Spaces",
            "description": "Private and general garden event setups for celebrations and groups.",
            "url": "/gardens/",
        },
        {
            "label": "Corporate Retreats in Machakos",
            "description": "Combine conferences and outdoor experiences for team retreats.",
            "url": "/conferences/",
        },
        {
            "label": "Contact Zamar Springs",
            "description": "Talk to our team directly for immediate assistance.",
            "url": "/#site-contact",
        },
    ]

    schema_payloads = {
        "tourist_attraction": json.dumps(
            {
                "@context": "https://schema.org",
                "@type": "TouristAttraction",
                "name": "Outdoor Activities at Zamar Springs Gardens",
                "description": seo["description"],
                "url": page_url,
                "touristType": ["Families", "Corporate teams", "Hiking groups", "Cycling enthusiasts"],
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Machakos",
                    "addressRegion": "Machakos County",
                    "addressCountry": "KE",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": -1.532478,
                    "longitude": 37.1868857,
                },
                "isAccessibleForFree": True,
            }
        ),
        "event_venue": json.dumps(
            {
                "@context": "https://schema.org",
                "@type": "EventVenue",
                "name": "Zamar Springs Gardens Outdoor Events",
                "url": page_url,
                "description": "Outdoor event venue and guided activity base in Machakos near Mua Hills and Nairobi.",
                "telephone": "+254112394681",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Kithini",
                    "addressLocality": "Machakos",
                    "addressCountry": "KE",
                },
            }
        ),
    }

    context = {
        "hero": hero,
        "nature_trail": nature_trail,
        "guided_hiking": guided_hiking,
        "organized_cycling": organized_cycling,
        "internal_links": internal_links,
        "seo": seo,
        "schema_payloads": schema_payloads,
    }
    return render(request, "home/outdoor_events.html", context)


def our_farm_view(request):
    sections = [
        {
            "title": "Our Farm",
            "description": "Foundational information about our farm operations will be added here.",
            "icon": "fas fa-seedling",
        },
        {
            "title": "Flower Nursery",
            "description": "Foundational information about our flower nursery will be added here.",
            "icon": "fas fa-spa",
        },
    ]
    return render(request, "home/our_farm.html", {"sections": sections})


def careers_view(request):
    return render(request, "home/careers.html")


def terms_of_service_view(request):
    return render(request, "home/terms_of_service.html")


def site_map_view(request):
    sections = [
        {
            "title": "Main Pages",
            "links": [
                {"label": "Home", "url": "/"},
                {"label": "Conferences", "url": "/conferences/"},
                {"label": "Gardens & Events", "url": "/gardens/"},
                {"label": "Outdoor Events", "url": "/outdoor-events/"},
                {"label": "Our Farm", "url": "/our-farm/"},
                {"label": "Dining", "url": "/dining/"},
                {"label": "Kids & Family", "url": "/kids-family/"},
                {"label": "Gallery", "url": "/gallery/"},
            ],
        },
        {
            "title": "Important Pages",
            "links": [
                {"label": "Privacy Policy", "url": "/privacy-policy/"},
                {"label": "Terms of Service", "url": "/terms-of-service/"},
                {"label": "Careers", "url": "/careers/"},
                {"label": "XML Sitemap", "url": "/sitemap.xml"},
            ],
        },
    ]
    return render(request, "home/sitemap.html", {"sections": sections})


def robots_txt_view(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: "
        f"{request.scheme}://{request.get_host()}/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")
