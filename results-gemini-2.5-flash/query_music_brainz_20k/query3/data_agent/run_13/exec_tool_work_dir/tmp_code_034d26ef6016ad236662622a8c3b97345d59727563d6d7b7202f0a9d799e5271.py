code = """import pandas as pd
import json
import datetime

# Load the tracks data from the JSON file
with open(locals()["var_function-call-4565568240269352944"], "r") as f:
    tracks_data = json.load(f)
tracks_df = pd.DataFrame(tracks_data)

# Load the sales data from the JSON file
with open(locals()["var_function-call-8679406998203301248"], "r") as f:
    sales_data = json.load(f)
sales_df = pd.DataFrame(sales_data)

# Clean and standardize the 'year' column
def clean_year(year):
    if pd.isna(year) or year == 'None' or str(year).strip() == '':
        return None
    year_str = str(year).strip().replace("'", "")
    if year_str.isdigit():
        year_int = int(year_str)
        if len(year_str) == 2:
            current_year_last_two_digits = datetime.datetime.now().year % 100
            if year_int <= current_year_last_two_digits:
                return int(f"20{year_int:02d}")
            else:
                return int(f"19{year_int:02d}")
        elif len(year_str) == 4:
            return year_int
    return None

tracks_df['cleaned_year'] = tracks_df['year'].apply(clean_year)

# Fill missing values for entity resolution
tracks_df['title'] = tracks_df['title'].fillna('')
tracks_df['artist'] = tracks_df['artist'].fillna('')
tracks_df['album'] = tracks_df['album'].fillna('')

# Create a combined identifier for entity resolution
tracks_df['song_identifier'] = tracks_df['title'] + ' - ' + tracks_df['artist'] + ' - ' + tracks_df['album'] + ' - ' + tracks_df['cleaned_year'].astype(str)

# Convert revenue_usd to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Merge tracks and sales data
merged_df = pd.merge(tracks_df, sales_df, on='track_id', how='inner')

# Calculate total revenue for each resolved song
total_revenue_per_song = merged_df.groupby('song_identifier')['revenue_usd'].sum().reset_index()

# Find the song with the highest total revenue
highest_revenue_song = total_revenue_per_song.loc[total_revenue_per_song['revenue_usd'].idxmax()]

# Extract the title from the highest revenue song_identifier
# The song_identifier is formed as 'title - artist - album - year'
# We need to parse this back to get the title.
# A more robust way would be to get the title from the original track record
# that corresponds to the `song_identifier` with the highest revenue.

# Find the `song_identifier` with the highest revenue
highest_rev_song_identifier = highest_revenue_song['song_identifier']

# Get a representative track for this `song_identifier`
# We take the first one, as all tracks with the same `song_identifier` should represent the same song.
representative_track_info = tracks_df[tracks_df['song_identifier'] == highest_rev_song_identifier].iloc[0]

result_title = representative_track_info['title']
result_revenue = highest_revenue_song['revenue_usd']

final_result = {
    "song_title": result_title,
    "total_revenue_usd": result_revenue
}

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-4565568240269352944': 'file_storage/function-call-4565568240269352944.json', 'var_function-call-8679406998203301248': 'file_storage/function-call-8679406998203301248.json'}

exec(code, env_args)
