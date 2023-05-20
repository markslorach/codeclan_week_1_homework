import pdb

# test 1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# test 2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# test 3 and 4
def add_or_remove_cash(pet_shop, total_cash):
    pet_shop["admin"]["total_cash"] += total_cash

# test 5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# test 6
def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

# test 7
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# test 8 and 9
def get_pets_by_breed(pet_shop, pet_name):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_name:
            pets.append(pet)

    return pets

# test 10 and 11
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        

# test 12
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)