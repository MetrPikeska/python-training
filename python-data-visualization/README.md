# Python Data Visualization Project

## Overview
This project is designed to visualize data related to mountain peaks and their elevations using Python. It includes functionalities for loading data from a CSV file, generating various types of graphs, and providing a clear structure for data analysis.

## Project Structure
```
python-data-visualization
├── src
│   ├── main.py              # Entry point of the application
│   ├── data_loader.py       # Functions for loading data from CSV
│   ├── graph_generator.py    # Functions for generating graphs
│   └── utils
│       └── __init__.py      # Utility functions and constants
├── data
│   └── beskydy.csv          # Data file containing mountain peaks and elevations
├── outputs
│   └── .gitkeep             # Keeps the outputs directory in the Git repository
├── requirements.txt          # List of dependencies for the project
├── README.md                 # Documentation for the project
└── .gitignore                # Files and directories to be ignored by Git
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-data-visualization
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

This will load the data from `data/beskydy.csv` and generate the specified graphs.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.