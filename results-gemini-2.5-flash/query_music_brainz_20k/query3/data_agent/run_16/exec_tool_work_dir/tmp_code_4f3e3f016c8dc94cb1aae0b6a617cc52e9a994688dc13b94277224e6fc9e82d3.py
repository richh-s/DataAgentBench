code = """import pandas as pd
import json

# Load data from storage
tracks_df = pd.DataFrame(json.load(open(locals()['var_function-call-14013552328078477005'], 'r')))
sales_df = pd.DataFrame(json.load(open(locals()['var_function-call-16760128783595443740'], 'r')))

# Convert track_id to integer for merging
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Merge dataframes
merged_df = pd.merge(tracks_df, sales_df, on='track_id', how='inner')

# Normalize title, artist, album for entity resolution
def normalize_string(text):
    if pd.isna(text):
        return ""
    return ''.join(filter(str.isalnum, str(text).lower()))

merged_df['normalized_title'] = merged_df['title'].apply(normalize_string)
merged_df['normalized_artist'] = merged_df['artist'].apply(normalize_string)
merged_df['normalized_album'] = merged_df['album'].apply(normalize_string)

# Normalize year for entity resolution
def normalize_year(year):
    if pd.isna(year) or str(year).strip() == "":
        return None
    year_str = str(year).strip()
    try:
        if len(year_str) == 2:
            if int(year_str) > 50: # Assume 19xx for years > 50
                return int("19" + year_str)
            else: # Assume 20xx for years <= 50
                return int("20" + year_str)
        elif len(year_str) == 4:
            return int(year_str)
    except ValueError:
        return None
    return None

merged_df['normalized_year'] = merged_df['year'].apply(normalize_year)

# Group by normalized attributes and sum revenue
song_revenue = merged_df.groupby(['normalized_title', 'normalized_artist', 'normalized_album', 'normalized_year']).agg(
    total_revenue=('revenue_usd', 'sum'),
    title=('title', 'first'),
    artist=('artist', 'first'),
    album=('album', 'first'),
    year=('year', 'first')
).reset_index()

# Find the song with the highest total revenue
highest_revenue_song = song_revenue.loc[song_revenue['total_revenue'].idxmax()]

# Format the result
result = {
    "title": highest_revenue_song['title'],
    "artist": highest_revenue_song['artist'],
    "album": highest_revenue_song['album'],
    "year": highest_revenue_song['year'],
    "total_revenue_usd": highest_revenue_song['total_revenue']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17336105588334470664': ['tracks'], 'var_function-call-14013552328078477005': 'file_storage/function-call-14013552328078477005.json', 'var_function-call-6878173595117947081': ['sales'], 'var_function-call-16760128783595443740': 'file_storage/function-call-16760128783595443740.json'}

exec(code, env_args)
