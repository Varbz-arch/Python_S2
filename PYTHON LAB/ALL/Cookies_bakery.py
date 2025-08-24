#RANDOM
def cookie_machine(sugar, flour):
    print(f"Baking with {sugar}g sugar and {flour}g flour...")
    cookies = (sugar + flour) // 10
    return cookies
jar = cookie_machine(50, 70)  # 50g sugar, 70g flour
print(f"You got {jar} cookies! 🍪")
def cookie_machine(sugar, flour):
    print(f"Mixing {sugar}g sugar and {flour}g flour... 🍚🌾")
    cookies = (sugar + flour) // 10
    print("Baking... 🔥")
    return cookies

print("Welcome to your bakery! 🧁")

sugar_stock = int(input("Enter sugar in grams: "))
flour_stock = int(input("Enter flour in grams: "))

batch = cookie_machine(sugar_stock, flour_stock)
print(f"You baked {batch} cookies! Enjoy! 🍪🍪🍪")
def cookie_machine(sugar, flour, flavor="chocolate"):
    print(f"Baking {flavor} cookies... 🍫🍓🍪")
    return (sugar + flour) // 10

batch = cookie_machine(60, 90, "strawberry")
print(f"Fresh batch: {batch} strawberry cookies! 🍓🍪")
