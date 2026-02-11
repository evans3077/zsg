# create_dining_data.py
#!/usr/bin/env python
import os
import django
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
apps_path = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, apps_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zamar_springs.settings')
django.setup()

from dining.models import DiningPage, FoodCategory, FoodItem, DiningSpace, FarmSource


def create_sample_data():
    print('Creating dining sample data...')

    DiningPage.objects.update_or_create(
        pk=1,
        defaults={
            'hero_title': 'Zamar Springs Gardens Dining',
            'hero_subtitle': 'Farm-to-fork meals from our Kitchen, Coffee Shop, and Open BBQ Grill.',
            'intro_text': 'Zamar Springs Gardens serves fresh, non-alcoholic dining experiences with ingredients sourced from our farm and trusted local producers.',
            'farm_title': 'Farm to Fork at Zamar Springs Gardens',
            'farm_subtitle': 'Fresh vegetables, fruits, herbs, and proteins prepared daily by our kitchen team.',
            'spaces_title': 'Dining Spaces',
            'spaces_subtitle': 'Gazebo 1 to 6, Pergola, and Open Air Field with flexible table setup.',
            'menu_title': 'Zamar Springs Gardens Menu',
            'menu_subtitle': 'Main meals, platters, mocktails, desserts, and grill favorites.',
            'meta_title': 'Dining at Zamar Springs Gardens | Farm-to-Fork Hotel Dining',
            'meta_description': 'Explore the Zamar Springs Gardens menu: farm-fresh meals, signature platters, mocktails, desserts, and outdoor dining spaces in Machakos.',
            'meta_keywords': 'Zamar Springs Gardens menu, farm to fork hotel, dining Machakos, platters, mocktails, BBQ grill',
            'is_active': True,
        },
    )

    categories_data = [
        {
            'name': 'Main Meals',
            'slug': 'main-meals',
            'category_type': 'mains',
            'description': 'Whole and half servings from our kitchen menu.',
            'icon': 'fas fa-drumstick-bite',
            'display_order': 1,
        },
        {
            'name': 'Signature Platters',
            'slug': 'signature-platters',
            'category_type': 'platters',
            'description': 'Group platters from our platter menu and event menu.',
            'icon': 'fas fa-utensils',
            'display_order': 2,
        },
        {
            'name': 'Mocktails and Coffee',
            'slug': 'mocktails-coffee',
            'category_type': 'mocktails',
            'description': 'Coffee bar and non-alcoholic drinks.',
            'icon': 'fas fa-mug-hot',
            'display_order': 3,
        },
        {
            'name': 'Fresh Juices and Soft Drinks',
            'slug': 'fresh-juices-soft-drinks',
            'category_type': 'juices',
            'description': 'Fresh juice, soda, and cold drink options.',
            'icon': 'fas fa-glass-water',
            'display_order': 4,
        },
        {
            'name': 'BBQ and Grill',
            'slug': 'bbq-and-grill',
            'category_type': 'bbq',
            'description': 'Open BBQ grill selections and choma favorites.',
            'icon': 'fas fa-fire',
            'display_order': 5,
        },
        {
            'name': 'Desserts',
            'slug': 'desserts',
            'category_type': 'desserts',
            'description': 'Milkshakes and ice cream choices.',
            'icon': 'fas fa-ice-cream',
            'display_order': 6,
        },
    ]

    categories = {}
    category_slugs = []
    for cat_data in categories_data:
        category_slugs.append(cat_data['slug'])
        category, _ = FoodCategory.objects.update_or_create(
            slug=cat_data['slug'],
            defaults={**cat_data, 'is_active': True},
        )
        categories[cat_data['slug']] = category

    FoodCategory.objects.exclude(slug__in=category_slugs).delete()

    food_items = [
        {
            'name': 'Kienyeji Chicken (Whole Serving)',
            'slug': 'kienyeji-chicken-whole-serving',
            'category': categories['main-meals'],
            'description': 'Whole serving from our main meals menu. Served with two accompaniments of choice (ugali, chapati, or rice).',
            'is_from_farm': True,
            'farm_ingredients': 'Kienyeji Chicken\nFresh Herbs',
            'price': 2800.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Mbuzi (Choma/Wet/Dry) Whole Serving',
            'slug': 'mbuzi-choma-wet-dry-whole-serving',
            'category': categories['main-meals'],
            'description': 'Whole serving goat meal from our menu with two accompaniments.',
            'is_from_farm': True,
            'farm_ingredients': 'Goat Meat\nKitchen Spices',
            'price': 2000.00,
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Zamar Rabbit (Wet/Dry) Whole Serving',
            'slug': 'zamar-rabbit-wet-dry-whole-serving',
            'category': categories['main-meals'],
            'description': 'Whole serving rabbit prepared wet or dry and served with two accompaniments.',
            'is_from_farm': True,
            'farm_ingredients': 'Rabbit Meat\nFresh Herbs',
            'price': 2000.00,
            'is_featured': True,
            'display_order': 3,
        },
        {
            'name': 'Whole Roast Chicken',
            'slug': 'whole-roast-chicken-main-meals',
            'category': categories['main-meals'],
            'description': 'Whole roast chicken from the main meals menu.',
            'is_from_farm': True,
            'farm_ingredients': 'Chicken\nHerbs\nSpices',
            'price': 2000.00,
            'is_featured': True,
            'display_order': 4,
        },
        {
            'name': 'Beef (Choma/Wet/Dry) Whole Serving',
            'slug': 'beef-choma-wet-dry-whole-serving',
            'category': categories['main-meals'],
            'description': 'Whole serving beef from the main meals menu.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 1800.00,
            'is_featured': False,
            'display_order': 5,
        },
        {
            'name': 'Whole Tilapia Wet Fry',
            'slug': 'whole-tilapia-wet-fry',
            'category': categories['main-meals'],
            'description': 'Whole tilapia prepared wet fry.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 1000.00,
            'is_featured': False,
            'display_order': 6,
        },
        {
            'name': 'Whole Tilapia Dry Fry',
            'slug': 'whole-tilapia-dry-fry',
            'category': categories['main-meals'],
            'description': 'Whole tilapia prepared dry fry.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 1000.00,
            'is_featured': False,
            'display_order': 7,
        },
        {
            'name': 'Platter 1 (For 2 Pax)',
            'slug': 'platter-1-for-2-pax',
            'category': categories['signature-platters'],
            'description': 'Roast chicken, wet fry beef, potato wedges, chapati, 2 glasses of Mua Dew, and green vegetables.',
            'is_from_farm': True,
            'farm_ingredients': 'Chicken\nBeef\nGreen Vegetables',
            'price': 3500.00,
            'is_featured': True,
            'is_special': True,
            'display_order': 1,
        },
        {
            'name': 'Platter 2 (For 2 Pax)',
            'slug': 'platter-2-for-2-pax',
            'category': categories['signature-platters'],
            'description': 'Dry fry goat, roast chicken, sauteed potatoes, ugali, 2 glasses of Mua Dew, and green vegetables.',
            'is_from_farm': True,
            'farm_ingredients': 'Goat Meat\nChicken\nGreen Vegetables',
            'price': 3500.00,
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Platter 1 (For 4 Pax)',
            'slug': 'platter-1-for-4-pax',
            'category': categories['signature-platters'],
            'description': 'Roast chicken, wet fry beef, samosas, choma sausages, fries, ugali, 4 glasses of Mua Dew, green vegetables, and kachumbari.',
            'is_from_farm': True,
            'farm_ingredients': 'Chicken\nBeef\nGreen Vegetables\nKachumbari',
            'price': 5000.00,
            'is_featured': True,
            'display_order': 3,
        },
        {
            'name': 'Platter 2 (For 4 Pax)',
            'slug': 'platter-2-for-4-pax',
            'category': categories['signature-platters'],
            'description': 'Wet fry goat, roast chicken, beef skewers, fries, ugali, 4 glasses of Mua Dew, and green vegetables.',
            'is_from_farm': True,
            'farm_ingredients': 'Goat Meat\nChicken\nBeef\nGreen Vegetables',
            'price': 5000.00,
            'is_featured': True,
            'display_order': 4,
        },
        {
            'name': 'Jolly Feast Platter (For 6)',
            'slug': 'jolly-feast-platter-for-6',
            'category': categories['signature-platters'],
            'description': 'Beef 1kg, goat 1kg, roast chicken 1pc, hot dog 2pcs, chips 2 portions, ugali 2 portions, chapati 2 portions, kachumbari, water and soda.',
            'is_from_farm': True,
            'farm_ingredients': 'Beef\nGoat Meat\nChicken\nKachumbari',
            'price': 9000.00,
            'is_featured': True,
            'is_special': True,
            'display_order': 5,
        },
        {
            'name': 'Carnival Mega Platter (For 10 Pax)',
            'slug': 'carnival-mega-platter-for-10-pax',
            'category': categories['signature-platters'],
            'description': 'Beef 2kg, goat 1kg, roast chicken 2pcs, choma sausages 5pcs, chips 3 portions, ugali 4 portions, chapati 3 portions, kachumbari, water and soda.',
            'is_from_farm': True,
            'farm_ingredients': 'Beef\nGoat Meat\nChicken\nKachumbari',
            'price': 15000.00,
            'is_featured': True,
            'display_order': 6,
        },
        {
            'name': 'Mini Buffet (Per Pax)',
            'slug': 'mini-buffet-per-pax',
            'category': categories['signature-platters'],
            'description': 'Organic beef stew, charcoal grilled chicken, breaded fish fillet, githeri ya mbaazi, vegetable rice, chapati, roast potatoes, ugali, kienyeji greens, and steamed cabbage.',
            'is_from_farm': True,
            'farm_ingredients': 'Beef\nChicken\nKienyeji Greens\nCabbage',
            'price': 2000.00,
            'is_featured': True,
            'display_order': 7,
        },
        {
            'name': 'Shirley Temple',
            'slug': 'shirley-temple',
            'category': categories['mocktails-coffee'],
            'description': 'Classic non-alcoholic mocktail.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 200.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': "Zamar's Sunrise",
            'slug': 'zamars-sunrise',
            'category': categories['mocktails-coffee'],
            'description': 'House mocktail from the Zamar Springs Gardens bar menu.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 300.00,
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Virgin Mojito',
            'slug': 'virgin-mojito',
            'category': categories['mocktails-coffee'],
            'description': 'Mint and lime based mocktail.',
            'is_from_farm': True,
            'farm_ingredients': 'Mint\nLime',
            'price': 300.00,
            'is_featured': True,
            'display_order': 3,
        },
        {
            'name': 'Cappuccino',
            'slug': 'cappuccino',
            'category': categories['mocktails-coffee'],
            'description': 'Hot cappuccino from the coffee menu.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 300.00,
            'is_featured': False,
            'display_order': 4,
        },
        {
            'name': 'Espresso',
            'slug': 'espresso',
            'category': categories['mocktails-coffee'],
            'description': 'Single espresso shot.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 250.00,
            'is_featured': False,
            'display_order': 5,
        },
        {
            'name': 'Latte',
            'slug': 'latte',
            'category': categories['mocktails-coffee'],
            'description': 'Creamy latte from the coffee menu.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 280.00,
            'is_featured': False,
            'display_order': 6,
        },
        {
            'name': 'Mocha',
            'slug': 'mocha',
            'category': categories['mocktails-coffee'],
            'description': 'Coffee and chocolate blend.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 300.00,
            'is_featured': False,
            'display_order': 7,
        },
        {
            'name': 'Fresh Juice',
            'slug': 'fresh-juice',
            'category': categories['fresh-juices-soft-drinks'],
            'description': 'Fresh seasonal juice from our bar section.',
            'is_from_farm': True,
            'farm_ingredients': 'Seasonal Fruits',
            'price': 250.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Soda 300ml',
            'slug': 'soda-300ml',
            'category': categories['fresh-juices-soft-drinks'],
            'description': 'Soft drink 300ml bottle.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 100.00,
            'is_featured': False,
            'display_order': 2,
        },
        {
            'name': 'Del Monte 1 Liter',
            'slug': 'del-monte-1-liter',
            'category': categories['fresh-juices-soft-drinks'],
            'description': 'Del Monte 1 liter juice bottle.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 600.00,
            'is_featured': False,
            'display_order': 3,
        },
        {
            'name': 'Beef Skewers',
            'slug': 'beef-skewers',
            'category': categories['bbq-and-grill'],
            'description': 'Grilled beef skewers from the grill section.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 700.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Mbuzi Choma (Whole)',
            'slug': 'mbuzi-choma-whole',
            'category': categories['bbq-and-grill'],
            'description': 'Open grill goat choma whole serving.',
            'is_from_farm': True,
            'farm_ingredients': 'Goat Meat',
            'price': 2000.00,
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Beef Choma (Whole)',
            'slug': 'beef-choma-whole',
            'category': categories['bbq-and-grill'],
            'description': 'Open grill beef choma whole serving.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 1800.00,
            'is_featured': False,
            'display_order': 3,
        },
        {
            'name': 'Milkshake',
            'slug': 'milkshake',
            'category': categories['desserts'],
            'description': 'Milkshake from dessert menu.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 350.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Ice Cream Small',
            'slug': 'ice-cream-small',
            'category': categories['desserts'],
            'description': 'Small serving. Flavours available: vanilla, strawberry, chocolate.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 150.00,
            'is_featured': False,
            'display_order': 2,
        },
        {
            'name': 'Ice Cream Large',
            'slug': 'ice-cream-large',
            'category': categories['desserts'],
            'description': 'Large serving. Flavours available: vanilla, strawberry, chocolate.',
            'is_from_farm': False,
            'farm_ingredients': '',
            'price': 250.00,
            'is_featured': False,
            'display_order': 3,
        },
    ]

    food_slugs = []
    for item in food_items:
        food_slugs.append(item['slug'])
        FoodItem.objects.update_or_create(
            slug=item['slug'],
            defaults={**item, 'is_active': True},
        )

    FoodItem.objects.exclude(slug__in=food_slugs).delete()

    dining_spaces = [
        {
            'name': 'Pergola',
            'slug': 'pergola',
            'space_type': 'pergola',
            'description': 'Covered pergola dining space for small groups, family meals, and private reservations.',
            'capacity': 20,
            'ideal_for': 'Family meals\nPrivate bookings\nSmall celebrations\nCoffee and dessert',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Gazebo 1',
            'slug': 'gazebo-1',
            'space_type': 'gazebo',
            'description': 'Open gazebo with table service and garden-facing setup.',
            'capacity': 8,
            'ideal_for': 'Casual dining\nFamily lunch\nQuick coffee meetings',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Gazebo 2',
            'slug': 'gazebo-2',
            'space_type': 'gazebo',
            'description': 'Comfortable gazebo with flexible layout for breakfast and dinner.',
            'capacity': 8,
            'ideal_for': 'Friends meetups\nWeekend meals\nSmall group booking',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': True,
            'display_order': 3,
        },
        {
            'name': 'Gazebo 3',
            'slug': 'gazebo-3',
            'space_type': 'gazebo',
            'description': 'Shaded gazebo suitable for long-stay dining and coffee service.',
            'capacity': 8,
            'ideal_for': 'Coffee and snacks\nFamily time\nQuiet dining',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': True,
            'display_order': 4,
        },
        {
            'name': 'Gazebo 4',
            'slug': 'gazebo-4',
            'space_type': 'gazebo',
            'description': 'Gazebo with comfortable flow for afternoon and evening service.',
            'capacity': 8,
            'ideal_for': 'Tea time\nSmall parties\nEvening meals',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': False,
            'display_order': 5,
        },
        {
            'name': 'Gazebo 5',
            'slug': 'gazebo-5',
            'space_type': 'gazebo',
            'description': 'Garden-facing gazebo designed for small private groups.',
            'capacity': 8,
            'ideal_for': 'Birthdays\nFamily dinner\nPrivate conversations',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': False,
            'display_order': 6,
        },
        {
            'name': 'Gazebo 6',
            'slug': 'gazebo-6',
            'space_type': 'gazebo',
            'description': 'Quiet gazebo near greenery for calm dining sessions.',
            'capacity': 8,
            'ideal_for': 'Quiet meals\nDate meals\nLight lunch',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': False,
            'display_order': 7,
        },
        {
            'name': 'Open Air Field',
            'slug': 'open-air-field',
            'space_type': 'garden',
            'description': 'Large open dining field where tables and seats are arranged for events and large groups.',
            'capacity': 200,
            'ideal_for': 'Large groups\nOutdoor events\nCorporate setups\nCelebrations',
            'has_lighting': True,
            'has_power': True,
            'is_covered': False,
            'is_private': False,
            'is_featured': True,
            'display_order': 8,
        },
    ]

    space_slugs = []
    for space in dining_spaces:
        space_slugs.append(space['slug'])
        DiningSpace.objects.update_or_create(
            slug=space['slug'],
            defaults={**space, 'is_active': True},
        )

    DiningSpace.objects.exclude(slug__in=space_slugs).delete()

    farm_sources = [
        {
            'name': 'Organic Vegetables',
            'source_type': 'vegetable',
            'icon': 'fas fa-carrot',
            'description': 'Seasonal vegetables used in sides, salads, and platter accompaniments.',
            'display_order': 1,
        },
        {
            'name': 'Seasonal Fruits',
            'source_type': 'fruit',
            'icon': 'fas fa-apple-whole',
            'description': 'Fresh fruit used in juices, mocktails, and dessert pairings.',
            'display_order': 2,
        },
        {
            'name': 'Fresh Herbs',
            'source_type': 'herb',
            'icon': 'fas fa-leaf',
            'description': 'Daily-picked herbs for marinades, soup, and grill finishing.',
            'display_order': 3,
        },
        {
            'name': 'Kienyeji Chicken',
            'source_type': 'meat',
            'icon': 'fas fa-drumstick-bite',
            'description': 'Free-range chicken used in whole meals and platter options.',
            'display_order': 4,
        },
        {
            'name': 'Rabbit and Goat',
            'source_type': 'meat',
            'icon': 'fas fa-paw',
            'description': 'Farm-reared rabbit and goat used in wet fry, dry fry, and grill menu options.',
            'display_order': 5,
        },
        {
            'name': 'Greens and Cabbage',
            'source_type': 'vegetable',
            'icon': 'fas fa-seedling',
            'description': 'Kienyeji greens and steamed cabbage for balanced meal plates.',
            'display_order': 6,
        },
    ]

    source_names = []
    for source in farm_sources:
        source_names.append(source['name'])
        FarmSource.objects.update_or_create(
            name=source['name'],
            defaults={**source, 'is_active': True},
        )

    FarmSource.objects.exclude(name__in=source_names).delete()

    print('Dining sample data created successfully.')
    print(f'Dining Page: {DiningPage.objects.count()}')
    print(f'Food Categories: {FoodCategory.objects.count()}')
    print(f'Food Items: {FoodItem.objects.count()}')
    print(f'Dining Spaces: {DiningSpace.objects.count()}')
    print(f'Farm Sources: {FarmSource.objects.count()}')


if __name__ == '__main__':
    create_sample_data()
