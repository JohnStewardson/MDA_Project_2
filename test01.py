import pandas as pd
import geopandas as gpd
import io
import pickle
import contextily as ctx
from matplotlib import pyplot as plt
import shapely
import numpy as np
import os


#Importing one Location file


def read_metadata(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Extracting user ID from the first line
        user_id = lines[0].split(': ')[1].strip()
        # Extracting recording ID from the last line
        recording_id = lines[-1].split(': ')[1].strip()
    return user_id, recording_id

def create_location_dataframe(folder_path):
    # Define column names based on the structure of the Location.txt file
    columns = ["Time_ms", "Accuracy", "Latitude", "Longitude", "Altitude"]

    # Read the file into a DataFrame, specifying column names and skipping the first two columns
    location_file_path = os.path.join(folder_path, "Torso_Location.txt")
    df = pd.read_csv(location_file_path, sep=' ', header=None, names=columns, usecols=[0, 3, 4, 5, 6])

    # Read metadata from 00inf.txt file
    inf_file_path = os.path.join(folder_path, "00inf.txt")
    user_id, recording_id = read_metadata(inf_file_path)

    # Add user ID and recording ID as new columns to the DataFrame
    df['User_ID'] = user_id
    df['Recording_ID'] = recording_id

    return df

folder_path = "data_moodle/User1/220617"

# Create DataFrame from Location.txt and add metadata
location_df = create_location_dataframe(folder_path)

# Display the DataFrame
#print(location_df.head)

# Function to create DataFrame for each folder in User1 and concatenate them
def create_combined_dataframe(user_folder_path):
    df_total = pd.DataFrame()
    # Iterate through each folder in User1 directory
    for folder_name in os.listdir(user_folder_path):
        folder_path = os.path.join(user_folder_path, folder_name)
        # Check if the item is a directory
        if os.path.isdir(folder_path):
            # Create DataFrame for the current folder
            df_temp = create_location_dataframe(folder_path)
            df_total = pd.concat([df_total, df_temp])


    return df_total

# Folder path containing User1 data
user1_folder_path = "data_moodle/User1"

# Create combined DataFrame for all folders in User1
df_location_1 = create_combined_dataframe(user1_folder_path)


#65012 rows,