import argparse
import sys

# Import modules
from src.compression import huffman, jabberwocky
from src.dp import hmm, edit_distance
from src.graphs import lightbulb

def main():
    parser = argparse.ArgumentParser(description="Logic-Compress-DP Engine")
    
    parser.add_argument("--module", required=True, 
                        choices=["compress", "dp", "sat"], 
                        help="Select the module to run")
    
    parser.add_argument("--action", required=True, 
                        help="Action to perform (e.g., encode, decode, solve)")
    
    parser.add_argument("--input", required=True, 
                        help="Path to the input file")
    
    parser.add_argument("--output", required=False, 
                        help="Path to the output file (optional)")
    
    parser.add_argument("--codebook", required=False, 
                        help="Path to the codebook (Huffman only)")

    args = parser.parse_args()

    print(f"--- Logic-Compress-DP Engine ---")
    print(f"Module: {args.module} | Action: {args.action}")

    if args.module == "compress":
        if args.action == "huffman_encode":
            huffman.encode(args.input, args.output, args.codebook)
        elif args.action == "huffman_decode":
            huffman.decode(args.input, args.output, args.codebook)
        elif args.action == "jabber_encode":
            jabberwocky.jabber(args.input, args.output)
        elif args.action == "wocky_decode":
            jabberwocky.wocky(args.input, args.output)
            
    elif args.module == "dp":
        if args.action == "edit_distance":
            edit_distance.calculate(args.input)
        elif args.action == "hmm_viterbi":
            hmm.viterbi(args.input)
            
    elif args.module == "sat":
        if args.action == "solve":
            lightbulb.solve_lightbulb(args.input)
            
    else:
        print("Invalid action for this module.")
        sys.exit(1)

if __name__ == "__main__":
    main()