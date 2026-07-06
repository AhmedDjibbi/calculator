from parcer import analyse_input
from priority import between_parenthesis,power,mul_div,normal_cal,square_root

while True:
    try:
        input_string = input("Enter a calculation: ")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting...")
        break
        
    if input_string.strip() == "exit":
        break
        
    tokens = analyse_input(input_string)
    if isinstance(tokens, str) and tokens.startswith("ERROR"):
        print(tokens)
        continue
        
    tokens = between_parenthesis(tokens)
    tokens = power(tokens)
    tokens = square_root(tokens)
    tokens = mul_div(tokens)
    tokens = normal_cal(tokens)
    
    if len(tokens) == 1:
        val = tokens[0]
        if isinstance(val, float):
            if val.is_integer():
                print(int(val))
            else:
                print(val)
        else:
            print(val)
    else:
        print("ERROR: Invalid input")
    
    
        