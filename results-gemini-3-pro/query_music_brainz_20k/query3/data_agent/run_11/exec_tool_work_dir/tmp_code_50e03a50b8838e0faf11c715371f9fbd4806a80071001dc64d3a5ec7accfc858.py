code = """import pandas as pd
import json
import re

# Get filenames from storage variables
sales_file = locals()['var_function-call-16976298203827158307']
tracks_file = locals()['var_function-call-10581686767626383820']

# Load data
with open(sales_file, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Basic cleaning function
def normalize_title(title):
    if not title or title == 'None': return ""
    s = str(title).lower()
    # Remove track numbers like "01 -", "001-", "1." at start if followed by non-digit
    # Regex: Start of string, optional digits, optional separators, keep the rest
    # Example: "01 - Title" -> "Title", "001-Title" -> "Title"
    s = re.sub(r'^\d+[\.\-\s]+', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def normalize_artist(artist):
    if not artist or str(artist) in ['None', '[unknown]', '']:
        return None
    return str(artist).lower().strip()

# Apply cleaning
df['clean_title'] = df['title'].apply(normalize_title)
df['clean_artist'] = df['artist'].apply(normalize_artist)

# Handle "Artist - Title" in title if artist is missing
def extract_artist_title(row):
    t = row['clean_title']
    a = row['clean_artist']
    
    # If artist is missing and title looks like "Artist - Title"
    if not a and ' - ' in t:
        parts = t.split(' - ', 1)
        # Check if the first part looks like an artist (not too long, not just numbers)
        return parts[0].strip(), parts[1].strip()
    
    return a, t

extracted = df.apply(extract_artist_title, axis=1)
df['final_artist'] = [x[0] for x in extracted]
df['final_title'] = [x[1] for x in extracted]

# Fill NA artist for grouping
df['group_artist'] = df['final_artist'].fillna('unknown')
df['group_title'] = df['final_title']

# Aggregation
grouped = df.groupby(['group_artist', 'group_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-16976298203827158307': 'file_storage/function-call-16976298203827158307.json', 'var_function-call-10581686767626383820': 'file_storage/function-call-10581686767626383820.json'}

exec(code, env_args)
