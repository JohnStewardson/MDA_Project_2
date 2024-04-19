from load_data import create_combined_dataframe_motion
from load_data import create_combined_dataframe
from load_data import create_labels_dataframe, activity_mapping, create_combined_dataframe_label
import pandas as pd
import os

user1_folder_path = "data_moodle/User1"
df_location_1 = create_combined_dataframe(user1_folder_path)
df_motion_1 = create_combined_dataframe_motion(user1_folder_path)
df_label_1 = create_combined_dataframe_label(user1_folder_path, activity_mapping)

df_motion_1_filled = df_motion_1.dropna(how='any')
print(df_motion_1_filled.head())
