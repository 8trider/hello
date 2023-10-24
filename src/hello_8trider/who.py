def my_name():
    print("My name is H8 ")

def lotto():
    import random
    numbers = list(range(1, 43))
    random_numbers = random.sample(numbers, 6)
    print(random_numbers)

def chant():
    import random
    chants = ["HAVE A NICE DAY",
              "KEEP IT UP",
              "GOOD LUCK",
              "ALL IS WELL",
              "CHEER UP",
              "NEVER GIVE UP",
              "TAKE IT EASY",
              "YOU CAN DO IT",
              "YOU CAN MAKE IT",
              "NOTHING CAN'T STOP YOU"
            ]
    
    chant = f"{random.choice(chants)}"
    result = print(chant)
    
    return result
