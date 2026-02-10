# create_gardens_data.py
#!/usr/bin/env python
import os
import django
import sys

# Build paths inside the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
apps_path = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, apps_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zamar_springs.settings')
django.setup()

from gardens.models import GardensPage, Garden, EventType

def create_sample_data():
    # Create Gardens Page
    page, created = GardensPage.objects.get_or_create(
        defaults={
            'hero_title': 'Gardens & Events',
            'hero_subtitle': 'Beautiful garden venues for weddings, events, and celebrations in a serene, non-alcoholic environment',
            'intro_text': 'From intimate garden weddings to large corporate events, our beautifully maintained gardens provide the perfect backdrop for your special occasions.',
            'why_title': 'Why Choose Our Gardens',
            'why_subtitle': 'Experience the perfect blend of natural beauty and professional event hosting',
            'meta_title': 'Gardens & Events | Zamar Springs Gardens',
            'meta_description': 'Beautiful garden venues for weddings, birthdays, corporate events and photoshoots in Machakos',
            'meta_keywords': 'garden weddings, event venues, birthday parties, photoshoots, machakos',
            'is_active': True,
        }
    )
    
    # Create Gardens
    gardens_data = [
        {
            'name': 'Muuo Garden',
            'slug': 'muuo-garden',
            'garden_type': 'main',
            'capacity': 80,
            'description': 'Our smallest garden with kids playing zone. Perfect for families and small groups.',
            'area': '2000 sqm',
            'special_features': 'Central water feature, stone pathways, romantic lighting',
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Wendo Garden',
            'slug': 'wendo-garden',
            'garden_type': 'main',
            'capacity': 1000,
            'description': 'Spacious garden with open lawns and covered pavilion. Ideal for large receptions and outdoor events.',
            'area': '2500 sqm',
            'special_features': 'Built-in stage, permanent canopy, fairy lights',
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Utanu Garden',
            'slug': 'utanu-garden',
            'garden_type': 'main',
            'capacity': 300,
            'description': 'Intimate garden with cozy corners and beautiful flower beds. Perfect for smaller weddings and family events.',
            'area': '1500 sqm',
            'special_features': 'water fallview',
            'is_featured': True,
            'display_order': 3,
        },
    ]
    
    for garden_data in gardens_data:
        garden, created = Garden.objects.get_or_create(
            slug=garden_data['slug'],
            defaults={
                **garden_data,
                'has_covered_area': True,
                'has_power': True,
                'has_lighting': True,
                'has_restrooms': True,
                'has_parking': True,
                'is_wheelchair_accessible': True,
                'is_active': True,
            }
        )
    
    # Create Event Types - Weddings
    wedding_events = [
        {
            'name': 'Garden Wedding',
            'slug': 'garden-wedding',
            'category': 'wedding',
            'icon': 'fas fa-ring',
            'description': 'Romantic garden wedding ceremony surrounded by beautiful flowers and nature',
            'detailed_description': 'Exchange your vows in our beautifully manicured gardens. Includes ceremony setup, seating, sound system (upon request), and floral arrangements.',
            'includes': 'Garden ceremony setup\nSeating for guests\nSound system (upon request)\nFloral arch decoration\nTents\nDining Tables & chairs\nCatering coordination\nDecor consultation',
            'starting_price': 1000000.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Reception Wedding',
            'slug': 'reception-wedding',
            'category': 'wedding',
            'icon': 'fas fa-glass-cheers',
            'description': 'Complete wedding reception package with dining and celebration facilities',
            'detailed_description': 'Celebrate your union with friends and family. Includes reception area, dining setup, dance floor, and catering coordination.',
            'includes': 'Reception venue setup\nGuest tables & chairs\nFood Setup\nDance floor\nSound (upon request)\nCatering coordination\nDecor consultation',
            'starting_price': 80000.00,
            'is_featured': True,
            'display_order': 2,
        },
    ]
    
    for event_data in wedding_events:
        event, created = EventType.objects.get_or_create(
            slug=event_data['slug'],
            defaults=event_data
        )
    
    # Create Event Types - Private Events
    private_events = [
        {
            'name': 'Birthday Parties',
            'slug': 'birthday-parties',
            'category': 'private',
            'icon': 'fas fa-birthday-cake',
            'description': 'Celebrate birthdays in a beautiful garden setting for all ages',
            'detailed_description': 'Make birthdays memorable with our garden parties. Perfect for children and adults alike.',
            'includes': 'Garden venue\nTables & chairs setup\nCake table setup\nGames area',
            'starting_price': 5000.00,
            'display_order': 2,
        },
        {
            'name': 'Picnics',
            'slug': 'picnics',
            'category': 'private',
            'icon': 'fas fa-basketball-ball',
            'description': 'Family and group picnics in our serene garden environment',
            'detailed_description': 'Enjoy quality time with family and friends in our beautiful gardens.',
            'includes': 'Designated picnic area\nPicnic mats & blankets\nShaded seating\nGames equipment',
            'starting_price': 10000.00,
            'display_order': 1,
        },
        {
            'name': 'Graduation Parties',
            'slug': 'graduation-parties',
            'category': 'private',
            'icon': 'fas fa-graduation-cap',
            'description': 'Celebrate academic achievements with friends and family',
            'detailed_description': 'Honor graduates in style with our graduation party packages.',
            'includes': 'Venue setup\nGraduation-themed decor\nSound system (upon request)\nPhoto backdrop\nCatering coordination\nPhoto Booth',
            'starting_price': 15000.00,
            'display_order': 4,
        },
        {
            'name': 'Engagements',
            'slug': 'engagements',
            'category': 'private',
            'icon': 'fas fa-heart',
            'description': 'Romantic engagement celebrations in beautiful garden settings',
            'detailed_description': 'Propose or celebrate your engagement in a romantic garden setting.',
            'includes': 'Private garden area\nRomantic decoration\nFloral arrangements\nPhotography spots\nChampagne setup',
            'starting_price': 5000.00,
            'display_order': 3,
        },
        {
            'name': 'Anniversaries',
            'slug': 'anniversaries',
            'category': 'private',
            'icon': 'fas fa-glass-cheers',
            'description': 'Celebrate milestones and anniversaries with loved ones',
            'detailed_description': 'Mark your special anniversaries in a memorable garden setting.',
            'includes': 'Venue decoration\nSpecial seating arrangement\nSound system (upon request)\nCake table',
            'starting_price': 8000.00,
            'display_order': 5,
        },
    ]
    
    for event_data in private_events:
        event, created = EventType.objects.get_or_create(
            slug=event_data['slug'],
            defaults=event_data
        )
    
    # Create Event Types - General Events
    general_events = [
        {
            'name': 'Photoshoots',
            'slug': 'photoshoots',
            'category': 'general',
            'icon': 'fas fa-camera',
            'description': 'Professional photoshoots in various beautiful garden settings',
            'detailed_description': 'Perfect location for fashion, family, maternity, and product photoshoots.',
            'includes': 'Multiple garden locations\nChanging room\nPower outlets\nParking for crew\nFlexible timing',
            'starting_price': 18000.00,
            'display_order': 2,
        },
        {
            'name': 'Group Chamas',
            'slug': 'group-chamas',
            'category': 'general',
            'icon': 'fas fa-users',
            'description': 'Regular meetings for groups and investment clubs',
            'detailed_description': 'Comfortable and private spaces for group meetings and gatherings.',
            'includes': 'Private meeting area\nTables & chairs\nWhiteboard\nTea/coffee service\nSecure environment',
            'starting_price': 10000.00,
            'display_order': 3,
        },
        {
            'name': 'Team Building',
            'slug': 'team-building',
            'category': 'general',
            'icon': 'fas fa-handshake',
            'description': 'Corporate team building activities and retreats',
            'detailed_description': 'Boost team morale with outdoor activities and games in our gardens.',
            'includes': 'Activity areas\nTeam building equipment\nFacilitator coordination\nRefreshments\nDebriefing space',
            'starting_price': 3500.00,
            'display_order': 1,
        },
        {
            'name': 'Choir / Video Shoots',
            'slug': 'choir-video-shoots',
            'category': 'general',
            'icon': 'fas fa-video',
            'description': 'Music recordings and video productions in scenic garden locations',
            'detailed_description': 'Beautiful natural backdrop for music videos, choir recordings, and film shoots.',
            'includes': 'Multiple scenic spots\nPower for equipment\nChanging facilities\nParking for vehicles\nFlexible scheduling',
            'starting_price': 25000.00,
            'display_order': 4,
        },
    ]
    
    for event_data in general_events:
        event, created = EventType.objects.get_or_create(
            slug=event_data['slug'],
            defaults=event_data
        )
    
    print("✅ Gardens sample data created successfully!")
    print(f"📊 Created: {GardensPage.objects.count()} page settings")
    print(f"🌿 Created: {Garden.objects.count()} gardens")
    print(f"🎉 Created: {EventType.objects.count()} event types")

if __name__ == '__main__':
    create_sample_data()