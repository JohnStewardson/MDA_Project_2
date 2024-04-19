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


def create_motion_dataframe(folder_path):
    # Define column names based on the structure of the Torso_Motion file
    columns = ["Time", "Acc_x", "Acc_y", "Acc_z", "Gyro_x", "Gyro_y", "Gyro_z",
               "Magnetometer_X", "Magnetometer_Y", "Magnetometer_Z", "Orientation_w", "Orientation_x", "Orientation_y",
               "Orientation_z",
               "Gravity_x", "Gravity_y", "Gravity_z", "Linear_acc_x", "Linear_acc_y",
               "Linear_acc_z", "Pressure", "Altitude", "Temperature"]

    # Read the file into a DataFrame, specifying column names
    motion_file_path = os.path.join(folder_path, "Torso_Motion.txt")
    df = pd.read_csv(motion_file_path, sep=' ', header=None, names=columns)

    return df


def create_combined_dataframe_motion(user_folder_path):
    df_total = pd.DataFrame()
    # Iterate through each folder in User1 directory
    for folder_name in os.listdir(user_folder_path):
        folder_path = os.path.join(user_folder_path, folder_name)
        # Check if the item is a directory
        if os.path.isdir(folder_path):
            # Create DataFrame for the current folder
            df_temp = create_motion_dataframe(folder_path)

            df_total = pd.concat([df_total, df_temp])

    return df_total
# Display the DataFrame

# Exemplary dictionary mapping activity labels to strings (you can adjust as needed)
activity_mapping = {
    0: "Still, Stand, Outside",
    1: "Still, Stand, Inside",
    2: "Still, Sit, Outside",
    3: "Still, Sit, Inside",
    4: "Walking, Inside",
    5: "Walking, Outside",
    6: "Run",
    7: "Bike",
    8: "Car, Driver",
    9: "Car, Passenger",
    10: "Bus, Stand",
    11: "Bus, Sit",
    12: "Bus, Up, Stand",
    13: "Bus, Up, Sit",
    14: "Train, Stand",
    15: "Train, Sit",
    16: "Subway, Stand",
    17: "Subway, Sit"
}

# Function to read labels data from file and create DataFrame with activity labels as strings
def create_labels_dataframe(folder_path, activity_mapping):
    # Define column names based on the structure of the labels_track_main.txt file
    columns = ["Start_time", "End_time", "Activity_label"]

    # Read the file into a DataFrame, specifying column names
    labels_file_path = os.path.join(folder_path, "labels_track_main.txt")
    df = pd.read_csv(labels_file_path, sep=' ', header=None, names=columns)

    # Map activity labels to strings based on provided dictionary
    df['Activity_label'] = df['Activity_label'].map(activity_mapping)

    return df

def create_combined_dataframe_label(user_folder_path, activity_mapping):
    df_total = pd.DataFrame()
    # Iterate through each folder in User1 directory
    for folder_name in os.listdir(user_folder_path):
        folder_path = os.path.join(user_folder_path, folder_name)
        # Check if the item is a directory
        if os.path.isdir(folder_path):
            # Create DataFrame for the current folder
            df_temp = create_labels_dataframe(folder_path, activity_mapping)

            df_total = pd.concat([df_total, df_temp])

    return df_total