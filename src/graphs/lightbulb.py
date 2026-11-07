import sys

def solve_lightbulb(filename):
    # Increase recursion depth for Tarjan's algorithm on large graphs
    sys.setrecursionlimit(2000000)
    
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return
        
    if not lines:
        return
        
    N = int(lines[0])
    M = int(lines[1])
    
    # Graph: 2N nodes. Node 2*i is positive literal, 2*i+1 is negative literal
    graph = [[] for _ in range(2 * N)]
    
    def get_node(val):
        if val > 0:
            return 2 * (val - 1)       # Positive literal
        else:
            return 2 * (-val - 1) + 1  # Negative literal
            
    def neg_node(node):
        return node ^ 1 # Flips the last bit (0->1, 1->0)

    # Build implication graph
    for i in range(2, 2 + M):
        if i >= len(lines): break
        parts = list(map(int, lines[i].split()))
        if len(parts) < 2: continue
        
        u, v = parts[0], parts[1]
        u_node = get_node(u)
        v_node = get_node(v)
        
        # Clause (u OR v) -> (~u -> v) and (~v -> u)
        graph[neg_node(u_node)].append(v_node)
        graph[neg_node(v_node)].append(u_node)
        
    # Tarjan's SCC Algorithm
    index = 0
    stack = []
    on_stack = [False] * (2 * N)
    indices = [-1] * (2 * N)
    lowlink = [0] * (2 * N)
    scc_id = [-1] * (2 * N)
    scc_count = 0
    
    def strongconnect(v):
        nonlocal index, scc_count
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True
        
        for w in graph[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])
                
        if lowlink[v] == indices[v]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc_id[w] = scc_count
                if w == v:
                    break
            scc_count += 1

    for i in range(2 * N):
        if indices[i] == -1:
            strongconnect(i)
            
    # Check for conflicts
    for i in range(N):
        pos_node = 2 * i
        neg_node = pos_node + 1
        if scc_id[pos_node] == scc_id[neg_node]:
            print(f"[SAT SOLVER] Instance {filename}: NO SOLUTION (Logical Conflict on switch {i+1})")
            return
            
    # Construct solution
    solution = []
    for i in range(N):
        pos_node = 2 * i
        neg_node = pos_node + 1
        if scc_id[pos_node] > scc_id[neg_node]:
            solution.append(i + 1)  # Switch is UP
        else:
            solution.append(-(i + 1)) # Switch is DOWN
            
    print(f"[SAT SOLVER] Instance {filename}: SOLUTION FOUND")
    print(" ".join(map(str, solution)))