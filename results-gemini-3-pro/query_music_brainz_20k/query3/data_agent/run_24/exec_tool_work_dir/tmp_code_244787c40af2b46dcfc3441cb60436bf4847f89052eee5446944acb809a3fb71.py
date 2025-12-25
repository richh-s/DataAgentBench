code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-5570592498162877174'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-5570592498162876679'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0.0)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def resolve_song(row):
    artist_raw = str(row['artist']) if row['artist'] is not None else "none"
    title_raw = str(row['title']) if row['title'] is not None else ""
    artist_norm = artist_raw.lower().strip()
    title_norm = title_raw.lower().strip()
    
    if artist_norm in ["none", "[unknown]", "unknown", "null", ""]:
        if " - " in title_norm:
            parts = title_norm.split(" - ", 1)
            artist_norm = parts[0].strip()
            title_norm = parts[1].strip()
        else:
            artist_norm = "unknown_artist"
            
    title_cleaned = re.sub(r'\(.*?\)', '', title_norm)
    title_cleaned = re.sub(r'\[.*?\]', '', title_cleaned)
    title_cleaned = re.split(r'\bfeat\.|\bft\.', title_cleaned)[0]
    
    if " - " in title_cleaned:
        title_cleaned = title_cleaned.split(" - ")[0]
        
    return artist_norm.strip(), title_cleaned.strip()

resolved = merged.apply(resolve_song, axis=1)
merged['clean_artist'] = resolved.apply(lambda x: x[0])
merged['clean_title'] = resolved.apply(lambda x: x[1])

# Analysis
grouped = merged.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
top_songs = grouped.sort_values(by='total_revenue', ascending=False).head(10)

# Debug
debug_info = {}
for i, row in top_songs.iterrows():
    key = f"{row['clean_artist']} - {row['clean_title']}"
    # Get sample original titles/artists for this group
    samples = merged[
        (merged['clean_artist'] == row['clean_artist']) & 
        (merged['clean_title'] == row['clean_title'])
    ][['title', 'artist']].head(3).to_dict(orient='records')
    debug_info[key] = samples

print("__RESULT__:")
print(json.dumps({"top_songs": top_songs.to_dict(orient='records'), "debug": debug_info}))"""

env_args = {'var_function-call-5570592498162877174': 'file_storage/function-call-5570592498162877174.json', 'var_function-call-5570592498162876679': 'file_storage/function-call-5570592498162876679.json', 'var_function-call-7904594862415471008': [{'clean_artist': 'unknown_artist', 'clean_title': 'none', 'total_revenue': 14647.52}, {'clean_artist': 'unknown_artist', 'clean_title': '003-', 'total_revenue': 8333.2}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'total_revenue': 7634.02}, {'clean_artist': 'neil biggin', 'clean_title': 'chile', 'total_revenue': 6192.51}, {'clean_artist': 'moonbootica', 'clean_title': 'watt bird', 'total_revenue': 5921.33}, {'clean_artist': 'vrisak generacije', 'clean_title': 'ne veruj', 'total_revenue': 5867.83}, {'clean_artist': 'fischerspooner', 'clean_title': 'emerge', 'total_revenue': 5746.85}, {'clean_artist': 'guts pie earshot', 'clean_title': 'travel', 'total_revenue': 5674.44}, {'clean_artist': 'atb', 'clean_title': 'let u go', 'total_revenue': 5624.17}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'total_revenue': 5584.02}]}

exec(code, env_args)
