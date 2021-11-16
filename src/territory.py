territory_neighbors = {
    'Akkala': ["Eldin", "Lanaryu"],
    'Central Hyrule': ["Great Hyrule Forest", "Ridgelands", "Gerudo Highlands", "Gerudo Wastelands", "Great Plateau", "Dueling Peaks", "Lanaryu"],
    'Dueling Peaks': ["Lanaryu", "Central Hyrule", "Great Plateau", "Lake", "Faron", "East Necluda"],
    'East Necluda': ["Lanaryu", "Dueling Peaks", "Faron"],
    'Eldin': ["Great Hyrule Forest", "Lanaryu", "Akkala"],
    'Faron': ["East Necluda", "Dueling Peaks", "Lake"],
    'Gerudo Highlands': ["Tabantha", "Ridgelands", "Gerudo Wastelands", "Central Hyrule"],
    'Gerudo Wastelands': ["Gerudo Highlands", "Lake", "Great Plateau"],
    'Great Hyrule Forest': ["Hebra", "Ridgelands", "Central Hyrule", "Lanaryu", "Eldin"],
    'Great Plateau': ["Central Hyrule", "Gerudo Wastelands", "Lake", "Dueling Peaks"],
    'Hebra': ["Tabantha", "Ridgelands", "Great Hyrule Forest"],
    'Lake': ["Great Plateau", "Gerudo Wastelands", "Faron", "Dueling Peaks"],
    'Lanaryu': ["Akkala", "Eldin", "Great Hyrule Forest", "Central Hyrule", "Dueling Peaks", "East Necluda"],
    'Ridgelands': ["Great Hyrule Forest", "Hebra", "Tabantha", "Gerudo Highlands", "Central Hyrule"],
    'Tabantha': ["Hebra", "Gerudo Highlands", "Ridgelands"]
}

class Territory():
    def __init__(self, name):
        self.name = name
        self.num_armies = 0
        self.occupier = "neutral"
        self.adjacent_territories = territory_neighbors[name]

    def update_territory(army_count, occupier):
        self.num_armies = army_count
        self.occupier = occupier

        