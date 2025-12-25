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

# Apply cleaning
df['clean_title'] = df['title'].apply(clean_text)
df['clean_artist'] = df['artist'].apply(clean_artist)

# Handle cases where artist is in title (simple heuristic: split by " - " if artist is unknown)
# Although we stripped punctuation in clean_title, let's look at original title for this specific fix if needed.
# But looking at the preview: "Daniel Balavoine - L'enfant aux yeux d'Italie" -> artist "None"
# The clean_title function removes " - ", so we can't split on it after cleaning.
# Let's improve the logic: extract artist from title BEFORE cleaning if artist is unknown.

def extract_artist_from_title(row):
    title = row['title']
    artist = row['artist']
    
    if not isinstance(artist, str) or artist.lower() in ["none", "unknown", "[unknown]", ""]:
        if isinstance(title, str) and " - " in title:
            parts = title.split(" - ", 1)
            # Assume "Artist - Title" format
            return parts[0].strip()
    return artist

# Update artist based on title extraction
df['temp_artist'] = df.apply(extract_artist_from_title, axis=1)
# Now clean the new artist column
df['clean_artist'] = df['temp_artist'].apply(clean_artist)

# Group and Sum
grouped = df.groupby(['clean_title', 'clean_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values(by='revenue_usd', ascending=False)

# Get top result
top_song = grouped.iloc[0]

# Retrieve original info for the top song to display nicely
# We find all rows matching the clean title and artist, and pick the most common original title/artist
matches = df[
    (df['clean_title'] == top_song['clean_title']) & 
    (df['clean_artist'] == top_song['clean_artist'])
]
best_title = matches['title'].mode()[0] if not matches.empty else top_song['clean_title']
best_artist = matches['artist'].mode()[0] if not matches.empty else top_song['clean_artist']

result = {
    "title": best_title,
    "artist": best_artist,
    "clean_title": top_song['clean_title'],
    "clean_artist": top_song['clean_artist'],
    "total_revenue": top_song['revenue_usd']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1271116417397029887': 'file_storage/function-call-1271116417397029887.json', 'var_function-call-6101111967261760493': 'file_storage/function-call-6101111967261760493.json'}

exec(code, env_args)
