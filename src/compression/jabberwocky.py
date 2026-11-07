def jabber(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read().strip()
        
    T = {"": 0}
    next_index = 1
    W = 0
    output = ""
    i = 0
    
    while i < len(text):
        prefix = ""
        j = i
        while j < len(text) and (prefix + text[j]) in T:
            prefix += text[j]
            j += 1
            
        if j == len(text):
            if W > 0:
                output += format(T[prefix], f'0{W}b')
            break
            
        next_bit = text[j]
        index = T[prefix]
        
        if W > 0:
            output += format(index, f'0{W}b')
        output += next_bit
        
        T[prefix + next_bit] = next_index
        next_index += 1
        
        if len(T) > 1 and (len(T) & (len(T) - 1)) == 0:
            W += 1
        i = j
        
    with open(output_file, 'w') as f:
        f.write(output)
    print(f"Jabberwocky encoded successfully to {output_file}")

def wocky(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read().strip()
        
    T = {0: ""}
    next_index = 1
    W = 0
    output = ""
    i = 0
    
    while i < len(text):
        if len(text) - i < W + 1:
            if len(text) - i == W and W > 0:
                index = int(text[i:i+W], 2)
                if index in T:
                    output += T[index]
            break
            
        index = 0
        if W > 0:
            index = int(text[i:i+W], 2)
        i += W
        
        next_bit = text[i]
        i += 1
        
        prefix = T[index]
        decoded_string = prefix + next_bit
        output += decoded_string
        
        T[next_index] = decoded_string
        next_index += 1
        
        if len(T) > 1 and (len(T) & (len(T) - 1)) == 0:
            W += 1
            
    with open(output_file, 'w') as f:
        f.write(output)
    print(f"Jabberwocky decoded successfully to {output_file}")