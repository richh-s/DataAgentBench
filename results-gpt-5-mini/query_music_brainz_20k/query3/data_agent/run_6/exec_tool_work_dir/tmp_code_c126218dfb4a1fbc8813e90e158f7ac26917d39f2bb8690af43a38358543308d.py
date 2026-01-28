code = """import json
import pandas as pd
import unicodedata
from difflib import SequenceMatcher

# Load data from provided storage file paths
tracks_path = var_call_pbno0vllvG9W6yX5kYZnPMj7
sales_path = var_call_WQCI5VPUk7hLG83cBtbIV0eB

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# For performance, convert to DataFrame but avoid heavy clustering; use simpler resolution
tracks_df = pd.DataFrame(tracks)[['track_id','title','artist']]
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
tracks_df['title'] = tracks_df['title'].fillna('').astype(str)
tracks_df['artist'] = tracks_df['artist'].fillna('').astype(str)

sales_df = pd.DataFrame(sales)[['track_id','revenue_usd']]
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)

# Simple normalization: lowercase, strip, remove parenthesis content
import re

def norm(s):
    s = str(s)
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    s = re.sub(r"[^0-9a-zA-Z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()

tracks_df['norm_title'] = tracks_df['title'].apply(norm)
tracks_df['norm_artist'] = tracks_df['artist'].apply(norm)

# Use joined key norm_title + norm_artist
tracks_df['key'] = tracks_df['norm_title'] + '||' + tracks_df['norm_artist']

# For empty artist, just use title
tracks_df['key'] = tracks_df['key'].apply(lambda x: x if x!='||' else '')

# Map track_id to key using first occurrence
track_to_key = tracks_df.drop_duplicates(subset=['key','track_id']).set_index('track_id')['key'].to_dict()

sales_df['key'] = sales_df['track_id'].map(track_to_key).fillna('')

agg = sales_df.groupby('key', dropna=False)['revenue_usd'].sum().reset_index()

# get representative title/artist for each key
key_info = tracks_df.groupby('key').agg({'title':lambda x: x.iloc[0], 'artist':lambda x: x.iloc[0]}).reset_index()

agg = agg.merge(key_info, on='key', how='left')

# Find max
max_row = agg.loc[agg['revenue_usd'].idxmax()]
max_title = max_row['title'] if pd.notna(max_row['title']) and max_row['title']!='' else 'Unknown Title'
max_artist = max_row['artist'] if pd.notna(max_row['artist']) and max_row['artist']!='' else 'Unknown Artist'
max_revenue = float(max_row['revenue_usd'])
max_revenue_rounded = round(max_revenue,2)

final_text = f"{max_title} by {max_artist} generated ${max_revenue_rounded} total revenue across all stores and countries."

out = {'title': max_title, 'artist': max_artist, 'total_revenue_usd': max_revenue_rounded, 'message': final_text}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5748BnJF4cSKibjMEy6OEUqa': ['tracks'], 'var_call_HpVP6a6szkJm8nSPsFcQLNPg': ['sales'], 'var_call_pbno0vllvG9W6yX5kYZnPMj7': 'file_storage/call_pbno0vllvG9W6yX5kYZnPMj7.json', 'var_call_WQCI5VPUk7hLG83cBtbIV0eB': 'file_storage/call_WQCI5VPUk7hLG83cBtbIV0eB.json'}

exec(code, env_args)
