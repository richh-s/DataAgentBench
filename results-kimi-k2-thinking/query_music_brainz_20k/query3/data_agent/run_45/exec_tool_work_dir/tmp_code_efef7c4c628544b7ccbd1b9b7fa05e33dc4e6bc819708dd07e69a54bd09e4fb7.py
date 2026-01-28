code = """import json
import pandas as pd
import re

# Read the sales data from the file
sales_file_path = var_functions.query_db:4
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

# Read the tracks data from the file
tracks_file_path = var_functions.query_db:5
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

print(f"Sales records: {len(sales_data)}")
print(f"Tracks records: {len(tracks_data)}")

# Convert to DataFrames
sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Show sample of data
print("\nSales data sample:")
print(sales_df.head())
print(f"Sales data types: {sales_df.dtypes.to_dict()}")

print("\nTracks data sample:")
print(tracks_df.head())
print(f"Tracks data types: {tracks_df.dtypes.to_dict()}")

# Calculate total revenue per track_id
total_revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
total_revenue_by_track = total_revenue_by_track.sort_values('revenue_usd', ascending=False)

print(f"\nTop 10 tracks by revenue (by track_id):")
print(total_revenue_by_track.head(10))

# Merge with tracks to see details
tracks_with_revenue = pd.merge(total_revenue_by_track, tracks_df, on='track_id', how='inner')
tracks_with_revenue = tracks_with_revenue.sort_values('revenue_usd', ascending=False)

print(f"\nTop 10 tracks with details:")
print(tracks_with_revenue.head(10))

# Define normalization functions
def normalize_string(s):
    if pd.isna(s) or s is None or s == "None":
        return ""
    return str(s).lower().strip()

def normalize_year(y):
    if pd.isna(y) or y is None or y == "None":
        return None
    # Extract 4-digit year if possible
    year_str = str(y)
    match = re.search(r'(\d{4})', year_str)
    if match:
        return match.group(1)
    # Handle 2-digit years
    match = re.search(r"(\d{2})", year_str)
    if match:
        year = int(match.group(1))
        return f"{1900 + year:04d}" if year > 20 else f"{2000 + year:04d}"
    return None

# Apply normalization
tracks_df['norm_title'] = tracks_df['title'].apply(normalize_string)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_string)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_string)
tracks_df['norm_year'] = tracks_df['year'].apply(normalize_year)

print("\nAfter normalization:")
print(tracks_df[['track_id', 'title', 'norm_title', 'artist', 'norm_artist', 'year', 'norm_year']].head(10))

# Group by normalized attributes to find duplicates
# Create a grouping key
tracks_df['group_key'] = tracks_df['norm_title'] + '|' + tracks_df['norm_artist'] + '|' + tracks_df['norm_album'] + '|' + tracks_df['norm_year'].astype(str)

# Count how many track_ids per group
group_counts = tracks_df.groupby('group_key').size().reset_index(name='count')
duplicate_groups = group_counts[group_counts['count'] > 1].sort_values('count', ascending=False)

print(f"\nNumber of duplicate groups: {len(duplicate_groups)}")
print("Top duplicate groups:")
print(duplicate_groups.head(10))

# Show some examples of duplicates
if len(duplicate_groups) > 0:
    print("\nExample duplicate group:")
    example_group_key = duplicate_groups.iloc[0]['group_key']
    example_tracks = tracks_df[tracks_df['group_key'] == example_group_key]
    print(example_tracks[['track_id', 'title', 'artist', 'album', 'year']])

# Calculate total revenue per group
tracks_with_revenue_norm = pd.merge(total_revenue_by_track, tracks_df[['track_id', 'group_key']], on='track_id', how='inner')
revenue_by_group = tracks_with_revenue_norm.groupby('group_key')['revenue_usd'].sum().reset_index()
revenue_by_group = revenue_by_group.sort_values('revenue_usd', ascending=False)

print(f"\nTop 10 groups by revenue:")
print(revenue_by_group.head(10))

# Get the top group and find its original track info
top_group_key = revenue_by_group.iloc[0]['group_key']
top_group_revenue = revenue_by_group.iloc[0]['revenue_usd']
top_group_tracks = tracks_df[tracks_df['group_key'] == top_group_key]

print(f"\nTop group key: {top_group_key}")
print(f"Total revenue: {top_group_revenue}")
print(f"Tracks in this group:")
print(top_group_tracks[['track_id', 'title', 'artist', 'album', 'year']])

# For final answer, pick the most complete record from the group
def get_best_track_info(tracks):
    # Prefer non-None values and longer strings
    best = {}
    for col in ['title', 'artist', 'album', 'year']:
        values = [v for v in tracks[col] if v is not None and str(v) != 'None' and str(v).strip()]
        if values:
            # Pick the longest, most descriptive value
            best[col] = max(values, key=lambda x: len(str(x)))
        else:
            best[col] = None
    return best

best_track_info = get_best_track_info(top_group_tracks)

# Print in required format
result = {
    'song_title': best_track_info['title'],
    'artist': best_track_info['artist'],
    'album': best_track_info['album'],
    'year': best_track_info['year'],
    'total_revenue_usd': float(top_group_revenue)
}

print("__RESULT__:")
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
