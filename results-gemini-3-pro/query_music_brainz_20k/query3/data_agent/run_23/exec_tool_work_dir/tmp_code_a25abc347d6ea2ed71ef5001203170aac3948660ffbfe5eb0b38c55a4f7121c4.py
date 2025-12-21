code = """import pandas as pd
import json
import re

# Load data
with open(var_function_call_18273672994042049859, 'r') as f:
    sales_data = json.load(f)
with open(var_function_call_5279454901003549866, 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Function to normalize text
def normalize_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove text in parentheses or brackets (often contains non-essential info like remix, year, etc)
    text = re.sub(r'\s*\(.*?\)\s*', ' ', text)
    text = re.sub(r'\s*\[.*?\]\s*', ' ', text)
    # Remove specific prefixes like "001-" or "01-"
    text = re.sub(r'^\d+[\-\.]\s*', '', text)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to infer artist and title
def clean_track(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    # Check if artist is missing or placeholder
    missing_artist = artist.lower() in ['none', 'null', '[unknown]', 'unknown', '']
    
    if missing_artist:
        # Try to extract from title "Artist - Song"
        if ' - ' in title:
            parts = title.split(' - ', 1)
            # Assumption: First part is artist, second is title. 
            # This is common in the provided examples (e.g. "Daniel Balavoine - L'enfant...")
            inferred_artist = parts[0]
            inferred_title = parts[1]
            return inferred_artist, inferred_title
        else:
            return "unknown", title
    else:
        return artist, title

# Apply cleaning
cleaned = df.apply(clean_track, axis=1)
df['clean_artist'] = cleaned.apply(lambda x: x[0])
df['clean_title'] = cleaned.apply(lambda x: x[1])

# Normalize for grouping
df['norm_artist'] = df['clean_artist'].apply(normalize_text)
df['norm_title'] = df['clean_title'].apply(normalize_text)

# Aggregation
grouped = df.groupby(['norm_artist', 'norm_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-18273672994042049859': 'file_storage/function-call-18273672994042049859.json', 'var_function-call-5279454901003549866': 'file_storage/function-call-5279454901003549866.json'}

exec(code, env_args)
