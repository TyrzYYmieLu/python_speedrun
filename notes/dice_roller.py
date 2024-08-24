import random


#print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

dice_art = {1:("""
            ┌─────────┐
            │         │
            │    ●    │
            │         │
            └─────────┘
            """),

            2:("""
            ┌─────────┐
            │ ●       │
            │         │
            │       ● │
            └─────────┘
            """),

            3:("""
            ┌─────────┐
            │ ●       │
            │    ●    │
            │       ● │
            └─────────┘
            """),

            4:("""
            ┌─────────┐
            │ ●     ● │
            │         │
            │ ●     ● │
            └─────────┘
            """),

            5:("""
            ┌─────────┐
            │ ●     ● │
            │    ●    │
            │ ●     ● │
            └─────────┘
            """),

            6:("""
            ┌─────────┐
            │ ●     ● │
            │ ●     ● │
            │ ●     ● │
            └─────────┘
            """)}

# user can as for 1 to 3 dice to roll at the same time
# roll dice remember to leave space for each of them
# ouput the dice in ASCII art
