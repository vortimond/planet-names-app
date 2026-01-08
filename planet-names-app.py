import random

_line = "_" * 80
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
moons = [0, 0, 1, 2, 95, 274, 28, 16]
attempts = 0
random_planet = random.choice(planets)
random_number = planets.index(random_planet)
print(_line)
print(" PLANET NAMES APP")
print("\n I have selected a planet from eight possible options:")
print(" Planets in our solar system:")
print(f" {planets}")
print(_line)

# Read the previous results from a file
print("Your previous results:")
try:
    with open('planet-names-app.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("No saved results.")
print(_line)

while True:
    user_planet = input("\nTell me which one ['q' to quit]: ")
    user_planet = user_planet.capitalize()
    attempts += 1
    if user_planet in planets:
        user_number = planets.index(user_planet)
        if random_number == user_number:
            print("Correct!")
            print(f"The selected planet was: {random_planet}")
            print(f"Note: The planet {random_planet} has {moons[random_number]} moon(s).")
            print(f"You needed {attempts} attempts.")

            # Save the results into a file and exit the app
            with open('planet-names-app.txt', 'a') as file:
                file.write(f"Attempts = {attempts} | Planet = {random_planet}\n")
            break
        elif random_number > user_number:
            print("The planet is farther away from the Sun.")
        else:
            print("The planet is closer to the Sun.")
    elif user_planet == "Q":
        break
    else:
        print(f"'{user_planet}' is not a planet.")
