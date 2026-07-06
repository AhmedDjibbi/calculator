from operations import add,sub,mul,div,power,mod,squareroot
def calculate (tokens):
    i=0
    while i<len(tokens):
        if tokens[i] =='+':
            tokens[i] = add(tokens[i-1],tokens[i+1])
            del tokens[i+1]
            del tokens[i-1]
            i = 0
            continue
        elif tokens[i] =='-':
            tokens[i] = sub(tokens[i-1],tokens[i+1])
            del tokens[i+1]
            del tokens[i-1]
            i = 0
            continue
        elif tokens[i] =='*':
            tokens[i] = mul(tokens[i-1],tokens[i+1])
            del tokens[i+1]
            del tokens[i-1]
            i = 0
            continue
        elif tokens[i] =='/':
            tokens[i] = div(tokens[i-1],tokens[i+1])
            del tokens[i+1]
            del tokens[i-1]
            i = 0
            continue
        elif tokens[i] =='%':
            tokens[i] = mod(tokens[i-1],tokens[i+1])
            del tokens[i+1]
            del tokens[i-1]
            i = 0
            continue
        elif tokens[i] == '**':
            tokens[i] = power(tokens[i-1],tokens[i+1])
            del tokens[i+1]
            del tokens[i-1]
            i = 0
            continue
        elif tokens[i] == '//':
            tokens[i] = squareroot(tokens[i-1])
            del tokens[i-1]
            i = 0
            continue
        i+=1
    return tokens[0]
        