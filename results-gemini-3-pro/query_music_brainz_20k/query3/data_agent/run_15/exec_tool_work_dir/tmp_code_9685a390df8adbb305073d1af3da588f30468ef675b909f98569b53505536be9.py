code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-1271116417397029887'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6101111967261760493'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Cleaning functions
def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove text in parentheses/brackets
    text = re.sub(r"\(.*?\)|\[.*?\]", "", text)
    # Remove punctuation/symbols (keep alphanumeric and spaces)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip().lower()

def clean_artist(text):
    if not isinstance(text, str):
        return "unknown"
    text = text.strip().lower()
    if text in ["none", "unknown", "[unknown]", ""]:
        return "unknown"
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    return text

def extract_artist_from_title(row):
    title = row['title']
    artist = row['artist']
    if not isinstance(artist, str) or artist.strip().lower() in ["none", "unknown", "[unknown]", ""]:
        if isinstance(title, str) and " - " in title:
            parts = title.split(" - ", 1)
            return parts[0].strip()
    return artist

# Apply extraction
df['temp_artist'] = df.apply(extract_artist_from_title, axis=1)

# Apply cleaning
df['clean_title'] = df['title'].apply(clean_text)
df['clean_artist'] = df['temp_artist'].apply(clean_artist)

# Filter out invalid titles
valid_df = df[
    (df['clean_title'] != "") & 
    (df['clean_title'] != "none") & 
    (df['clean_title'] != "unknown")
]

# Group and Sum
grouped = valid_df.groupby(['clean_title', 'clean_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values(by='revenue_usd', ascending=False)

# Get top result
top_song = grouped.iloc[0]

# Retrieve original info
matches = valid_df[
    (valid_df['clean_title'] == top_song['clean_title']) & 
    (valid_df['clean_artist'] == top_song['clean_artist'])
]

# Use the most frequent original title and artist (excluding 'None'/'Unknown' if possible)
def get_best_str(series):
    # Filter out None/Unknown
    valid_vals = series[~series.str.lower().isin(['none', 'unknown', '[unknown]', ''])]
    if not valid_vals.empty:
        return valid_vals.mode()[0]
    return series.mode()[0] if not series.empty else "Unknown"

best_title = get_best_str(matches['title'])
best_artist = get_best_str(matches['artist'])

# If artist is still unknown/None, try the temp_artist
if best_artist.lower() in ['none', 'unknown', '']:
     best_artist = get_best_str(matches['temp_artist'])

result = {
    "title": best_title,
    "artist": best_artist,
    "clean_title": top_song['clean_title'],
    "clean_artist": top_song['clean_artist'],
    "total_revenue": top_song['revenue_usd']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1271116417397029887': 'file_storage/function-call-1271116417397029887.json', 'var_function-call-6101111967261760493': 'file_storage/function-call-6101111967261760493.json', 'var_function-call-5041480887059053554': {'title': 'None', 'artist': 'None', 'clean_title': 'none', 'clean_artist': 'unknown', 'total_revenue': 14647.52}}

exec(code, env_args)
