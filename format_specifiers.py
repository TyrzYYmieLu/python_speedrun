# format specifiers = {value:flags} format a value based on what flags are inserted

price = 3.14159
price2 = price * 1000


# .(number)f = found to that many decimal places (fixed point)

    # print(f"Price is {price.2f}")
    # output: Price is 3.14 

# :(number)  = allocate taht many spaces

    # print(f"Price is {price:10}")
    # output: Price is    3.14159 

# :03        = allocate and zero pad that many spaces

    # print(f"Price is {price:010}")
    # output: Price is 0003.14159 

# :<         = left justify

    # print(f"Price is {price:<10}")
    # output: Price is 3.14159   

# :>         = right justify (this is default behaviour?)

    # print(f"Price is {price:>10}")
    # output: Price is    3.14159 

# :^         = center align

    # print(f"Price is {price:^10}")
    # output: Price is  3.14159 

# :+         = use a plus sign to indicate positive value
    
    # print(f"Price is {price:+10}")
    # output: Price is   +3.14159 

# :=         = place sign to leftmost position

    # print(f"Price is {price:=10}")
    # output: Price is    3.14159

# :          = insert a space before positive numbers

    # print(f"Price is {price:+10}")
    # output: Price is   +3.14159

# :,         = comma separator

    # print(f"Price is {price2:,}")
    # output: Price is 3,141.5899999999997


# combo 
    # print(f"Price is {price2:+,.2f}")
    # output: Price is +3,141.59