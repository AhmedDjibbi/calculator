from calculation import calculate

def evaluate_tokens(tokens):
    tokens = between_parenthesis(tokens)
    tokens = power(tokens)
    tokens = square_root(tokens)
    tokens = mul_div(tokens)
    tokens = normal_cal(tokens)
    return tokens

def between_parenthesis(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '(':
            start = i
            count = 1
            j = i + 1
            while j < len(tokens):
                if tokens[j] == '(':
                    count += 1
                elif tokens[j] == ')':
                    count -= 1
                    if count == 0:
                        break
                j += 1
            
            if j < len(tokens):
                sub_tokens = tokens[start+1 : j]
                sub_result = evaluate_tokens(sub_tokens)
                if len(sub_result) == 1:
                    tokens[start] = sub_result[0]
                    del tokens[start+1 : j+1]
                    i = start
                else:
                    return ["ERROR: Invalid input"]
            else:
                return ["ERROR: Invalid input"]
        elif tokens[i] == ')':
            return ["ERROR: Invalid input"]
        i += 1
    return tokens

def power(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '**':
            if i - 1 < 0 or i + 1 >= len(tokens):
                return ["ERROR: Invalid input"]
            result = calculate(tokens[i-1 : i+2])
            if isinstance(result, str) and result.startswith("ERROR"):
                return [result]
            tokens[i-1] = result
            del tokens[i : i+2]
            continue
        i += 1
    return tokens

def square_root(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '//':
            if i - 1 < 0:
                return ["ERROR: Invalid input"]
            result = calculate(tokens[i-1 : i+1])
            if isinstance(result, str) and result.startswith("ERROR"):
                return [result]
            tokens[i-1] = result
            del tokens[i]
            continue
        i += 1
    return tokens

def mul_div(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] in ['*', '/', '%']:
            if i - 1 < 0 or i + 1 >= len(tokens):
                return ["ERROR: Invalid input"]
            result = calculate(tokens[i-1 : i+2])
            if isinstance(result, str) and result.startswith("ERROR"):
                return [result]
            tokens[i-1] = result
            del tokens[i : i+2]
            continue
        i += 1
    return tokens

def normal_cal(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] in ['+', '-']:
            if i - 1 < 0 or i + 1 >= len(tokens):
                return ["ERROR: Invalid input"]
            result = calculate(tokens[i-1 : i+2])
            if isinstance(result, str) and result.startswith("ERROR"):
                return [result]
            tokens[i-1] = result
            del tokens[i : i+2]
            continue
        i += 1
    return tokens