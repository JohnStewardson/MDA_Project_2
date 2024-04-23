from load_data import create_combined_dataframe_motion
from load_data import create_combined_dataframe
from load_data import create_labels_dataframe, activity_mapping, create_combined_dataframe_label
import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np

user1_folder_path = "data_moodle/User1"
df_location_1 = create_combined_dataframe(user1_folder_path)
df_motion_1 = create_combined_dataframe_motion(user1_folder_path)
df_label_1 = create_combined_dataframe_label(user1_folder_path, activity_mapping)

df_motion_1_filled = df_motion_1.dropna(how='any')
# Set the display option to print the first 20 digits
pd.set_option('display.float_format', lambda x: '%.20f' % x)
#print(df_location_1["Time"]): 1498121199383, 1498121200374, 1498121201386...
#print(df_motion_1["Time"]): 1498120298000.0, 1498120298010.0 ....

"""
y = np.ones(len(df_location_1["Time"]))
y2 = np.ones(len(df_motion_1["Time"]))
print(y)
plt.scatter(df_location_1["Time"].values, y, label='Location', color='blue')
plt.scatter(df_motion_1["Time"].values, 0.9 * y2, label='Motion', color='red')
plt.xlabel("Time")
plt.legend()
plt.show()
"""
#Converting motion time to int to match datatype of location
df_motion_1["Time"] = df_motion_1["Time"].astype('int64')