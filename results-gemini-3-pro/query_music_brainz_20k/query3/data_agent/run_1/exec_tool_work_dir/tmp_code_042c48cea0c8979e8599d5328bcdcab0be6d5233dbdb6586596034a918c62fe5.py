code = """import json
import pandas as pd
import re

# Load data
with open('var_function-call-647087583900672662.json', 'r') as f:
    sales_data = json.load(f)
with open('var_function-call-7759510096737382327.json', 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert total_revenue to float
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Cleaning function
def clean_track_info(row):
    title = str(row['title']) if row['title'] is not None else ""
    artist = str(row['artist']) if row['artist'] is not None else ""
    
    # Handle artist "None" or "Unknown"
    if artist.lower() in ['none', 'unknown', '[unknown]', ''] and ' - ' in title:
        parts = title.split(' - ', 1)
        potential_artist = parts[0]
        potential_title = parts[1]
        # Basic heuristic: if the first part is reasonable length and title has content
        if len(potential_artist) > 0 and len(potential_title) > 0:
            artist = potential_artist
            title = potential_title

    # Remove leading numbering like "001-", "01- ", "1. "
    # Regex for start of string, digits, followed by hyphen or dot or space
    title = re.sub(r'^\d+[\.\-\s]+', '', title)
    
    # Clean up whitespace and lower case
    title = title.strip().lower()
    artist = artist.strip().lower()
    
    return pd.Series([title, artist])

df[['clean_title', 'clean_artist']] = df.apply(clean_track_info, axis=1)

# Group by clean title and artist
grouped = df.groupby(['clean_title', 'clean_artist'])['total_revenue'].sum().reset_index()

# Sort
top_songs = grouped.sort_values(by='total_revenue', ascending=False).head(10)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-647087583900672662': 'file_storage/function-call-647087583900672662.json', 'var_function-call-7759510096737382327': 'file_storage/function-call-7759510096737382327.json'}

exec(code, env_args)
