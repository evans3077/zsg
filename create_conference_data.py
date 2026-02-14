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

# Now import from your apps
try:
    from apps.conferences.models import (
        ConferencePage, ConferenceCategory, 
        ConferenceRoom, ConferencePackage
    )
    print("✅ Successfully imported conference models")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print(f"📁 Current Python path: {sys.path}")
    print(f"📁 Apps path: {apps_path}")
    print("📁 Checking if conferences app exists...")
    conferences_path = os.path.join(apps_path, 'conferences')
    if os.path.exists(conferences_path):
        print(f"✅ Conferences app directory exists at: {conferences_path}")
        print("📁 Contents:")
        for item in os.listdir(conferences_path):
            print(f"   - {item}")
    sys.exit(1)

    
def create_sample_data():
    # Create Conference Page
    page, created = ConferencePage.objects.get_or_create(
        defaults={
            'hero_title': 'Conference & Meetings',
            'hero_subtitle': 'State-of-the-art meeting facilities in a serene, non-alcoholic environment',
            'intro_text': 'From intimate board meetings to large conferences, we have the perfect space for your business needs.',
            'meta_title': 'Conference Facilities | Zamar Springs Gardens',
            'meta_description': 'Professional meeting rooms and conference halls in a non-alcoholic garden venue near Nairobi',
            'meta_keywords': 'conference rooms, meeting facilities, board rooms, meeting rooms, halls, nairobi',
            'is_active': True,
        }
    )
    
    # Create Categories
    categories_data = [
        {
            'name': 'Board Rooms',
            'slug': 'board-rooms',
            'category_type': 'board',
            'description': 'Executive board rooms for confidential meetings and decision-making sessions',
            'icon': 'fas fa-gavel',
            'display_order': 1,
        },
        {
            'name': 'Meeting Rooms',
            'slug': 'meeting-rooms',
            'category_type': 'meeting',
            'description': 'Versatile meeting rooms for team discussions and client presentations',
            'icon': 'fas fa-users',
            'display_order': 2,
        },
        {
            'name': 'Halls',
            'slug': 'halls',
            'category_type': 'hall',
            'description': 'Large conference hall for major events, seminars, and corporate gatherings',
            'icon': 'fas fa-chalkboard-teacher',
            'display_order': 3,
        },
    ]
    
    categories = {}
    for data in categories_data:
        category, created = ConferenceCategory.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        categories[data['slug']] = category
    
    # Create Conference Hall (Acacia)
    conference_hall, created = ConferenceRoom.objects.get_or_create(
        slug='acacia-conference-hall',
        defaults={
            'category': categories['halls'],
            'name': 'Acacia Conference Hall',
            'room_type': 'hall',
            'description': 'Our premier conference hall with modern audiovisual equipment and flexible seating arrangements. Perfect for large corporate events, seminars, and major presentations.',
            'capacity_classroom': 120,
            'capacity_theatre': 180,
            'capacity_banquet': 120,
            'capacity_u_shape': 0,
            'capacity_boardroom': 40,
            'has_projector': True,
            'has_sound_system': True,
            'has_wifi': True,
            'has_whiteboard': True,
            'has_air_conditioning': True,
            'has_natural_light': True,
            'has_secretary_space': True,
            'has_video_conferencing': True,
            'dimensions': '15m x 20m',
            'floor_area': '300 sqm',
            'half_day_rate': 3500.00,
            'full_day_rate': 4500.00,
            'meta_title': 'Acacia Conference Hall - Zamar Springs Gardens',
            'meta_description': 'Large conference hall for 200 people with modern facilities',
            'is_featured': True,
            'display_order': 1,
        }
    )
    
    # Create Meeting Rooms - Standard
    meeting_rooms_standard = [
        {
            'slug': 'bamboo-meeting-room',
            'category': categories['halls'],
            'name': 'Bamboo Hall',
            'room_type': 'hall',
            'description': 'Spacious conference hall with natural lighting and comfortable seating. Ideal for large presentations.',
            'capacity_classroom': 70,
            'capacity_theatre': 160,
            'capacity_banquet': 70,
            'capacity_u_shape': 0,
            'capacity_boardroom': 30,
            'display_order': 1,
        },
        {
            'slug': 'cactus-meeting-room',
            'category': categories['halls'],
            'name': 'Cactus Hall',
            'room_type': 'hall',
            'description': 'Versatile conference hall with modern amenities and flexible layout options.',
            'capacity_classroom': 70,
            'capacity_theatre': 150,
            'capacity_banquet': 70,
            'capacity_u_shape': 0,
            'capacity_boardroom': 30,
            'display_order': 2,
        },
    ]
    
    for room_data in meeting_rooms_standard:
        room, created = ConferenceRoom.objects.get_or_create(
            slug=room_data['slug'],
            defaults={
                **room_data,
                'has_projector': True,
                'has_sound_system': True,
                'has_wifi': True,
                'has_whiteboard': True,
                'has_air_conditioning': True,
                'has_natural_light': True,
                'has_secretary_space': False,
                'has_video_conferencing': True,
                'dimensions': '10m x 8m',
                'floor_area': '80 sqm',
                'half_day_rate': 3500.00,
                'full_day_rate': 45000.00,
                'meta_title': f"{room_data['name']} - Professional Meeting Space",
                'meta_description': f"Meeting room for up to {room_data['capacity_theatre']} people",
                'is_featured': room_data['slug'] == 'bamboo-meeting-room',
            }
        )
    
    # Create Meeting Rooms - Executive
    meeting_rooms_executive = [
        {
            'slug': 'japonica-meeting-room',
            'category': categories['meeting-rooms'],
            'name': 'Japonica Meeting Room',
            'room_type': 'standard',
            'description': 'Premium meeting room with leather seating and advanced technology.',
            'capacity_classroom': 35,
            'capacity_theatre': 50,
            'capacity_banquet': 35,
            'capacity_u_shape': 20,
            'capacity_boardroom': 25,
            'display_order': 1,
        },
        {
            'slug': 'melia-meeting-room',
            'category': categories['meeting-rooms'],
            'name': 'Melia Meeting Room',
            'room_type': 'standard',
            'description': 'Meeting space with panoramic garden views and premium amenities.',
            'capacity_classroom': 35,
            'capacity_theatre': 50,
            'capacity_banquet': 35,
            'capacity_u_shape': 20,
            'capacity_boardroom': 25,
            'display_order': 2,
        },
    ]
    
    for room_data in meeting_rooms_executive:
        room, created = ConferenceRoom.objects.get_or_create(
            slug=room_data['slug'],
            defaults={
                **room_data,
                'has_projector': True,
                'has_sound_system': True,
                'has_wifi': True,
                'has_whiteboard': True,
                'has_air_conditioning': True,
                'has_natural_light': True,
                'has_secretary_space': True,
                'has_video_conferencing': True,
                'dimensions': '8m x 6m',
                'floor_area': '48 sqm',
                'half_day_rate': 3500.00,
                'full_day_rate': 4500.00,
                'hourly_rate': 1000.00,
                'meta_title': f"{room_data['name']} - Meeting Room",
                'meta_description': f"Meeting room for up to {room_data['capacity_theatre']} people",
                'is_featured': True,
            }
        )
    
    # Create Board Rooms
    board_rooms = [
        {
            'slug': 'board-room-1',
            'category': categories['board-rooms'],
            'name': 'Board Room 1',
            'room_type': 'board',
            'description': 'Executive board room with premium leather chairs and integrated technology.',
            'capacity_classroom': 0,
            'capacity_theatre': 0,
            'capacity_banquet': 0,
            'capacity_u_shape': 0,
            'capacity_boardroom': 12,
            'display_order': 1,
        },
        {
            'slug': 'board-room-2',
            'category': categories['board-rooms'],
            'name': 'Board Room 2',
            'room_type': 'board',
            'description': 'Modern board room with video conferencing capabilities and personal secretary space.',
            'capacity_classroom': 0,
            'capacity_theatre': 0,
            'capacity_banquet': 0,
            'capacity_u_shape': 0,
            'capacity_boardroom': 12,
            'display_order': 2,
        },
    ]
    
    for room_data in board_rooms:
        room, created = ConferenceRoom.objects.get_or_create(
            slug=room_data['slug'],
            defaults={
                **room_data,
                'has_projector': True,
                'has_sound_system': True,
                'has_wifi': True,
                'has_whiteboard': True,
                'has_air_conditioning': True,
                'has_natural_light': True,
                'has_secretary_space': True,
                'has_video_conferencing': True,
                'dimensions': '6m x 4m',
                'floor_area': '24 sqm',
                'half_day_rate': 3500.00,
                'full_day_rate': 4500.00,
                'hourly_rate': 1000.00,
                'meta_title': f"{room_data['name']} - Executive Board Room",
                'meta_description': f"Board room for {room_data['capacity_boardroom']} executives",
                'is_featured': True,
            }
        )
    
    # Create Packages
    packages_data = [
        {
            'slug': 'half-day-conference',
            'name': 'Half Day Conference',
            'description': 'Perfect for morning or afternoon meetings, includes basic amenities and refreshments.',
            'includes': '4-hour room rental\nProjector & Screen\nWhiteboard & Markers\nHigh-speed WiFi\nTea/Coffee Break\nBottled Water',
            'price': 3500.00,
            'duration': 'Half Day (4 Hours)',
            'suitable_for': 'Team meetings, client presentations, training sessions',
            'is_popular': True,
            'display_order': 1,
        },
        {
            'slug': 'full-day-conference',
            'name': 'Full Day Conference',
            'description': 'Complete conference package with full amenities and catering services.',
            'includes': '8-hour room rental\nAudiovisual Equipment\nFlipchart & Stationery\nHigh-speed WiFi\nMorning & Afternoon Tea\nLunch Buffet\nBottled Water',
            'price': 4500.00,
            'duration': 'Full Day (8 Hours)',
            'suitable_for': 'Full-day workshops, seminars, corporate training',
            'is_popular': True,
            'display_order': 2,
        },
        {
            'slug': 'executive-board-package',
            'name': 'Executive Board Package',
            'description': 'Premium package for executive meetings with enhanced privacy and services.',
            'includes': 'Flexible timing (up to 6 hours)\nVideo Conferencing Setup\nConfidential Meeting Space\nPersonal Secretary Area\nPremium Catering\nDocument Printing',
            'price': 3500.00,
            'duration': 'Flexible Hours',
            'suitable_for': 'Board meetings, executive sessions, confidential discussions',
            'is_popular': False,
            'display_order': 3,
        },
        {
            'slug': 'training-workshop-package',
            'name': 'Training Workshop Package',
            'description': 'Designed specifically for interactive training sessions and workshops.',
            'includes': 'Full day room rental\nInteractive Whiteboard\nTraining Materials Setup\nBreakout Space\nTea/Coffee & Snacks\nLunch Buffet\nTraining Support',
            'price': 4500.00,
            'duration': 'Full Day (8 Hours)',
            'suitable_for': 'Corporate training, workshops, team building',
            'is_popular': True,
            'display_order': 4,
        },
    ]
    
    for package_data in packages_data:
        package, created = ConferencePackage.objects.get_or_create(
            slug=package_data['slug'],
            defaults=package_data
        )
    
    print("✅ Conference sample data created successfully!")
    print(f"📊 Created: {ConferenceCategory.objects.count()} categories")
    print(f"🏢 Created: {ConferenceRoom.objects.count()} rooms")
    print(f"📦 Created: {ConferencePackage.objects.count()} packages")

if __name__ == '__main__':
    create_sample_data()
