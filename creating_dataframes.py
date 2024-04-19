from load_data import create_combined_dataframe_motion
from load_data import create_combined_dataframe
import pandas as pd
import os

user1_folder_path = "data_moodle/User1"
df_location_1 = create_combined_dataframe(user1_folder_path)
df_motion_1 = create_combined_dataframe_motion(user1_folder_path)

