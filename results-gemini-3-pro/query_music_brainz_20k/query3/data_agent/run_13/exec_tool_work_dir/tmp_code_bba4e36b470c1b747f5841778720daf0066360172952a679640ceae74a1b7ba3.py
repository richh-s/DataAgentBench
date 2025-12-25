code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-7603886357055213310'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-3062453601885258613'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

df_merged['title'] = df_merged['title'].fillna('None').astype(str)
df_merged['artist'] = df_merged['artist'].fillna('None').astype(str)

def normalize(s):
    return s.lower().strip()

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Inspect top raw tracks
print("Top Raw Tracks:")
top_raw = df_merged.sort_values('total_revenue', ascending=False).head(10)[['track_id', 'title', 'artist', 'total_revenue']]
print(top_raw.to_string())

# Grouping
# Filter out "none" titles
df_clean = df_merged[~df_merged['norm_title'].isin(['none', 'null', '', '[unknown]'])]

revenue_by_song = df_clean.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
revenue_by_song = revenue_by_song.sort_values('total_revenue', ascending=False)

print("Top Grouped Songs:")
top_grouped = revenue_by_song.head(5)
print(top_grouped.to_string())

result_list = []
for index, row in top_grouped.iterrows():
    # Get original display strings
    original_rec = df_clean[
        (df_clean['norm_title'] == row['norm_title']) & 
        (df_clean['norm_artist'] == row['norm_artist'])
    ].iloc[0]
    
    result_list.append({
        'title': original_rec['title'],
        'artist': original_rec['artist'],
        'total_revenue': row['total_revenue']
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-7603886357055213310': 'file_storage/function-call-7603886357055213310.json', 'var_function-call-3062453601885258613': 'file_storage/function-call-3062453601885258613.json', 'var_function-call-9915776680240783115': [{'title': 'None', 'artist': 'None', 'total_revenue': 14647.52}, {'title': '010-', 'artist': 'None', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 4128.59}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'total_revenue': 3767.95}]}

exec(code, env_args)
