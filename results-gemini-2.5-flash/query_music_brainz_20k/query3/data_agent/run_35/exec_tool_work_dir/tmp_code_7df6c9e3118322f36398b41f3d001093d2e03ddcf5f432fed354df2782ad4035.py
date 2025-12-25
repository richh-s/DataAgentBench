code = """import pandas as pd
tracks_df = pd.read_json(locals()['var_function-call-2484900789149530228'])
sales_df = pd.read_json(locals()['var_function-call-4542668981267457718'])

# Clean and normalize 'title' and 'artist' for entity resolution
def normalize_string(s):
    if pd.isna(s):
        return ""
    s = str(s).lower()
    s = s.replace("-", " ").replace("/", " ").replace("\", " ").replace("(", " ").replace(")", " ").replace(":", " ").replace("'", "").replace('"', '').strip()
    return ' '.join(s.split())

tracks_df['normalized_title'] = tracks_df['title'].apply(normalize_string)
tracks_df['normalized_artist'] = tracks_df['artist'].apply(normalize_string)
tracks_df['normalized_album'] = tracks_df['album'].apply(normalize_string)

# Create a combined identifier for songs to handle duplicates
tracks_df['song_identifier'] = tracks_df['normalized_title'] + " - " + tracks_df['normalized_artist'] + " - " + tracks_df['normalized_album']

# Merge the dataframes
merged_df = pd.merge(sales_df, tracks_df, on='track_id', how='left')

# Calculate total revenue for each unique song identifier
total_revenue_per_song = merged_df.groupby('song_identifier')['revenue_usd'].sum().reset_index()

# Find the song with the highest total revenue
highest_revenue_song = total_revenue_per_song.loc[total_revenue_per_song['revenue_usd'].idxmax()]

# Get the original title and artist for the highest revenue song from the tracks_df
# We can pick any track_id that maps to this song_identifier and get its original title and artist.
# However, to be more robust, we should try to get the most common (or first encountered) original title and artist.
# For simplicity, let's take the first encountered original title and artist for the highest revenue song_identifier.
# It is possible that the original title or artist contains more information so it is better to take directly from merged_df
original_song_info = merged_df[merged_df['song_identifier'] == highest_revenue_song['song_identifier']].iloc[0]

result = {
    "song_title": original_song_info['title'],
    "song_artist": original_song_info['artist'],
    "total_revenue_usd": highest_revenue_song['revenue_usd']
}

print('__RESULT__:')
print(pd.io.json.dumps(result))"""

env_args = {'var_function-call-2484900789149530228': 'file_storage/function-call-2484900789149530228.json', 'var_function-call-4542668981267457718': 'file_storage/function-call-4542668981267457718.json'}

exec(code, env_args)
