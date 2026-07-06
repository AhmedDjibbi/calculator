def analyse_input (input_string):
    tokens = []
    i = 0
    while i < len(input_string):
        if input_string[i] == ' ':
            i+=1
            continue
        elif input_string[i:i+2] in ['**', '//']:
            tokens.append(input_string[i:i+2])
            i+=2
        elif input_string[i] in ['+', '-', '*', '/', '%']:
            tokens.append(input_string[i])
            i+=1
        elif input_string[i] in ['(' , ')']:
            tokens.append(input_string[i])
            i+=1
        elif input_string[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num_str = ''
            while i < len(input_string) and input_string[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                num_str += input_string[i]
                i+=1
            try:
                tokens.append(float(num_str))
            except ValueError:
                return "ERROR: Invalid input"
        else:
            return "ERROR: Invalid input"
    return tokens