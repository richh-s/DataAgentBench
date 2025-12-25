code = """import json
import pandas as pd
import re

# Load data
with open('var_function-call-12705008639209252188.json', 'r') as f:
    sales_data = json.load(f)
with open('var_function-call-12705008639209254219.json', 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0.0)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower().strip()
    # Remove leading numbering like "01-", "001-", "01 "
    # Regex: Start of string, 2+ digits, followed by dash or space or dot
    text = re.sub(r'^\d{2,}[-.\s]+', '', text)
    # Remove text in parens/brackets (often extra info like live, remix)
    # Be careful not to remove essential title parts, but usually safe for aggregation
    text = re.sub(r'\s*[\(\[].*?[\)\]]', '', text)
    # Remove special chars
    # text = re.sub(r'[^\w\s]', '', text) # Maybe too aggressive?
    return text.strip()

def resolve_entity(row):
    title = row.get('title', '')
    artist = row.get('artist', '')
    
    if not isinstance(title, str): title = ""
    if not isinstance(artist, str): artist = ""
    
    # Check if artist is missing or placeholder
    if artist.lower() in ['none', '[unknown]', 'unknown', '']:
        # Try to extract from title if it looks like "Artist - Title"
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist = parts[0]
            title = parts[1]
    
    clean_t = clean_text(title)
    clean_a = clean_text(artist)
    
    # Fallback if cleaning removed everything
    if not clean_t: clean_t = title.lower().strip()
    if not clean_a: clean_a = artist.lower().strip()
    
    return pd.Series([clean_a, clean_t])

df[['clean_artist', 'clean_title']] = df.apply(resolve_entity, axis=1)

# Group by clean artist and title
grouped = df.groupby(['clean_artist', 'clean_title'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values('revenue_usd', ascending=False)

result = grouped.head(10).to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12705008639209252188': 'file_storage/function-call-12705008639209252188.json', 'var_function-call-12705008639209254219': 'file_storage/function-call-12705008639209254219.json'}

exec(code, env_args)
