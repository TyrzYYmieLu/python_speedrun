# Concession stand program

menu = {"pizza": 3.00,
        "popcorn": 2.50,
        "soda": 1.50,
        "candy": 1.0}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")