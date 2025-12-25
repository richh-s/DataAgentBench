code = """import json
import pandas as pd
import re

sales_file_path = locals()['var_function-call-17703763520691558553']
tracks_file_path = locals()['var_function-call-17703763520691559746']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
if df_sales.empty:
    print("__RESULT__:")
    print(json.dumps([]))
    exit()

df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

def normalize_text(s):
    if not isinstance(s, str):
        return ""
    # Lowercase and strip
    s = s.lower().strip()
    # Remove punctuation, but keep unicode letters/numbers
    # regex \w matches [a-zA-Z0-9_] and unicode alphanumerics in Python 3 (str)
    # We want to remove characters that are NOT word characters or spaces
    # But let's be less aggressive. Just remove basic punctuation.
    # Actually, removing all non-alphanumeric (including unicode) is safer for matching
    # provided we don't end up with empty strings for everything.
    # \w in python 3 re matches unicode characters!
    # So [^\w\s] removes punctuation/symbols but keeps letters/numbers/spaces.
    s = re.sub(r'[^\w\s]', '', s) 
    # Collapse multiple spaces
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def extract_artist_title(row):
    title = row.get('title')
    artist = row.get('artist')
    
    if title is None: title = ""
    if artist is None: artist = ""
    
    # Handle "None" strings which appear to be placeholders in this dataset
    if title == "None": title = ""
    if artist == "None": artist = ""
    
    # If artist is missing, try to split title
    if not artist or artist.lower() in ['[unknown]', 'unk', 'various artists']:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist_cand = parts[0]
            title_cand = parts[1]
            return artist_cand, title_cand
    
    return artist, title

cleaned_data = []
for _, row in df_tracks.iterrows():
    raw_artist, raw_title = extract_artist_title(row)
    norm_artist = normalize_text(raw_artist)
    norm_title = normalize_text(raw_title)
    
    # If both are empty after normalization, use original track_id to avoid mass merging
    # or just skip? Better to keep as distinct "unknowns"
    if not norm_artist and not norm_title:
        merge_key = f"UNKNOWN_{row['track_id']}"
    else:
        merge_key = f"{norm_artist}|{norm_title}"
    
    cleaned_data.append({
        'track_id': row['track_id'],
        'original_title': row['title'],
        'original_artist': row['artist'],
        'norm_artist': norm_artist,
        'norm_title': norm_title,
        'merge_key': merge_key
    })

df_clean = pd.DataFrame(cleaned_data)

df_merged = pd.merge(df_clean, df_sales, on='track_id', how='inner')

df_grouped = df_merged.groupby('merge_key').agg({
    'revenue_usd': 'sum',
    'original_title': 'first', 
    'original_artist': 'first',
    'norm_artist': 'first',
    'norm_title': 'first'
}).reset_index()

df_sorted = df_grouped.sort_values('revenue_usd', ascending=False)
top_songs = df_sorted.head(10).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_songs))"""

env_args = {'var_function-call-17703763520691558553': 'file_storage/function-call-17703763520691558553.json', 'var_function-call-17703763520691559746': 'file_storage/function-call-17703763520691559746.json', 'var_function-call-17375738143367374828': [{'merge_key': '|', 'revenue_usd': 206433.9, 'original_title': 'Στα καμένα', 'original_artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'merge_key': '|none', 'revenue_usd': 17150.55, 'original_title': 'None', 'original_artist': '幡谷尚史'}, {'merge_key': '|004', 'revenue_usd': 7271.32, 'original_title': '004-/', 'original_artist': 'None'}, {'merge_key': '|003', 'revenue_usd': 7090.13, 'original_title': '003-', 'original_artist': 'None'}, {'merge_key': '|001', 'revenue_usd': 6283.24, 'original_title': '00-1', 'original_artist': 'None'}, {'merge_key': '|005', 'revenue_usd': 6155.29, 'original_title': '005', 'original_artist': 'None'}, {'merge_key': 'richmatteson|groovey', 'revenue_usd': 5417.34, 'original_title': 'Rich Matteson - Groovey', 'original_artist': 'None'}, {'merge_key': '|009', 'revenue_usd': 5045.7, 'original_title': '009-  ', 'original_artist': ' '}, {'merge_key': '|002', 'revenue_usd': 5013.4400000000005, 'original_title': '002-', 'original_artist': 'None'}, {'merge_key': '|010', 'revenue_usd': 4734.360000000001, 'original_title': '010-', 'original_artist': 'None'}]}

exec(code, env_args)
