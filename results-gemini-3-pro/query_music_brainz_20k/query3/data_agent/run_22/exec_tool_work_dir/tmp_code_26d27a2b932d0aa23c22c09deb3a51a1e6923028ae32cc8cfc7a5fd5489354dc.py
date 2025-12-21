code = """import json
import pandas as pd
import re

# Load tracks
with open(locals()['var_function-call-2457622807540925275'], 'r') as f:
    tracks = json.load(f)
df_tracks = pd.DataFrame(tracks)

# Load sales
with open(locals()['var_function-call-6100282308464487853'], 'r') as f:
    sales = json.load(f)
df_sales = pd.DataFrame(sales)

# Convert types
df_sales['revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize(text):
    if not text: return ""
    # Lowercase
    text = str(text).lower()
    # Remove leading numbers and hyphens (e.g., "001-", "01 ")
    text = re.sub(r'^\d+[\-\.\s]+', '', text)
    # Remove content in parens/brackets
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    # Strip whitespace
    return text.strip()

def extract_artist_title(row):
    artist = str(row['artist'])
    title = str(row['title'])
    
    # Handle missing artist
    if artist in [None, 'None', '[unknown]', '', 'nan', 'null']:
        if ' - ' in title:
            parts = title.split(' - ')
            # Heuristic: assume first part is artist
            extracted_artist = parts[0]
            extracted_title = ' - '.join(parts[1:])
            return extracted_artist, extracted_title
        return '[unknown]', title
    
    return artist, title

# Apply extraction
extracted = df.apply(extract_artist_title, axis=1)
df['clean_artist'] = [x[0] for x in extracted]
df['clean_title'] = [x[1] for x in extracted]

# Normalize
df['norm_artist'] = df['clean_artist'].apply(normalize)
df['norm_title'] = df['clean_title'].apply(normalize)

# Filter out invalid entries
df = df[df['norm_title'] != 'none']
df = df[df['norm_title'] != '']
df = df[df['norm_artist'] != '[unknown]']
df = df[df['norm_artist'] != '']

# Group
grouped = df.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()
grouped = grouped.sort_values('revenue', ascending=False)

top_5 = grouped.head(5)

# Get original names for display (mode)
results = []
for idx, row in top_5.iterrows():
    # Find original rows
    mask = (df['norm_artist'] == row['norm_artist']) & (df['norm_title'] == row['norm_title'])
    original_rows = df[mask]
    
    # Pick the most common title/artist representation that is not "None"
    # Actually just take the first one that looks good or the most frequent
    best_artist = original_rows['clean_artist'].mode()[0]
    best_title = original_rows['clean_title'].mode()[0]
    
    results.append({
        "artist": best_artist,
        "title": best_title,
        "revenue": row['revenue']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2457622807540925275': 'file_storage/function-call-2457622807540925275.json', 'var_function-call-6100282308464487853': 'file_storage/function-call-6100282308464487853.json', 'var_function-call-7903873907971748242': {'artist': '[Unknown]', 'title': 'None', 'revenue': 14647.52}, 'var_function-call-1063100188911444143': [{'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5417.34}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say (album version)', 'revenue': 4110.55}, {'norm_artist': 'kerstin gier', 'norm_title': 'kapitel 01', 'revenue': 4091.12}, {'norm_artist': 'damian marley', 'norm_title': 'beautiful (instrumental)', 'revenue': 4004.42}, {'norm_artist': 'matthew barber', 'norm_title': 'the story of your life', 'revenue': 3962.97}], 'var_function-call-15419448355779907791': [{'track_id': '2133', 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 1501.6699999999998}, {'track_id': '8656', 'title': '001-Gator Whale', 'artist': 'Grooveyard', 'revenue': 294.01}, {'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 1036.29}, {'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson', 'revenue': 251.16}, {'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'revenue': 1288.75}, {'track_id': '10416', 'title': '002-All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 1070.38}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 949.82}, {'track_id': '12601', 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 1739.54}, {'track_id': '3144', 'title': 'Luke Bryan - All My Friends Say (album version)', 'artist': 'None', 'revenue': 869.34}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 2142.48}]}

exec(code, env_args)
