import random

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
selected_planet = random.choice(planets)
print("I have selected a planet from eight possible options:")
print(planets)
while True:
    user_input = input("Tell me which one [q to quit]: ")
    if user_input == "q":
        break
    elif user_input == selected_planet:
        print("Correct!")
        break
