code = """import json
import pandas as pd
import re

# Load data using locals() with the key strings
sales_path = locals()['var_function-call-5175618226163414670']
tracks_path = locals()['var_function-call-7684694315687986133']

with open(sales_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution Functions
def normalize_text(text):
    if not isinstance(text, str):
        return ""
    if text.lower() in ['none', '[unknown]', 'unknown', '']:
        return ""
    # Remove leading numbers like "01-", "001-", "1. "
    text = re.sub(r'^\d+[\.\-]\s*', '', text)
    # Remove things in brackets/parentheses
    text = re.sub(r'\s*[\(\[].*?[\)\]]', '', text)
    return text.strip()

def extract_artist_title(row):
    raw_title = row.get('title', '')
    raw_artist = row.get('artist', '')
    
    # Check if artist is missing or placeholder
    is_artist_missing = (not raw_artist) or (str(raw_artist).lower() in ['none', '[unknown]', 'unknown', ''])
    
    if not is_artist_missing:
        artist = str(raw_artist)
        title = str(raw_title)
    else:
        # If artist is missing, check if title is "Artist - Title"
        # Heuristic: split by " - "
        raw_t_str = str(raw_title)
        if ' - ' in raw_t_str:
            parts = raw_t_str.split(' - ', 1)
            artist = parts[0]
            title = parts[1]
        else:
            artist = "Unknown"
            title = raw_t_str
    
    clean_a = normalize_text(artist)
    clean_t = normalize_text(title)
    
    return clean_a.lower(), clean_t.lower()

# Apply extraction
canonical = df.apply(extract_artist_title, axis=1)
df['clean_artist'] = [x[0] for x in canonical]
df['clean_title'] = [x[1] for x in canonical]

# Group by clean artist and title
grouped = df.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-17091667474296777698': ['sales'], 'var_function-call-17091667474296777251': ['tracks'], 'var_function-call-13701487654061221405': [{'count(DISTINCT track_id)': '19375'}], 'var_function-call-5175618226163416147': [{'count(*)': '19375'}], 'var_function-call-5175618226163414670': 'file_storage/function-call-5175618226163414670.json', 'var_function-call-7684694315687986133': 'file_storage/function-call-7684694315687986133.json'}

exec(code, env_args)
