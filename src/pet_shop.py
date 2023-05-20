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
