code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-1289187297188193352']) as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-912133559032777454']) as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

def normalize(s):
    if not isinstance(s, str):
        return ""
    return "".join(c for c in s.lower() if c.isalnum())

def get_key(row):
    title = row.get('title', '')
    artist = row.get('artist', '')
    if pd.isna(title): title = ""
    if pd.isna(artist): artist = ""
    title = str(title)
    artist = str(artist)
    
    t_lower = title.lower()
    a_lower = artist.lower()
    
    invalid_artists = ['none', '[unknown]', 'unknown', '', 'null', 'nan']
    
    eff_artist = a_lower
    eff_title = t_lower
    
    if a_lower in invalid_artists:
        if ' - ' in title: 
            parts = title.split(' - ', 1)
            eff_artist = parts[0].lower()
            eff_title = parts[1].lower()
        else:
            eff_artist = ""
            eff_title = t_lower
            
    # If title is "None" and we have no artist, it's effectively empty/trash
    if eff_title == "none" and eff_artist == "":
        return "invalid_none"
        
    return normalize(eff_artist) + normalize(eff_title)

df_tracks['resolution_key'] = df_tracks.apply(get_key, axis=1)

# Merge
df_merged = df_sales.merge(df_tracks[['track_id', 'resolution_key', 'title', 'artist']], on='track_id', how='left')

# Group
grouped = df_merged.groupby('resolution_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Get top 30
top_30 = grouped.head(30).to_dict(orient='records')

final_results = []
for item in top_30:
    key = item['resolution_key']
    rev = item['total_revenue']
    matches = df_merged[df_merged['resolution_key'] == key]
    # Try to find a rep with valid artist/title
    rep = matches.iloc[0]
    for _, row in matches.iterrows():
        if row['artist'] not in ['None', '[unknown]', ''] and row['title'] != 'None':
            rep = row
            break
            
    final_results.append({
        "key": key,
        "revenue": rev,
        "title": rep['title'],
        "artist": rep['artist']
    })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-1289187297188193352': 'file_storage/function-call-1289187297188193352.json', 'var_function-call-912133559032777454': 'file_storage/function-call-912133559032777454.json', 'var_function-call-350696585057672437': [{'key': 'none', 'revenue': 14647.52, 'title': 'None', 'artist': 'None'}, {'key': '004', 'revenue': 7271.32, 'title': '004- ', 'artist': ' '}, {'key': '003', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': '001', 'revenue': 6283.24, 'title': '00-1', 'artist': '[unknown]'}, {'key': '005', 'revenue': 6155.29, 'title': '005-', 'artist': 'None'}]}

exec(code, env_args)
