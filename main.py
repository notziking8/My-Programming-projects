import csv


def loadPetstore():
    inventory = dict()
    try:
        with open('PetStore.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row['Category']
                pet_info = {
                    'Pet_Name': row['Pet_Name'],
                    'Size': row.get('Size', ''),
                    'Weight': float(row['Weight']),
                    'Color': row['Color'],
                    'Habitat': row.get('Habitat', ''),
                    'Is_Constrictor': bool(row.get('Is_Constrictor', False)),
                    'Has_Frill': bool(row.get('Has_Frill', False)),
                    'Has_Spikes': bool(row.get('Has_Spikes', False)),
                    'Location': row['Location'],
                    'Quantity': int(row['Quantity']),
                    'Price': float(row['Price'])
                }
                if category not in inventory:
                    inventory[category] = []
                inventory[category].append(pet_info)
    except FileNotFoundError:
        print("PetStore.csv not found. Setting up the pet store...")
        inventory = setupStore()
        savePetstore(inventory)
    return inventory


def savePetstore(inventory):
    with open('PetStore.csv', mode='w', newline='') as file:
        fieldnames = ['Category', 'Pet_Name', 'Size', 'Weight', 'Color', 'Habitat',
                      'Is_Constrictor', 'Has_Frill', 'Has_Spikes', 'Location', 'Quantity', 'Price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for category, pets in inventory.items():
            for pet in pets:
                writer.writerow({
                    'Category': category,
                    'Pet_Name': pet['Pet_Name'],
                    'Size': pet['Size'],
                    'Weight': pet['Weight'],
                    'Color': pet['Color'],
                    'Habitat': pet['Habitat'],
                    'Is_Constrictor': pet['Is_Constrictor'],
                    'Has_Frill': pet['Has_Frill'],
                    'Has_Spikes': pet['Has_Spikes'],
                    'Location': pet['Location'],
                    'Quantity': pet['Quantity'],
                    'Price': pet['Price']
                })
