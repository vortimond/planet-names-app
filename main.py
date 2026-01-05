import random

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
random_planet = random.choice(planets)
random_number = planets.index(random_planet)
print("I have selected a planet from eight possible options:")
print(planets)
while True:
    user_planet = input("Tell me which one [q to quit]: ")
    user_planet = user_planet.capitalize()
    if user_planet in planets:
        user_number = planets.index(user_planet)
        if random_number == user_number:
            print("Correct!")
            break
        elif random_number > user_number:
            print("The planet is farther away from the Sun.")
        else:
            print("The planet is closer to the Sun.")
    elif user_planet == "Q":
        break
