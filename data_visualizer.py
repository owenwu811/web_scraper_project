import matplotlib.pyplot as plt
import pandas as pd
import sys
import logging

# Setup logging
log_filename = '/home/chatgpt/custom_utilities/utility_library/tmp/data_visualizer.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

# Get data file path from command line argument
data_file_path = sys.argv[1]

try:
    # Load the data into a pandas DataFrame
    df = pd.read_csv(data_file_path)

    # Create a bar chart of the data
    df.plot(kind='bar')

    # Save the plot to a file
    plt.savefig('/home/chatgpt/custom_utilities/utility_library/tmp/data_visualization.png')

    # Log a success message
    logging.info(f'Successfully visualized data from {data_file_path}')

except Exception as e:
    # If there's an exception, log an error message
    logging.error(f'Error visualizing data from {data_file_path}: {e}')
