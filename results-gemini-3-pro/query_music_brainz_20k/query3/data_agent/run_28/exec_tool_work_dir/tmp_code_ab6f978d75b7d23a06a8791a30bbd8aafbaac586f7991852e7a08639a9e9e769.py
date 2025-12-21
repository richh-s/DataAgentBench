code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-6059198179457054813'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-1039588835092017339'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Cleaning / Normalization Function
def normalize_text(text):
    if text is None:
        return ""
    text = str(text).lower()
    # Remove text in parentheses/brackets which are often extra info (live, remix, album info)
    # This assumes the song title is the main part. 
    # Example: "Title (Live)" -> "Title"
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    # Remove punctuation and extra spaces
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def clean_artist(artist, title):
    # If artist is None or "unknown", try to extract from title if possible (heuristic)
    # For this dataset, let's look at the "normalized" artist.
    norm_artist = normalize_text(artist)
    if norm_artist in ['', 'none', 'unknown', 'various artists']:
        # Heuristic: Check if title has " - " which might separate artist - title
        # In the raw title
        if title and ' - ' in str(title):
            parts = str(title).split(' - ', 1)
            # This is ambiguous, could be "Artist - Title" or "Title - Artist"
            # But looking at sample track_id 1: "Daniel Balavoine - L'enfant..."
            # It seems to be "Artist - Title".
            return normalize_text(parts[0])
        return "unknown"
    return norm_artist

def clean_title(title, artist):
    # If title has " - " and artist was extracted or known, we might want to strip the artist part from title
    # But simplifying: just normalize the title removing parentheses.
    # If title contains "Artist - Title", we should probably remove the artist part to get the song name.
    
    # Let's normalize first
    t = str(title)
    
    # Heuristic for "Artist - Title" pattern in title when artist is present or extracted
    # If the title starts with the artist name, strip it.
    
    # First, simple normalization
    norm_title = normalize_text(t)
    
    # Handle the "Artist - Title" case in the title field
    if ' - ' in t:
        parts = t.split(' - ', 1)
        # If we assume the first part is artist (common in dirty data)
        # We can try to match it.
        # But let's just use the normalized title as is, if we group by (CleanArtist, CleanTitle) it might split same song if one has "Artist - " and other doesn't.
        # Better approach: If there is a hyphen, take the SECOND part as title if the first part looks like an artist?
        # Or just keep it simple?
        
        # Let's try to detect if the first part is the artist.
        p0_norm = normalize_text(parts[0])
        
        # We need the cleaned artist for this row to compare.
        # This function call order matters.
        pass
        
    return norm_title

# Apply cleaning
# We will create 'clean_artist' and 'clean_title' columns.

# First pass: clean artist
df['clean_artist'] = df.apply(lambda x: clean_artist(x['artist'], x['title']), axis=1)

# Second pass: clean title. 
# We need to handle cases where title includes artist.
def extract_song_name(row):
    title = str(row['title'])
    clean_art = row['clean_artist']
    
    # If the title explicitly contains " - ", check if the first part matches the artist
    if ' - ' in title:
        parts = title.split(' - ', 1)
        # If the first part normalized is similar to clean_artist
        if normalize_text(parts[0]) == clean_art:
             return normalize_text(parts[1])
        # If clean_artist is 'unknown' and we see a hyphen, we might assume the first part is the artist and second is title
        # (Based on track_id 1 example)
        if clean_art == 'unknown':
             return normalize_text(parts[1])
             
    return normalize_text(title)

df['clean_title'] = df.apply(extract_song_name, axis=1)

# Group by clean_artist and clean_title
grouped = df.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Get top result
top_song = grouped.iloc[0]

# Retrieve original variations to display a nice name
# We get the most frequent original title and artist for this group
mask = (df['clean_artist'] == top_song['clean_artist']) & (df['clean_title'] == top_song['clean_title'])
top_rows = df[mask]
best_title = top_rows['title'].mode()[0] if not top_rows['title'].mode().empty else top_rows['title'].iloc[0]
best_artist = top_rows['artist'].mode()[0] if not top_rows['artist'].mode().empty else top_rows['artist'].iloc[0]

# If best_artist is None/Unknown, try to see if we extracted it
if str(best_artist).lower() in ['none', 'unknown', '']:
    # Find a non-null artist in the group if possible
    valid_artists = top_rows[~top_rows['artist'].astype(str).str.lower().isin(['none', 'unknown', ''])]['artist']
    if not valid_artists.empty:
        best_artist = valid_artists.iloc[0]
    elif top_song['clean_artist'] != 'unknown':
        best_artist = top_song['clean_artist'].title() # Fallback

# Result
result = {
    "title": best_title,
    "artist": best_artist,
    "revenue_usd": top_song['total_revenue'],
    "clean_title": top_song['clean_title'],
    "clean_artist": top_song['clean_artist']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6059198179457054813': 'file_storage/function-call-6059198179457054813.json', 'var_function-call-1039588835092017339': 'file_storage/function-call-1039588835092017339.json'}

exec(code, env_args)
