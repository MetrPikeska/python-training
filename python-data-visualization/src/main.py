import pandas as pd
from data_loader import load_data
from graph_generator import generate_graph

def main():
    # Načtení dat
    data = load_data("data/beskydy.csv")
    
    # Generování grafu
    generate_graph(data, graph_type='bar')

if __name__ == "__main__":
    main()