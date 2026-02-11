# create_dining_data.py
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

from dining.models import DiningPage, FoodCategory, FoodItem, DiningSpace, SpaceGallery, FarmSource

def create_sample_data():
    print("🔄 Creating dining sample data...")
    
    # Create Dining Page
    page, created = DiningPage.objects.get_or_create(
        defaults={
            'hero_title': 'Dining Experience',
            'hero_subtitle': 'Farm-to-fork dining in a serene, non-alcoholic environment',
            'intro_text': 'Experience fresh, organic meals prepared with ingredients from our own farm. Enjoy dining in our beautiful pergolas and gazebos surrounded by nature.',
            'farm_title': 'Farm-to-Fork Freshness',
            'farm_subtitle': 'All ingredients sourced directly from our organic farm',
            'spaces_title': 'Prime Dining Spaces',
            'spaces_subtitle': 'Beautiful locations for memorable dining experiences',
            'menu_title': 'Our Menu',
            'menu_subtitle': 'Fresh, organic, and delicious',
            'meta_title': 'Dining Experience | Zamar Springs Gardens',
            'meta_description': 'Farm-to-fork dining with organic ingredients, beautiful pergolas and gazebos in Machakos',
            'meta_keywords': 'farm to fork, organic dining, pergola dining, gazebo, fresh juices, mocktails',
            'is_active': True,
        }
    )
    
    # Create Food Categories
    categories_data = [
        {
            'name': 'Fresh Juices',
            'slug': 'fresh-juices',
            'category_type': 'juices',
            'description': 'Freshly squeezed juices from our organic fruits',
            'icon': 'fas fa-glass-whiskey',
            'display_order': 1,
        },
        {
            'name': 'Mocktails & Coffee',
            'slug': 'mocktails-coffee',
            'category_type': 'mocktails',
            'description': 'Creative non-alcoholic drinks and premium coffee',
            'icon': 'fas fa-cocktail',
            'display_order': 2,
        },
        {
            'name': 'Platters',
            'slug': 'platters',
            'category_type': 'platters',
            'description': 'Shareable platters for groups and families',
            'icon': 'fas fa-utensils',
            'display_order': 3,
        },
        {
            'name': 'Main Dishes',
            'slug': 'main-dishes',
            'category_type': 'mains',
            'description': 'Farm-fresh main courses and specialties',
            'icon': 'fas fa-drumstick-bite',
            'display_order': 4,
        },
        {
            'name': 'BBQ / Choma Zone',
            'slug': 'bbq-choma',
            'category_type': 'bbq',
            'description': 'Grilled meats and BBQ specialties',
            'icon': 'fas fa-fire',
            'display_order': 5,
        },
        {
            'name': 'Desserts',
            'slug': 'desserts',
            'category_type': 'desserts',
            'description': 'Sweet treats and desserts',
            'icon': 'fas fa-ice-cream',
            'display_order': 6,
        },
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = FoodCategory.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        categories[cat_data['slug']] = category
    
    # Create Food Items - Fresh Juices
    juices = [
        {
            'name': 'Mango Passion',
            'slug': 'mango-passion-juice',
            'category': categories['fresh-juices'],
            'description': 'Fresh mango blended with passion fruit, served chilled',
            'is_from_farm': True,
            'farm_ingredients': 'Mango\nPassion Fruit',
            'price': 350.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Orange Carrot Ginger',
            'slug': 'orange-carrot-ginger-juice',
            'category': categories['fresh-juices'],
            'description': 'Orange, carrot, and ginger blend for a healthy boost',
            'is_from_farm': True,
            'farm_ingredients': 'Oranges\nCarrots\nGinger',
            'price': 300.00,
            'is_featured': True,
            'display_order': 2,
        },
    ]
    
    # Create Food Items - Mocktails
    mocktails = [
        {
            'name': 'Virgin Mojito',
            'slug': 'virgin-mojito',
            'category': categories['mocktails-coffee'],
            'description': 'Fresh mint, lime, and soda water with a hint of sweetness',
            'is_from_farm': True,
            'farm_ingredients': 'Mint\nLimes',
            'price': 450.00,
            'is_featured': True,
            'is_special': True,
            'display_order': 1,
        },
        {
            'name': 'Berry Bliss',
            'slug': 'berry-bliss-mocktail',
            'category': categories['mocktails-coffee'],
            'description': 'Mixed berries with soda and fresh herbs',
            'is_from_farm': True,
            'farm_ingredients': 'Strawberries\nBlueberries\nMint',
            'price': 500.00,
            'is_featured': True,
            'display_order': 2,
        },
    ]
    
    # Create Food Items - Platters
    platters = [
        {
            'name': 'Fruit Platter',
            'slug': 'fresh-fruit-platter',
            'category': categories['platters'],
            'description': 'Seasonal fruits beautifully arranged, serves 4-6 people',
            'is_from_farm': True,
            'farm_ingredients': 'Seasonal Fruits',
            'price': 1500.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Vegetable Crudités',
            'slug': 'vegetable-crudites',
            'category': categories['platters'],
            'description': 'Fresh vegetables with homemade dips',
            'is_from_farm': True,
            'farm_ingredients': 'Carrots\nCucumbers\nBell Peppers\nHerbs',
            'price': 1200.00,
            'is_featured': True,
            'display_order': 2,
        },
    ]
    
    # Create Food Items - Main Dishes
    mains = [
        {
            'name': 'Farm Chicken Stew',
            'slug': 'farm-chicken-stew',
            'category': categories['main-dishes'],
            'description': 'Free-range chicken stew with farm vegetables',
            'is_from_farm': True,
            'farm_ingredients': 'Kienyeji Chicken\nTomatoes\nOnions\nGarlic\nHerbs',
            'price': 1200.00,
            'is_featured': True,
            'is_special': True,
            'display_order': 1,
        },
        {
            'name': 'Rabbit Curry',
            'slug': 'rabbit-curry',
            'category': categories['main-dishes'],
            'description': 'Tender rabbit meat in rich curry sauce',
            'is_from_farm': True,
            'farm_ingredients': 'Rabbit Meat\nCoconut Milk\nCurry Spices\nHerbs',
            'price': 1500.00,
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Goat Meat Deluxe',
            'slug': 'goat-meat-deluxe',
            'category': categories['main-dishes'],
            'description': 'Tender goat meat with rosemary and garlic',
            'is_from_farm': True,
            'farm_ingredients': 'Goat Meat\nRosemary\nGarlic\nFarm Vegetables',
            'price': 1400.00,
            'is_featured': True,
            'display_order': 3,
        },
    ]
    
    # Create Food Items - BBQ
    bbq = [
        {
            'name': 'Mixed Grill Platter',
            'slug': 'mixed-grill-platter',
            'category': categories['bbq-choma'],
            'description': 'Assorted grilled meats with traditional sides, serves 4-6',
            'is_from_farm': True,
            'farm_ingredients': 'Chicken\nGoat Meat\nBeef\nFarm Vegetables',
            'price': 3500.00,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Whole Roasted Chicken',
            'slug': 'whole-roasted-chicken',
            'category': categories['bbq-choma'],
            'description': 'Free-range chicken roasted with herbs and spices',
            'is_from_farm': True,
            'farm_ingredients': 'Kienyeji Chicken\nHerbs\nSpices',
            'price': 2500.00,
            'is_featured': True,
            'display_order': 2,
        },
    ]
    
    # Combine all food items
    all_food = juices + mocktails + platters + mains + bbq
    
    for food_data in all_food:
        food, created = FoodItem.objects.get_or_create(
            slug=food_data['slug'],
            defaults=food_data
        )
    
    # Create Dining Spaces
    dining_spaces = [
        {
            'name': 'Romantic Pergola',
            'slug': 'romantic-pergola',
            'space_type': 'pergola',
            'description': 'Private pergola with fairy lights, perfect for romantic dinners and special occasions. Surrounded by flowering plants with beautiful garden views.',
            'capacity': 4,
            'ideal_for': 'Romantic dinners\nAnniversaries\nProposals\nSpecial occasions\nPrivate dining',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': True,
            'display_order': 1,
        },
        {
            'name': 'Family Gazebo',
            'slug': 'family-gazebo',
            'space_type': 'gazebo',
            'description': 'Spacious gazebo ideal for family gatherings and group dining. Open sides with beautiful views of the gardens.',
            'capacity': 8,
            'ideal_for': 'Family gatherings\nBirthday parties\nGroup dining\nCelebrations',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': True,
            'display_order': 2,
        },
        {
            'name': 'Garden Pavilion',
            'slug': 'garden-pavilion',
            'space_type': 'gazebo',
            'description': 'Large pavilion surrounded by gardens, perfect for bigger groups and events. Features beautiful natural lighting.',
            'capacity': 15,
            'ideal_for': 'Corporate events\nGroup celebrations\nLarge family gatherings\nSpecial events',
            'has_lighting': True,
            'has_power': True,
            'is_covered': True,
            'is_private': True,
            'is_featured': True,
            'display_order': 3,
        },
    ]
    
    for space_data in dining_spaces:
        space, created = DiningSpace.objects.get_or_create(
            slug=space_data['slug'],
            defaults=space_data
        )
    
    # Create Farm Sources
    farm_sources = [
        {
            'name': 'Organic Vegetables',
            'source_type': 'vegetable',
            'icon': 'fas fa-carrot',
            'description': 'Fresh vegetables grown in our organic gardens without chemicals',
            'display_order': 1,
        },
        {
            'name': 'Seasonal Fruits',
            'source_type': 'fruit',
            'icon': 'fas fa-apple-alt',
            'description': 'Juicy fruits harvested at peak ripeness from our orchards',
            'display_order': 2,
        },
        {
            'name': 'Fresh Herbs',
            'source_type': 'herb',
            'icon': 'fas fa-leaf',
            'description': 'Aromatic herbs picked fresh daily for maximum flavor',
            'display_order': 3,
        },
        {
            'name': 'Kienyeji Chicken',
            'source_type': 'meat',
            'icon': 'fas fa-drumstick-bite',
            'description': 'Free-range chickens raised naturally on our farm',
            'display_order': 4,
        },
        {
            'name': 'Rabbit Meat',
            'source_type': 'meat',
            'icon': 'fas fa-paw',
            'description': 'Lean, healthy rabbit meat from our sustainable rabbitry',
            'display_order': 5,
        },
        {
            'name': 'Goat Meat',
            'source_type': 'meat',
            'icon': 'fas fa-horse',
            'description': 'Tender goat meat from our own herd, raised on natural feed',
            'display_order': 6,
        },
    ]
    
    for source_data in farm_sources:
        source, created = FarmSource.objects.get_or_create(
            name=source_data['name'],
            defaults=source_data
        )
    
    print("✅ Dining sample data created successfully!")
    print(f"📄 Dining Page: {DiningPage.objects.count()}")
    print(f"🍽️  Food Categories: {FoodCategory.objects.count()}")
    print(f"🥗 Food Items: {FoodItem.objects.count()}")
    print(f"🏞️  Dining Spaces: {DiningSpace.objects.count()}")
    print(f"🌱 Farm Sources: {FarmSource.objects.count()}")

if __name__ == '__main__':
    create_sample_data()