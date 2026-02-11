from django.shortcuts import render


def overview(request):
    kids_activities = [
        {"name": "Soft Archery", "icon": "fas fa-bullseye", "desc": "Safe target play with guided rules."},
        {"name": "Holla Hoop", "icon": "fas fa-circle-notch", "desc": "Fun rhythm movement challenge."},
        {"name": "Skipping Ropes", "icon": "fas fa-link", "desc": "Active jumping sessions for energy."},
        {"name": "Bouncing Castle", "icon": "fas fa-house", "desc": "High-energy jumping in a soft zone."},
        {"name": "Trampoline", "icon": "fas fa-arrows-up-down", "desc": "Controlled bounce play for kids."},
        {"name": "Badminton", "icon": "fas fa-table-tennis-paddle-ball", "desc": "Light court play for all ages."},
        {"name": "Cards", "icon": "fas fa-clone", "desc": "Simple card games with animator support."},
        {"name": "Swings and Slides", "icon": "fas fa-child-reaching", "desc": "Classic outdoor playground fun."},
        {"name": "Darts", "icon": "fas fa-location-crosshairs", "desc": "Soft target accuracy play."},
        {"name": "Face Painting", "icon": "fas fa-palette", "desc": "Creative face art for themed fun."},
        {"name": "Canvas Painting", "icon": "fas fa-paintbrush", "desc": "Guided painting activities for kids."},
        {"name": "Football", "icon": "fas fa-futbol", "desc": "Open play field sessions."},
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
        "kids_activities": kids_activities,
        "family_activities": family_activities,
    }
    return render(request, "kids/overview.html", context)
