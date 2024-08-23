import subprocess
import re
import os
import cowsay

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Display a greeting using cowsay with a random fortune or quote
    display_greeting()

    while True:
        usr_input = input("\n\nUnit conversion (type (q) to quit): ").strip().lower()
        if usr_input in {"q"}:
            break
        
        clear_screen()
        
        if is_valid(usr_input):
            value, from_unit, to_unit = parse_input(usr_input)
            result = convert_units(value, from_unit, to_unit)
            cowsay.cow(f"{value}{from_unit} is {result:.2f}{to_unit}")
        else:
            cowsay.cow("Invalid input. Please try again.")

def display_greeting():
    try:
        # Use fortune if available
        fortune = subprocess.run(["fortune"], capture_output=True, text=True)
        clear_screen()
        cowsay.cow(fortune.stdout.strip())
    except FileNotFoundError:
        # Fallback greeting message
        clear_screen()
        cowsay.cow("What would you like to convert today?")

def is_valid(usr_input):
    # Supported units for conversion
    supported_units = {'kg', 'lb'}

    # Regex pattern for matching conversion requests like "1 kg to lbs" or "convert 1kg to lbs"
    pattern = r"(\d+)\s*(kg|lb)\s*(to|in)\s*(kg|lb)"

    match = re.match(pattern, usr_input)
    if match:
        from_unit = match.group(2)
        to_unit = match.group(4)
        return from_unit in supported_units and to_unit in supported_units and from_unit != to_unit
    
    return False

def parse_input(usr_input):
    # Extract the numeric value, the from-unit, and the to-unit
    pattern = r"(\d+)\s*(kg|lb)\s*(to|in)\s*(kg|lb)"
    match = re.match(pattern, usr_input)
    
    if match:
        value = int(match.group(1))
        from_unit = match.group(2)
        to_unit = match.group(4)
        return value, from_unit, to_unit

def convert_units(value, from_unit, to_unit):
    # Conversion factors
    conversions = {
        'kg_to_lb': 2.20462,
        'lb_to_kg': 0.453592
    }
    
    if from_unit == 'kg' and to_unit == 'lb':
        return value * conversions['kg_to_lb']
    elif from_unit == 'lb' and to_unit == 'kg':
        return value * conversions['lb_to_kg']
    else:
        raise ValueError("Unsupported conversion")

if __name__ == "__main__":
    main()
