code = """import json
import pandas as pd

# Load sales data
with open(locals()['var_function-call-7603886357055213310'], 'r') as f:
    sales_data = json.load(f)

# Load tracks data
with open(locals()['var_function-call-3062453601885258613'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge to attach metadata to sales
# We keep all tracks in sales, even if metadata might be missing (inner join vs left join)
# Assuming tracks_db covers all sold tracks.
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution Logic
# 1. Fill NaNs
df_merged['title'] = df_merged['title'].fillna('').astype(str)
df_merged['artist'] = df_merged['artist'].fillna('').astype(str)

# 2. Normalize
def normalize(s):
    return s.lower().strip()

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Handle cases where artist is "none" or "[unknown]"
# If artist is missing, rely on title.
# We group by (norm_title, norm_artist) for now.
# However, if artist is 'none', 'unknown', or empty, we might want to group just by title? 
# But duplicate titles exist (e.g. "Intro", "Greatest Hits").
# Let's inspect the top revenue generators first without complex merging.

# Group by normalized title and artist
revenue_by_song = df_merged.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
revenue_by_song = revenue_by_song.sort_values('total_revenue', ascending=False)

# Get the top 5
top_songs = revenue_by_song.head(5)

# We need to recover the original Title and Artist (take the first one or most frequent)
result_list = []
for index, row in top_songs.iterrows():
    # Find one original record to get nice casing
    original_rec = df_merged[
        (df_merged['norm_title'] == row['norm_title']) & 
        (df_merged['norm_artist'] == row['norm_artist'])
    ].iloc[0]
    
    result_list.append({
        'title': original_rec['title'],
        'artist': original_rec['artist'],
        'total_revenue': row['total_revenue']
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-7603886357055213310': 'file_storage/function-call-7603886357055213310.json', 'var_function-call-3062453601885258613': 'file_storage/function-call-3062453601885258613.json'}

exec(code, env_args)
