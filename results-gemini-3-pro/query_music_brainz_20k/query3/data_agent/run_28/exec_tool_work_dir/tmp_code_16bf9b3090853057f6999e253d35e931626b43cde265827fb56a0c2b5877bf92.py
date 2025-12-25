code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-6059198179457054813'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-1039588835092017339'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize(text):
    if text is None: return ""
    s = str(text).lower()
    if s in ['none', 'null', 'unknown', '[unknown]']:
        return ""
    # Remove contents of brackets/parens
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\[.*?\]', '', s)
    # Remove punct
    s = re.sub(r'[^\w\s]', '', s)
    return s.strip()

def process_row(row):
    title_raw = str(row['title']) if row['title'] else ""
    artist_raw = str(row['artist']) if row['artist'] else ""
    
    # Check if artist_raw is effectively empty
    artist_clean = normalize(artist_raw)
    
    # Check for "Artist - Title" pattern in title_raw if artist is missing
    # Example: "Daniel Balavoine - L'enfant aux yeux d'Italie"
    # Logic: if " - " exists, and artist is missing, split.
    # Also, sometimes title has " - " even if artist is present.
    
    title_parts = title_raw.split(' - ', 1)
    
    final_artist = artist_clean
    final_title = normalize(title_raw)
    
    if artist_clean == "":
        if len(title_parts) == 2:
            # Assume part 0 is artist, part 1 is title
            pot_artist = normalize(title_parts[0])
            pot_title = normalize(title_parts[1])
            if pot_artist and pot_title:
                final_artist = pot_artist
                final_title = pot_title
    else:
        # Artist is present. Check if title starts with artist name (redundant)
        # e.g. Artist="Queen", Title="Queen - Bohemian Rhapsody"
        # normalize(title_raw) would be "queen bohemian rhapsody"
        # We want "bohemian rhapsody"
        # Heuristic: if title starts with artist, strip it.
        # Be careful with partial matches.
        
        # Construct normalized potential full string "artist title"
        # Check if title_raw contains the separator
        if len(title_parts) == 2:
            p0 = normalize(title_parts[0])
            p1 = normalize(title_parts[1])
            if p0 == artist_clean:
                final_title = p1
            else:
                # Maybe the separator isn't distinguishing artist/title, just part of title
                pass
                
    return pd.Series([final_artist, final_title])

df[['clean_artist', 'clean_title']] = df.apply(process_row, axis=1)

# Filter out garbage
df_clean = df[(df['clean_title'] != "")].copy()

# Group
grouped = df_clean.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_10 = grouped.head(10).to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-6059198179457054813': 'file_storage/function-call-6059198179457054813.json', 'var_function-call-1039588835092017339': 'file_storage/function-call-1039588835092017339.json', 'var_function-call-2520799401825761242': {'title': 'None', 'artist': 'None', 'revenue_usd': 14647.52, 'clean_title': 'none', 'clean_artist': 'unknown'}}

exec(code, env_args)
