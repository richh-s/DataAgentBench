code = """import json
import pandas as pd

# Load tracks
with open(locals()['var_function-call-2457622807540925275'], 'r') as f:
    tracks = json.load(f)
df_tracks = pd.DataFrame(tracks)

# Load sales
with open(locals()['var_function-call-6100282308464487853'], 'r') as f:
    sales = json.load(f)
df_sales = pd.DataFrame(sales)

# Convert types
df_sales['revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution Logic
def clean_artist(row):
    artist = str(row['artist'])
    title = str(row['title'])
    
    if artist in [None, 'None', '[unknown]', '', 'nan']:
        if ' - ' in title:
            parts = title.split(' - ')
            # Assumption: "Artist - Title"
            return parts[0].strip()
        return '[Unknown]'
    return artist

def clean_title(row):
    artist = str(row['artist'])
    title = str(row['title'])
    
    if artist in [None, 'None', '[unknown]', '', 'nan'] and ' - ' in title:
        parts = title.split(' - ')
        if len(parts) > 1:
            return ' - '.join(parts[1:]).strip()
    return title

df['cleaned_artist'] = df.apply(clean_artist, axis=1)
df['cleaned_title'] = df.apply(clean_title, axis=1)

# Normalize for grouping
df['norm_artist'] = df['cleaned_artist'].str.lower().str.strip()
df['norm_title'] = df['cleaned_title'].str.lower().str.strip()

# Group
grouped = df.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()
grouped = grouped.sort_values('revenue', ascending=False)

top_song = grouped.iloc[0]

# Find original casing
original = df[(df['norm_artist'] == top_song['norm_artist']) & (df['norm_title'] == top_song['norm_title'])].iloc[0]

result = {
    "artist": original['cleaned_artist'],
    "title": original['cleaned_title'],
    "revenue": top_song['revenue']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2457622807540925275': 'file_storage/function-call-2457622807540925275.json', 'var_function-call-6100282308464487853': 'file_storage/function-call-6100282308464487853.json'}

exec(code, env_args)
