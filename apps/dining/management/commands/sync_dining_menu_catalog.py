from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from dining.models import FoodCategory, FoodItem


CATALOG = [
    {
        "name": "Tea & Hot Drinks",
        "slug": "tea-hot-drinks",
        "category_type": "mocktails",
        "icon": "fas fa-mug-hot",
        "description": "Tea and hot beverage selection from Menu-1.",
        "items": [
            ("African Mixed Tea", "250", "tea,african,mixed"),
            ("Masala Tea", "300", "tea,masala,chai"),
            ("Lemon Tea", "150", "tea,lemon"),
            ("Black Tea", "150", "tea,black"),
            ("White Chocolate", "250", "chocolate,hot,white"),
            ("Black Chocolate", "200", "chocolate,hot,black"),
            ("White Milo", "250", "milo,white,hot"),
            ("Black Milo", "200", "milo,black,hot"),
            ("White Coffee", "250", "coffee,white,hot"),
            ("Black Coffee", "200", "coffee,black,hot"),
            ("Dawa", "250", "tea,dawa,honey,ginger,lemon"),
            ("Pot of Milk", "250", "milk,hot,tea"),
        ],
    },
    {
        "name": "Coffee",
        "slug": "coffee",
        "category_type": "mocktails",
        "icon": "fas fa-coffee",
        "description": "Single and double coffee options.",
        "items": [
            ("Espresso (Single)", "150", "coffee,espresso,single"),
            ("Espresso (Double)", "250", "coffee,espresso,double"),
            ("Cappuccino (Single)", "250", "coffee,cappuccino,single"),
            ("Cappuccino (Double)", "300", "coffee,cappuccino,double"),
            ("Americano", "250", "coffee,americano"),
            ("Latte (Single)", "280", "coffee,latte,single"),
            ("Latte (Double)", "350", "coffee,latte,double"),
            ("Mocha (Single)", "300", "coffee,mocha,single"),
            ("Mocha (Double)", "380", "coffee,mocha,double"),
        ],
    },
    {
        "name": "Cold Drinks",
        "slug": "cold-drinks",
        "category_type": "juices",
        "icon": "fas fa-glass-water",
        "description": "Sodas, juices, water and cold beverages.",
        "items": [
            ("Soda 300ml", "100", "cold,drink,soda"),
            ("Del Monte 1 Liter", "600", "cold,drink,juice,del monte"),
            ("Water 500ml", "100", "cold,drink,water"),
            ("Water 1 Liter", "190", "cold,drink,water"),
            ("Water 1.5 Liters", "280", "cold,drink,water"),
            ("Water 10 Liters", "1500", "cold,drink,water"),
            ("Water 20 Litres", "2500", "cold,drink,water"),
        ],
    },
    {
        "name": "Snacks",
        "slug": "snacks",
        "category_type": "mains",
        "icon": "fas fa-cookie-bite",
        "description": "Quick snack options and tea accompaniments.",
        "items": [
            ("Beef Sausage Pair", "150", "snacks,beef,sausage"),
            ("Beef Samosa Pair", "150", "snacks,beef,samosa"),
            ("Mandazi Pair", "100", "snacks,mandazi,pastry"),
            ("Fried Eggs", "150", "snacks,eggs"),
            ("Spanish Omelette", "300", "snacks,omelette"),
            ("Beef Skewers", "700", "snacks,beef,skewers"),
        ],
    },
    {
        "name": "Additionals",
        "slug": "additionals",
        "category_type": "mains",
        "icon": "fas fa-bowl-rice",
        "description": "Sides and add-on accompaniments.",
        "items": [
            ("White Rice", "150", "additionals,rice"),
            ("Vegetable Rice", "170", "additionals,vegetable,rice"),
            ("White Ugali", "150", "additionals,ugali"),
            ("Brown Ugali", "170", "additionals,ugali,brown"),
            ("White Chapati", "150", "additionals,chapati"),
            ("Brown Chapati", "170", "additionals,chapati,brown"),
            ("Chips", "250", "additionals,chips,fries"),
            ("Roast Potatoes", "300", "additionals,potatoes,roast"),
            ("Chips Masala", "350", "additionals,chips,masala"),
            ("Chips Masala Special", "500", "additionals,chips,masala,special"),
        ],
    },
    {
        "name": "Soups",
        "slug": "soups",
        "category_type": "mains",
        "icon": "fas fa-bowl-food",
        "description": "Freshly prepared soup options.",
        "items": [
            ("Bone Soup", "200", "soups,bone"),
            ("Chicken Soup", "250", "soups,chicken"),
            ("Vegetable Soup", "150", "soups,vegetable"),
        ],
    },
    {
        "name": "Vegetables",
        "slug": "vegetables",
        "category_type": "mains",
        "icon": "fas fa-leaf",
        "description": "Vegetable side dishes and salads.",
        "items": [
            ("Spinach", "150", "vegetables,spinach"),
            ("Cabbage", "150", "vegetables,cabbage"),
            ("Mixed Vegetables", "150", "vegetables,mixed"),
            ("Chef's Salad", "250", "vegetables,salad"),
            ("Kachumbari", "100", "vegetables,kachumbari"),
            ("Kienyeji Greens", "150", "vegetables,kienyeji,greens"),
        ],
    },
    {
        "name": "Kiddies Corner",
        "slug": "kiddies-corner",
        "category_type": "mains",
        "icon": "fas fa-child-reaching",
        "description": "Kid-friendly meal options.",
        "items": [
            ("Fish Fingers", "850", "kiddies,fish,fingers"),
            ("Fish Fillet", "850", "kiddies,fish,fillet"),
            ("Quarter Chicken and Chips", "700", "kiddies,chicken,chips"),
            ("Chips and Sausage", "350", "kiddies,chips,sausage"),
        ],
    },
    {
        "name": "Main Meals (Whole Servings)",
        "slug": "main-meals-whole",
        "category_type": "mains",
        "icon": "fas fa-drumstick-bite",
        "description": "Whole servings served with two accompaniments.",
        "items": [
            ("Kienyeji Chicken (Whole Serving)", "2800", "whole servings,main meals,chicken"),
            ("Mbuzi (Choma/Wet/Dry) Whole Serving", "2000", "whole servings,main meals,goat,mbuzi"),
            ("Whole Roast Chicken", "2000", "whole servings,main meals,chicken,roast"),
            ("Zamar Rabbit (Wet/Dry) Whole Serving", "2000", "whole servings,main meals,rabbit"),
            ("Beef (Choma/Wet/Dry) Whole Serving", "1800", "whole servings,main meals,beef"),
            ("Whole Tilapia Wet Fry", "1000", "whole servings,fish,tilapia,wet"),
            ("Whole Tilapia Dry Fry", "1000", "whole servings,fish,tilapia,dry"),
            ("Wet Githeri", "350", "main meals,githeri"),
            ("Wet Githeri Special", "500", "main meals,githeri,special"),
        ],
    },
    {
        "name": "Half Servings",
        "slug": "half-servings",
        "category_type": "mains",
        "icon": "fas fa-plate-wheat",
        "description": "Half servings served with one accompaniment.",
        "items": [
            ("Kienyeji Chicken (Half Serving)", "1600", "half servings,main meals,chicken"),
            ("Mbuzi (Choma/Wet/Dry) Half Serving", "1200", "half servings,main meals,goat,mbuzi"),
            ("Zamar Rabbit (Wet/Dry) Half Serving", "1200", "half servings,main meals,rabbit"),
            ("Roast Chicken (Half Serving)", "1200", "half servings,main meals,chicken,roast"),
            ("Beef (Choma/Wet/Dry) Half Serving", "1100", "half servings,main meals,beef"),
        ],
    },
    {
        "name": "Signature Platters",
        "slug": "signature-platters",
        "category_type": "platters",
        "icon": "fas fa-utensils",
        "description": "Popular sharing platters and buffet options.",
        "items": [
            ("Platter 1 (For 2 Pax)", "3500", "platter,2 pax"),
            ("Platter 2 (For 2 Pax)", "3500", "platter,2 pax"),
            ("Platter 1 (For 4 Pax)", "5000", "platter,4 pax"),
            ("Platter 2 (For 4 Pax)", "5000", "platter,4 pax"),
            ("Jolly Feast Platter (For 6)", "9000", "platter,6 pax"),
            ("Carnival Mega Platter (For 10 Pax)", "15000", "platter,10 pax"),
            ("Mini Buffet (Per Pax)", "2000", "buffet,per pax"),
        ],
    },
    {
        "name": "Desserts",
        "slug": "desserts",
        "category_type": "desserts",
        "icon": "fas fa-ice-cream",
        "description": "Milkshake and ice cream options.",
        "items": [
            ("Milkshake", "300", "desserts,milkshake"),
            ("Ice Cream Large", "250", "desserts,ice cream,large"),
            ("Ice Cream Small", "150", "desserts,ice cream,small"),
        ],
    },
]


class Command(BaseCommand):
    help = "Syncs Dining menu catalog from the latest Menu-1 structure."

    def handle(self, *args, **options):
        active_category_slugs = []
        active_item_slugs = []

        for category_index, category_data in enumerate(CATALOG, start=1):
            category, _ = FoodCategory.objects.update_or_create(
                slug=category_data["slug"],
                defaults={
                    "name": category_data["name"],
                    "category_type": category_data["category_type"],
                    "description": category_data["description"],
                    "icon": category_data["icon"],
                    "display_order": category_index,
                    "is_active": True,
                },
            )
            active_category_slugs.append(category.slug)

            for item_index, (name, price, tags) in enumerate(category_data["items"], start=1):
                item_slug = f"{category.slug}-{slugify(name)}"
                FoodItem.objects.update_or_create(
                    slug=item_slug,
                    defaults={
                        "category": category,
                        "name": name,
                        "description": f"{name} from {category.name}.",
                        "search_tags": tags,
                        "price": Decimal(price),
                        "is_from_farm": False,
                        "farm_ingredients": "",
                        "is_featured": category.slug in {"tea-hot-drinks", "coffee", "cold-drinks", "main-meals-whole"},
                        "is_special": "special" in name.lower() or "platter" in name.lower(),
                        "is_active": True,
                        "display_order": item_index,
                        "meta_title": name,
                        "meta_description": f"{name} available at Zamar Springs Gardens dining menu.",
                        "meta_keywords": tags,
                    },
                )
                active_item_slugs.append(item_slug)

        FoodCategory.objects.exclude(slug__in=active_category_slugs).update(is_active=False)
        FoodItem.objects.exclude(slug__in=active_item_slugs).update(is_active=False)

        self.stdout.write(
            self.style.SUCCESS(
                f"Dining catalog synced. Active categories: {len(active_category_slugs)} | Active items: {len(active_item_slugs)}"
            )
        )
