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
            return parts[0], parts[1]
        else:
            return "unknown", title_clean
    
    return artist_clean, title_clean

# Apply cleaning
normalized_data = []
for idx, row in df.iterrows():
    artist, title = extract_artist_title(row)
    
    # Remove leading track numbers
    title_norm = re.sub(r'^\d+[\.\-\s]+', '', title)
    
    # Remove parenthesis content for fuzzy grouping (e.g. "(Live)", "(Remix)")
    # This aggregates all versions of the song.
    title_core = re.sub(r'\s*\(.*?\)', '', title_norm)
    # Remove brackets too
    title_core = re.sub(r'\s*\[.*?\]', '', title_core)
    
    title_core = clean_string(title_core)
    artist_norm = clean_string(artist)
    
    # Filter out invalid or generic titles/artists
    if title_core in ['', 'none', 'unknown', 'track']:
        continue
    if artist_norm in ['', 'none', 'unknown']:
        continue
        
    normalized_data.append({
        'original_title': row['title'],
        'original_artist': row['artist'],
        'norm_artist': artist_norm,
        'norm_title': title_core,
        'revenue': row['total_revenue']
    })

df_norm = pd.DataFrame(normalized_data)

# Group by normalized artist and title
grouped = df_norm.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()
grouped = grouped.sort_values('revenue', ascending=False)

# Get top 5
top_5 = grouped.head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-9165943318207358128': 'file_storage/function-call-9165943318207358128.json', 'var_function-call-1686680427873547385': 'file_storage/function-call-1686680427873547385.json', 'var_function-call-13708768064711140461': [{'norm_artist': 'unknown', 'norm_title': '', 'revenue': 59287.18}, {'norm_artist': 'unknown', 'norm_title': 'none', 'revenue': 14647.52}, {'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5668.5}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say (album version)', 'revenue': 5180.93}, {'norm_artist': 'pras', 'norm_title': 'ghetto supastar (that is what you are)', 'revenue': 4933.98}, {'norm_artist': 'frankie goes to hollywood', 'norm_title': 'the power of love (rob searle club mix)', 'revenue': 4909.04}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue': 4881.42}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'revenue': 4770.54}, {'norm_artist': 'the turtles', 'norm_title': 'happy together', 'revenue': 4747.049999999999}, {'norm_artist': 'lemon d', 'norm_title': 'jah love (vip remix)', 'revenue': 4645.110000000001}]}

exec(code, env_args)
