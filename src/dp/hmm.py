# def viterbi(input_file):
# print(f"Viterbi algorithm ready for {input_file}")

def viterbi(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    n_states = int(lines[0])
    n_obs = int(lines[1])
    
    # Read matrices
    trans = [list(map(float, lines[2+i].split())) for i in range(n_states)]
    emit = list(map(float, lines[2+n_states].split()))
    obs = [int(c) for c in lines[2+n_states+1]]
    
    n_steps = len(obs)
    
    # v[s][t] stores max probability of being in state s at time t
    v = [[0.0] * n_steps for _ in range(n_states)]
    # ptr[s][t] stores the previous state that maximized the probability
    ptr = [[0] * n_steps for _ in range(n_states)]
    
    # Initialization (t = 0) - assume uniform start probability (0.5)
    for s in range(n_states):
        p_emit = emit[s] if obs[0] == 1 else (1 - emit[s])
        v[s][0] = (1.0 / n_states) * p_emit
        ptr[s][0] = -1
        
    # Induction (t = 1 to n_steps - 1)
    for t in range(1, n_steps):
        for s in range(n_states):
            max_prob = -1.0
            best_prev = -1
            
            for prev_s in range(n_states):
                prob = v[prev_s][t-1] * trans[prev_s][s]
                if prob > max_prob:
                    max_prob = prob
                    best_prev = prev_s
                    
            p_emit = emit[s] if obs[t] == 1 else (1 - emit[s])
            v[s][t] = max_prob * p_emit
            ptr[s][t] = best_prev
            
    # Termination - find the best final state
    best_final_state = 0
    max_final_prob = v[0][n_steps - 1]
    for s in range(1, n_states):
        if v[s][n_steps - 1] > max_final_prob:
            max_final_prob = v[s][n_steps - 1]
            best_final_state = s
            
    # Backtracking
    path = [0] * n_steps
    path[n_steps - 1] = best_final_state
    for t in range(n_steps - 1, 0, -1):
        path[t - 1] = ptr[path[t]][t]
        
    # Format output (0 = Coin X, 1 = Coin Y)
    result_str = "".join(str(s) for s in path)
    print(f"[HMM VITERBI] Most likely state sequence for {input_file}:")
    print(result_str)