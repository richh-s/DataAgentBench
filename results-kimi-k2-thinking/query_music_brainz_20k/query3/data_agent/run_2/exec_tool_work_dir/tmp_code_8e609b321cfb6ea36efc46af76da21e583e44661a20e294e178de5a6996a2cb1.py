code = """import json
import pandas as pd

# Load tracks data
tracks_file = var_functions.query_db:5
tracks_data = []
with open(tracks_file, 'r') as f:
    for line in f:
        if line.strip():
            tracks_data.append(json.loads(line.strip()))

tracks_df = pd.DataFrame(tracks_data)
print(f'Tracks data shape: {tracks_df.shape}')
print(f'Columns: {tracks_df.columns.tolist()}')

# Load sales data
sales_file = var_functions.query_db:6
sales_data = []
with open(sales_file, 'r') as f:
    for line in f:
        if line.strip():
            sales_data.append(json.loads(line.strip()))

sales_df = pd.DataFrame(sales_data)
print(f'Sales data shape: {sales_df.shape}')
print(f'Columns: {sales_df.columns.tolist()}')

# Convert revenue to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
print(f'Total revenue sum: ${sales_df["revenue_usd"].sum():,.2f}')

# Show first few rows of each
tracks_preview = tracks_df.head()
sales_preview = sales_df.head()

print('Tracks preview:')
print(tracks_preview.to_string())
print('\nSales preview:')
print(sales_preview.to_string())

# Calculate total revenue per track_id
revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
top_tracks = revenue_by_track.sort_values('revenue_usd', ascending=False).head(10)
print('\nTop 10 tracks by revenue:')
print(top_tracks.to_string())

# Show corresponding track info for top revenue tracks
top_track_ids = top_tracks['track_id'].tolist()
top_tracks_info = tracks_df[tracks_df['track_id'].isin(top_track_ids)]
print('\nCorresponding track info:')
print(top_tracks_info.to_string())

# Save key variables for further analysis
result_dict = {
    'tracks_df': tracks_df,
    'sales_df': sales_df,
    'revenue_by_track': revenue_by_track,
    'top_tracks': top_tracks
}

# Let's look at potential duplicates by examining some common patterns
# First, let's see what we're dealing with - look at title cleaning
sample_titles = tracks_df['title'].head(20).tolist()
print('\nSample titles:')
for i, title in enumerate(sample_titles):
    print(f'{i+1}. {title}')

# Check for same track names with different track_ids
title_counts = tracks_df['title'].value_counts().head(20)
print('\nMost common titles:')
print(title_counts.to_string())

# Check if some track_ids have the same title and artist
print('\nAnalyzing potential duplicates...')
tracks_df['title_clean'] = tracks_df['title'].str.lower().str.strip() if tracks_df['title'].notna().all() else tracks_df['title']
tracks_df['artist_clean'] = tracks_df['artist'].str.lower().str.strip() if tracks_df['artist'].notna().all() else tracks_df['artist']

# Look at duplicates by title and artist
duplicates = tracks_df.groupby(['title_clean', 'artist_clean']).size().reset_index(name='count')
duplicates = duplicates[duplicates['count'] > 1].sort_values('count', ascending=False)
print(f'Number of duplicate groups: {len(duplicates)}')
print('Top duplicate groups:')
print(duplicates.head(10).to_string())

# Now let's see what the total revenue would be for these duplicate groups
# We need to merge revenue with track info first
merged = pd.merge(tracks_df, revenue_by_track, on='track_id', how='left')
merged['revenue_usd'] = merged['revenue_usd'].fillna(0)

# Group by cleaned title and artist to aggregate revenue
revenue_by_entity = merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().reset_index()
top_entities = revenue_by_entity.sort_values('revenue_usd', ascending=False).head(10)
print('\nTop 10 entities by revenue (grouped by title+artist):')
print(top_entities.to_string())

print('__RESULT__:')
print('Data loaded and preliminary analysis completed. Ready for detailed entity resolution.')"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
