import matplotlib.pyplot as plt

def generate_graph(data, graph_type='bar'):
    """
    Generates a graph based on the provided data and graph type.

    Parameters:
    - data: A dictionary with labels and values for the graph.
    - graph_type: The type of graph to generate ('bar', 'line', etc.).

    Returns:
    - None
    """
    labels = list(data.keys())
    values = list(data.values())

    if graph_type == 'bar':
        plt.bar(labels, values)
        plt.xlabel('Vrcholy')
        plt.ylabel('Nadmořská výška (m)')
        plt.title('Nadmořské výšky vrcholů')
    elif graph_type == 'line':
        plt.plot(labels, values, marker='o')
        plt.xlabel('Vrcholy')
        plt.ylabel('Nadmořská výška (m)')
        plt.title('Nadmořské výšky vrcholů')
    else:
        raise ValueError("Unsupported graph type. Use 'bar' or 'line'.")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()