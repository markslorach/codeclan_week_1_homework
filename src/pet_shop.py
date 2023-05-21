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

# test 13
def add_pet_to_stock(pet_shop, new_pet):
     pet_shop["pets"].append(new_pet)

# test 14
def get_customer_cash(customer_cash):
    return customer_cash["cash"]

# test 15
def remove_customer_cash(customer, cash_amount):
    customer["cash"] -= cash_amount

# test 16
def get_customer_pet_count(pet_count):
    return len(pet_count["pets"])

# test 17
def add_pet_to_customer(customer_pets, new_pet):
    customer_pets["pets"].append(new_pet)

# extension 1, 2 and 3
# def customer_can_afford_pet(customer_cash, pet_price):
#     if customer_cash["cash"] >= pet_price["price"]:
#         return True
#     else:
#         False

def customer_can_afford_pet(customer_cash, pet_price):
    return customer_cash["cash"] >= pet_price["price"]

# integration test
def sell_pet_to_customer(pet_shop, pet, customer):
    # if there is a pet in the shop and the customer has enough cash
    if pet in pet_shop["pets"] and customer["cash"] >= pet["price"]:
        #remove the pet from the shop
        pet_shop["pets"].remove(pet)
        # add 1 pet to the total pets sold
        pet_shop["admin"]["pets_sold"] += 1
        # add pet price to total cash
        pet_shop["admin"]["total_cash"] += pet["price"]
        # add pet to customer
        customer["pets"].append(pet)
        # subtract pet price from customer cash
        customer["cash"] -= pet["price"]
