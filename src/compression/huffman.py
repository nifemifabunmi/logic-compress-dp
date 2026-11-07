import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            c1 = self.char if self.char is not None else ''
            c2 = other.char if other.char is not None else ''
            return c1 < c2
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1
        
    forest = []
    for char, freq in freq_map.items():
        heapq.heappush(forest, Node(char, freq))
        
    while len(forest) > 1:
        left = heapq.heappop(forest)
        right = heapq.heappop(forest)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(forest, parent)
    return forest[0]

def get_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    if root is None:
        return codes
    if root.char is not None:
        codes[root.char] = current_code
    get_codes(root.left, current_code + "0", codes)
    get_codes(root.right, current_code + "1", codes)
    return codes

def encode(input_file, output_file, codebook_file=None):
    with open(input_file, 'r') as f:
        text = f.read()
        
    root = build_huffman_tree(text)
    codes = get_codes(root)
    
    # Save codebook if requested
    if codebook_file:
        with open(codebook_file, 'w') as f:
            for char, code in codes.items():
                f.write(f"{ord(char)} {code}\n")
                
    bit_string = "".join(codes[char] for char in text)
    with open(output_file, 'w') as f:
        f.write(bit_string)
    print(f"Huffman encoded successfully to {output_file}")

def decode(input_file, output_file, codebook_file):
    codes = {}
    with open(codebook_file, 'r') as f:
        for line in f:
            if line.strip():
                char_int, code = line.split()
                codes[code] = chr(int(char_int))
                
    with open(input_file, 'r') as f:
        bits = f.read().strip()
        
    output = ""
    current_code = ""
    for bit in bits:
        current_code += bit
        if current_code in codes:
            output += codes[current_code]
            current_code = ""
            
    with open(output_file, 'w') as f:
        f.write(output)
    print(f"Huffman decoded successfully to {output_file}")