print("Fertilizer Calculator")

# The amount of fertilizer needed for each crop is different
# Common crop and their fertilizer rate (kg per acre)
crop_rates = {
    "maize": 100,
    "rice": 120,
    "yam": 90,
    "cassava": 80
}

print("Available Crops: maize, rice, cassva, yam")
# Farmer Information
farmer_name = input("Enter farmer name: ")
crop_type = input("Enter crop type: "). lower()
farm_size = float(input("Enter farm size in acres: "))
bag_size = float(input("Enter bag size in your area (e.g 25 or 50): "))
price_per_bag = float(input("Enter price of one bag in your area: "))

# Calculation
rate = crop_rates[crop_type]
total_kg = farm_size * rate
bags_needed = total_kg / bag_size
total_cost = price_per_bag * bags_needed

# Result
print(" \n Result ")
print(farmer_name + ", you need " + str(total_kg) +
      " kg of fertilizer for " + crop_type)
print(f"That is {bags_needed} bags of {bag_size} kg")
print(f"Total cost in your location N{total_cost}")
