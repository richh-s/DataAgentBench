code = """import pandas as pd
import json

tracks_df = pd.read_json(locals()['var_function-call-2484900789149530228'])
sales_df = pd.read_json(locals()['var_function-call-4542668981267457718'])

# Ensure revenue_usd is numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Clean and normalize 'title', 'artist', and 'album' for entity resolution
def normalize_string(s):
    if pd.isna(s) or s is None:
        return ""
    s = str(s).lower()
    # Replace common punctuation and special characters with space
    # The outer string for the 'code' argument is '''...'''.
    # So, inside the Python code, a literal single quote ' must be written as \' to avoid terminating the outer string.
    # A literal double quote " can be written as " or \" 
    s = s.replace('-', ' ')
    s = s.replace('/', ' ')
    s = s.replace('\\', ' ') # Replace a literal backslash with space
    s = s.replace('(', ' ')
    s = s.replace(')', ' ')
    s = s.replace(':', ' ')
    s = s.replace('\'', '')  # This will be interpreted as s.replace("'", "") in Python
    s = s.replace('"', '')   # This will be interpreted as s.replace("\"", "") in Python
    s = ' '.join(s.split()).strip()
    return s


tracks_df['normalized_title'] = tracks_df['title'].apply(normalize_string)
tracks_df['normalized_artist'] = tracks_df['artist'].apply(normalize_string)
tracks_df['normalized_album'] = tracks_df['album'].apply(normalize_string)

# Create a combined identifier for songs to handle duplicates
def create_song_identifier(row):
    identifier_parts = []
    if row['normalized_title']:
        identifier_parts.append(row['normalized_title'])
    if row['normalized_artist']:
        identifier_parts.append(row['normalized_artist'])
    if row['normalized_album']:
        identifier_parts.append(row['normalized_album'])
    return ' - '.join(filter(None, identifier_parts))

tracks_df['song_identifier'] = tracks_df.apply(create_song_identifier, axis=1)


# Merge the dataframes
merged_df = pd.merge(sales_df, tracks_df, on='track_id', how='left')

# Calculate total revenue for each unique song identifier
total_revenue_per_song = merged_df.groupby('song_identifier')['revenue_usd'].sum().reset_index()

# Find the song with the highest total revenue
highest_revenue_song = total_revenue_per_song.loc[total_revenue_per_song['revenue_usd'].idxmax()]

# Get the original title and artist for the highest revenue song from the tracks_df
# We take the first encountered original title and artist for the highest revenue song_identifier.
original_song_info = merged_df[merged_df['song_identifier'] == highest_revenue_song['song_identifier']].iloc[0]

result = {
    "song_title": original_song_info['title'],
    "song_artist": original_song_info['artist'],
    "total_revenue_usd": highest_revenue_song['revenue_usd']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-2484900789149530228': 'file_storage/function-call-2484900789149530228.json', 'var_function-call-4542668981267457718': 'file_storage/function-call-4542668981267457718.json'}

exec(code, env_args)
