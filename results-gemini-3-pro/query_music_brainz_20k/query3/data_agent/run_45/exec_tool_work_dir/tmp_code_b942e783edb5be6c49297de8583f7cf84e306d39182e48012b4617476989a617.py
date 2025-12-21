code = """import json
import pandas as pd
import re

# Get file paths from local variables
sales_file_path = locals()['var_function-call-9165943318207358128']
tracks_file_path = locals()['var_function-call-1686680427873547385']

# Load data
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Merge
df = pd.merge(df_tracks, df_sales, on='track_id', how='inner')

# Data cleaning function
def clean_string(s):
    if not isinstance(s, str):
        return ""
    # Lowercase
    s = s.lower().strip()
    return s

def extract_artist_title(row):
    title = row['title']
    artist = row['artist']
    
    if not isinstance(title, str):
        title = ""
    if not isinstance(artist, str):
        artist = ""

    # Basic cleaning
    title_clean = title.strip()
    artist_clean = artist.strip()
    
    # Handle "None" or "[unknown]" artists
    if artist_clean.lower() in ['none', '[unknown]', '']:
        # Try to split title by " - " if artist is missing
        if " - " in title_clean:
            parts = title_clean.split(" - ", 1)
            # Assume "Artist - Title" format if artist is missing
            possible_artist = parts[0]
            possible_title = parts[1]
            return possible_artist, possible_title
        else:
            return "unknown", title_clean
    
    return artist_clean, title_clean

# Apply cleaning
normalized_data = []
for idx, row in df.iterrows():
    artist, title = extract_artist_title(row)
    
    # Further normalization for matching
    # Remove leading track numbers from title (e.g., "01 ", "01-", "01.", "001-")
    title_norm = re.sub(r'^\d+[\.\-\s]+', '', title)
    title_norm = clean_string(title_norm)
    
    # Remove things in parenthesis like "(live)", "(remix)" from title for grouping?
    # Maybe too aggressive. Let's stick to basic normalization first.
    
    artist_norm = clean_string(artist)
    
    normalized_data.append({
        'original_title': row['title'],
        'original_artist': row['artist'],
        'norm_artist': artist_norm,
        'norm_title': title_norm,
        'revenue': row['total_revenue']
    })

df_norm = pd.DataFrame(normalized_data)

# Group by normalized artist and title
grouped = df_norm.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()
grouped = grouped.sort_values('revenue', ascending=False)

# Get top 10
top_10 = grouped.head(10).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-9165943318207358128': 'file_storage/function-call-9165943318207358128.json', 'var_function-call-1686680427873547385': 'file_storage/function-call-1686680427873547385.json'}

exec(code, env_args)
