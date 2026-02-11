from django.shortcuts import render


def overview(request):
    kids_play_images = [
        "/static/images/web-pictures/kids-outdoor-games-machakos-1.webp",
        "/static/images/web-pictures/kids-outdoor-games-machakos-2.webp",
        "/static/images/web-pictures/outdoor-kids-playarea-1.webp",
        "/static/images/web-pictures/outdoor-kids-playarea-2.webp",
    ]

    hero_images = [
        kids_play_images[0],
        kids_play_images[1],
        kids_play_images[2],
    ]

    kids_activities = [
        {"name": "Soft Archery", "icon": "fas fa-bullseye", "desc": "Safe target play with guided rules.", "image": kids_play_images[0]},
        {"name": "Holla Hoop", "icon": "fas fa-circle-notch", "desc": "Fun rhythm movement challenge.", "image": kids_play_images[1]},
        {"name": "Skipping Ropes", "icon": "fas fa-link", "desc": "Active jumping sessions for energy.", "image": kids_play_images[2]},
        {"name": "Bouncing Castle", "icon": "fas fa-house", "desc": "High-energy jumping in a soft zone.", "image": kids_play_images[3]},
        {"name": "Trampoline", "icon": "fas fa-arrows-up-down", "desc": "Controlled bounce play for kids.", "image": kids_play_images[0]},
        {"name": "Badminton", "icon": "fas fa-table-tennis-paddle-ball", "desc": "Light court play for all ages.", "image": kids_play_images[1]},
        {"name": "Cards", "icon": "fas fa-clone", "desc": "Simple card games with animator support.", "image": kids_play_images[2]},
        {"name": "Swings and Slides", "icon": "fas fa-child-reaching", "desc": "Classic outdoor playground fun.", "image": kids_play_images[3]},
        {"name": "Darts", "icon": "fas fa-location-crosshairs", "desc": "Soft target accuracy play.", "image": kids_play_images[0]},
        {"name": "Face Painting", "icon": "fas fa-palette", "desc": "Creative face art for themed fun.", "image": kids_play_images[1]},
        {"name": "Canvas Painting", "icon": "fas fa-paintbrush", "desc": "Guided painting activities for kids.", "image": kids_play_images[2]},
        {"name": "Football", "icon": "fas fa-futbol", "desc": "Open play field sessions.", "image": kids_play_images[3]},
    ]

    family_images = [
        kids_play_images[0],
        kids_play_images[1],
    ]

    family_activities = [
        {"name": "Soft Archery", "icon": "fas fa-bullseye", "desc": "Family target challenges."},
        {"name": "Darts", "icon": "fas fa-location-crosshairs", "desc": "Relaxed scoring games for groups."},
        {"name": "Table Tennis", "icon": "fas fa-table-tennis-paddle-ball", "desc": "Friendly match play."},
        {"name": "Sand Bags and Bean Bags", "icon": "fas fa-bag-shopping", "desc": "Casual toss-and-score fun."},
        {"name": "Card Games", "icon": "fas fa-clone", "desc": "Tabletop bonding activities."},
        {"name": "Badminton", "icon": "fas fa-shuttlecock", "desc": "Outdoor doubles and family rounds."},
        {"name": "Table Football", "icon": "fas fa-gamepad", "desc": "Quick competitive foosball rounds."},
        {"name": "Other Recreational Activities", "icon": "fas fa-person-running", "desc": "Flexible activities for mixed groups."},
    ]

    context = {
        "hero_images": hero_images,
        "kids_activities": kids_activities,
        "family_images": family_images,
        "family_activities": family_activities,
    }
    return render(request, "kids/overview.html", context)
