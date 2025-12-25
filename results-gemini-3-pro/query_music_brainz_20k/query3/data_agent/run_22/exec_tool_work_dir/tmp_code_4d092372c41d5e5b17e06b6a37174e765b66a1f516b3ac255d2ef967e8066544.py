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

# Filter out "None" titles
df = df[df['norm_title'] != 'none']
df = df[df['norm_title'] != '']
df = df[df['norm_artist'] != '[unknown]']

# Group
grouped = df.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()
grouped = grouped.sort_values('revenue', ascending=False)

# Get top 5
top_5 = grouped.head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-2457622807540925275': 'file_storage/function-call-2457622807540925275.json', 'var_function-call-6100282308464487853': 'file_storage/function-call-6100282308464487853.json', 'var_function-call-7903873907971748242': {'artist': '[Unknown]', 'title': 'None', 'revenue': 14647.52}}

exec(code, env_args)
