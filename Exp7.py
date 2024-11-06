import random

def generate_story():

    subjects = ["A wizard", "An astronaut", "A dragon", "A detective", "A robot", 
                "A princess", "A pirate"]
    verbs = ["found", "lost", "created", "destroyed", "discovered", "chased", 
             "rescued"]
    objects = ["a magic wand", "an ancient artifact", "a hidden treasure", 
               "a mysterious creature", "a secret map", "an alien ship"]
    places = ["in a dark forest", "on a distant planet", "inside a haunted castle", 
              "in an abandoned city", "on a remote island", "in the middle of a battlefield"]

    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    place = random.choice(places)

    story = f"{subject} {verb} {obj} {place}."
    return story

def main():
    print("Welcome to the random story generator.")
    while True:
        user_input = input("Do you want to generate a new story? (yes/no): ").lower()
        if user_input == "yes":
            print(generate_story())
        elif user_input == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

main()
