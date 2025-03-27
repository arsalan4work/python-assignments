MERCURY = 0.376
VENUS = 0.889
MARS = 0.378
JUPITER = 2.36
SATURN = 1.081
URANUS = 0.815
NEPTUNE = 1.14

def main():
    weight_on_earth:float = float(input("Enter your weight on Earth (in kg): "))
    planet_to_choose = input("Enter a planet to choose(mercury, venus, mars, jupiter, saturn, uranus, neptune): ")
    # Mercury
    if planet_to_choose == "mercury":
        weight_on_mercury = weight_on_earth * MERCURY
        print(f"Your weight on mercury is {weight_on_mercury:.2f}")
    # Venus
    elif planet_to_choose == "venus":
        weight_on_venus = weight_on_earth * VENUS
        print(f"Your weight on venus is {weight_on_venus:.2f}")
    # Mars
    elif planet_to_choose == "mars":
        weight_on_mars = weight_on_earth * MARS
        print(f"Your weight on mars is {weight_on_mars:.2f}")
    # Jupiter
    elif planet_to_choose == "jupiter":
        weight_on_jupiter = weight_on_earth * JUPITER
        print(f"Your weight on jupiter is {weight_on_jupiter:.2f}")
    # Saturn
    elif planet_to_choose == "saturn":
        weight_on_saturn = weight_on_earth * SATURN
        print(f"Your weight on saturn is {weight_on_saturn:.2f}")
    # Uranus
    elif planet_to_choose == "uranus":
        weight_on_uranus = weight_on_earth * URANUS
        print(f"Your weight on uranus is {weight_on_uranus:.2f}")
    # Neptune
    elif planet_to_choose == "neptune":
        weight_on_neptune = weight_on_earth * NEPTUNE
        print(f"Your weight on neptune is {weight_on_neptune:.2f}")

    else:
        print("Error! Please Write Correct Name!")

if __name__ == "__main__":
    main()