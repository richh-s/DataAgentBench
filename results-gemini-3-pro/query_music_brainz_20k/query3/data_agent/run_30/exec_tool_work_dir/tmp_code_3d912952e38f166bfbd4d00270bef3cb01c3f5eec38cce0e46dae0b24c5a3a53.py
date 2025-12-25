code = """import pandas as pd
import json
import re

# Load data
with open(var_function_call_9771478070084226116, 'r') as f:
    sales_data = json.load(f)
with open(var_function_call_14488292253542672495, 'r') as f:
    tracks_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Convert types
sales_df['total_revenue'] = pd.to_numeric(sales_df['total_revenue'])
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

# Merge
df = pd.merge(sales_df, tracks_df, on='track_id', how='left')

# Cleaning functions
def clean_string(s):
    if not s:
        return ""
    s = str(s).lower().strip()
    if s in ["none", "unknown", "[unknown]", ""]:
        return ""
    return s

def resolve_entity(row):
    title = clean_string(row['title'])
    artist = clean_string(row['artist'])
    
    # Remove track number prefixes from title like "001-", "01-", "1. "
    # Regex: Start of string, one or more digits, followed by hyphen or dot or space
    title = re.sub(r'^\d+[-.\s]+', '', title)
    
    # Handle missing artist
    if not artist:
        # Check if title has " - " format which often implies "Artist - Title"
        if " - " in title:
            parts = title.split(" - ", 1)
            # Assume first part is artist, second is title if artist is missing
            artist = parts[0].strip()
            title = parts[1].strip()
    
    # Further cleaning: remove content in parenthesis usually? 
    # E.g., "title (live)", "title (remix)". 
    # But sometimes the title IS in parenthesis or important info is there.
    # Let's try to strip trailing parenthesis content if it looks like metadata
    # But keep it simple first. "remix", "live", "feat" might be good to ignore for grouping but risky.
    # Let's stick to cleaning whitespace and casing for now.
    
    return pd.Series([artist, title])

df[['clean_artist', 'clean_title']] = df.apply(resolve_entity, axis=1)

# Group by clean artist and title
# If artist is still empty, we group by title only (could be risky but necessary)
grouped = df.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()

# Sort descending
top_songs = grouped.sort_values(by='total_revenue', ascending=False)

# Get the top one
top_song = top_songs.iloc[0]

print("__RESULT__:")
print(json.dumps({
    "top_artist": top_song['clean_artist'], 
    "top_title": top_song['clean_title'], 
    "revenue": top_song['total_revenue']
}))"""

env_args = {'var_function-call-9771478070084226116': 'file_storage/function-call-9771478070084226116.json', 'var_function-call-14488292253542672495': 'file_storage/function-call-14488292253542672495.json'}

exec(code, env_args)
