import pandas as pd
import numpy as np
import time
from geopy.distance import geodesic
import matplotlib.pyplot as plt

# Check execution run time
start_time = time.time()

# Import Fish positions CSV 
# fish_pos_df = pd.read_csv("fishPos_20190604.csv")
# release_df = pd.read_csv("PIT_CE.xlsx - Release.csv")
# collection_df = pd.read_csv("PIT_CE.xlsx - Collection.csv")
# converted_coordinates_df = pd.read_csv("converted_coordinates_fish_pos.csv", sep=',', dtype='unicode' )
# merged_pit_df = pd.read_csv('merged_PIT_CE.csv')

########### FISHPOS HELPER FUNCTIONS ###########
# Converts local coordinates into global coordinates
def local_to_global(fish_pos_df):
    origin_lat = 48.714167 # Latitude of the origin point
    origin_long = -121.131111 # Longitude of the origin point
    origin_point = (origin_lat, origin_long)
    for index,row in fish_pos_df.iterrows():
        fish_x =  row['X']
        fish_y = row['Y']
        
        # Calculate the distance in feet for one degree of latitude and longitude
        one_degree_latitude = geodesic(origin_point, (origin_lat + 1, origin_long)).feet
        one_degree_longitude = geodesic(origin_point, (origin_lat, origin_long + 1)).feet

    # Calculate the offsets in feet from the origin point to the fish location
        offset_x_feet = fish_x
        offset_y_feet = fish_y

    # Calculate the fish's global coordinates (latitude and longitude)
        fish_global_lat = origin_lat + (offset_y_feet / one_degree_latitude)
        fish_global_long = origin_long + (offset_x_feet / one_degree_longitude)

        fish_pos_df.loc[index, 'X'] = fish_global_lat
        fish_pos_df.loc[index, 'Y'] = fish_global_long

    # Create a new column for AT_code
    fish_pos_df['AT_code'] = np.nan


    # Add shortened AT_code data to new column AT_code
    for index, row in fish_pos_df.iterrows():
        long_AT = row['AT_code_long']
        short_AT = long_AT[3:7]
        fish_pos_df.loc[index, 'AT_code'] = short_AT
    
    fish_pos_df.to_csv('converted_coordinates_fish_pos.csv')
    return fish_pos_df

# Adds shortened AT_code data to new column AT_code
def retrieves_shortened_AT_codes(fish_pos_df):
        # Create a new column for AT_code
    fish_pos_df['AT_code'] = np.nan


    # Add shortened AT_code data to new column AT_code
    for index, row in fish_pos_df.iterrows():
        long_AT = row['AT_code_long']
        short_AT = long_AT[3:7]
        fish_pos_df.loc[index, 'AT_code'] = short_AT

    return fish_pos_df

# Retrieves the first instance in fish_pos of tag_code
def retrieves_first_pos(fish_pos_df):
    fish_pos_df = local_to_global(fish_pos_df)
    # Sort by timestamp
    fish_pos_df = fish_pos_df.sort_values(by = 'date_time', ascending=True)
    fish_pos_df = fish_pos_df.drop_duplicates(subset=['AT_code_long'], keep='first')
    fish_pos_df.to_csv("dummyfirstpos.csv")
    # return fish_pos_df
#######################################################



########### RELEASE AND COLLECTION HELPER FUNCTIONS ###########
# Removes any records without "Final Collection Point" in collection_df
def site_name_filter(collection_df):
    collection_df = collection_df.drop(collection_df[collection_df['site_name'] != 'Final Collection Point '].index)
    return collection_df

# Merge release and collection data for fish and remove any that do not have AT codes
def AT_code_filter(release_df, collection_df):
    collection_df = site_name_filter(collection_df)

    # Merge release_df and collection_df based on PIT code or 'tag_code'
    merged_df=release_df.merge(collection_df, on=['tag_code'], how='left', indicator='Match')

    # Sort for when Match = 'both' ; outputs true = collected, false = not collected
    merged_df['Match'] = merged_df['Match'] == 'both'

    # Rename Match Column to collection_status
    merged_df.rename(columns = {'Match': 'collection_status'}, inplace = True)

    # Remove rows that do not have an AT code
    merged_df = merged_df[merged_df.AT_code.notnull()]
    
    # Make at_code in merged_df uppercase
    for index,row in merged_df.iterrows():
        AT_code = row['AT_code']
        AT_code = AT_code.upper()
        merged_df.loc[index, 'AT_code'] = AT_code

    merged_df.to_csv('merged_PIT_CE.csv')
    return merged_df
##################################################################



# Merges release/collection data to fish position data
def merge_with_fish_position(release_collection_df,fish_pos_df):

    # Merge fish_pos and merged_df using INNER JOIN to return only matching AT_code rows between the two dataframes
    fish_pos_merged_df = fish_pos_df.merge(release_collection_df, on=['AT_code'], how='inner', indicator='Match')

    fish_pos_merged_df.to_csv('scubbed_data.csv')

# Remove any AT codes in fishPos data that does not have an AT code match in release data
def look_for_matching_AT_codes(df1, df2):
    merged_df = df1.merge(df2, on=['AT_code'], how='inner', indicator='Match')
    merged_df.to_csv('merged_fish_cr.csv')
#######################################################


########### VALIDATION FUNCTIONS ###########
# Validate data processing for fish_db by checking the number of matching unique AT codes between fishPos data and merged Release/Collection data
def filter_for_unique_AT_codes(fish_pos_df, merged_released_df):
    unique_at_pos = fish_pos_df['AT_code'].str.split(',\s*').explode().unique().tolist()
    unique_at_cr = merged_released_df['AT_code'].str.split(',\s*').explode().unique().tolist()
    results = {}
    for i in unique_at_pos:
        results[i] = unique_at_cr.count(i) 
    c = sum(1 for v in results.values() if v > 0)
    print(c)

## Creates a scatterplot to validate relationship between first position points.
def plot_first_positions():
        df = pd.read_csv('test_data/dummyfirstpos.csv')
        X = []
        Y = []
        for index,row in df.iterrows():
            X.append(row[3])
            Y.append(row[4])
        plt.scatter(X, Y, color='b')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
#######################################################


# Print processing time
print("Process finished --- %s seconds ---" % (time.time() - start_time))
