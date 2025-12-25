code = """import pandas as pd
import json
import re

# Load files
tracks_file = locals()['var_function-call-14091195230091116524']
sales_file = locals()['var_function-call-14091195230091115561']

with open(tracks_file, 'r') as f:
    tracks = pd.DataFrame(json.load(f))
with open(sales_file, 'r') as f:
    sales = pd.DataFrame(json.load(f))

tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)
sales['total_revenue'] = pd.to_numeric(sales['total_revenue'])

merged = pd.merge(tracks, sales, on='track_id', how='inner')

def clean_artist_title(row):
    title = str(row['title'])
    artist = str(row['artist'])
    if artist.lower() in ['none', '[unknown]', '', 'nan']:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            possible_artist = parts[0].strip()
            possible_title = parts[1].strip()
            if re.match(r'^\d+$', possible_artist):
                return artist, title 
            return possible_artist, possible_title
        return artist, title
    return artist, title

cleaned = merged.apply(clean_artist_title, axis=1)
merged['clean_artist'] = [x[0] for x in cleaned]
merged['clean_title'] = [x[1] for x in cleaned]

def normalize_title(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def normalize_artist(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    if text.startswith("the "):
        text = text[4:]
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

merged['norm_artist'] = merged['clean_artist'].apply(normalize_artist)
merged['norm_title'] = merged['clean_title'].apply(normalize_title)

# Filter out garbage
invalid_terms = ["none", "unknown", "untitled", ""]
mask = (
    (~merged['norm_title'].isin(invalid_terms)) & 
    (~merged['norm_artist'].isin(invalid_terms)) &
    (merged['norm_title'].str.len() > 1) &
    (merged['norm_artist'].str.len() > 1)
)
filtered = merged[mask]

grouped = filtered.groupby(['norm_artist', 'norm_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top = grouped.head(10)

results = []
for idx, row in top.iterrows():
    mask = (merged['norm_artist'] == row['norm_artist']) & (merged['norm_title'] == row['norm_title'])
    originals = merged[mask]
    
    t = originals['clean_title'].mode()
    t = t[0] if not t.empty else originals['clean_title'].iloc[0]
    
    a = originals['clean_artist'].mode()
    a = a[0] if not a.empty else originals['clean_artist'].iloc[0]
    
    results.append({
        "rank": len(results)+1,
        "title": t,
        "artist": a,
        "revenue": row['total_revenue']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-14091195230091116524': 'file_storage/function-call-14091195230091116524.json', 'var_function-call-14091195230091115561': 'file_storage/function-call-14091195230091115561.json', 'var_function-call-6181621511931833030': [{'rank': 1, 'title': '[untitled]', 'artist': '[unknown]', 'revenue': 253349.14}, {'rank': 2, 'title': 'None', 'artist': 'None', 'revenue': 14647.52}, {'rank': 3, 'title': '001-', 'artist': 'None', 'revenue': 5866.48}, {'rank': 4, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 5, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}], 'var_function-call-3899079882760515651': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}, {'rank': 3, 'title': 'Vagga', 'artist': 'Ske', 'revenue': 4981.38}, {'rank': 4, 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 4896.240000000001}, {'rank': 5, 'title': 'Best Friends', 'artist': 'Hans Zimmer', 'revenue': 4806.24}, {'rank': 6, 'title': 'Letters: A Short Essay', 'artist': 'echolyn', 'revenue': 4694.76}, {'rank': 7, 'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'revenue': 4693.259999999999}, {'rank': 8, 'title': 'Travel (live)', 'artist': 'Guts Pie Earshot', 'revenue': 4595.34}, {'rank': 9, 'title': '36-30', 'artist': 'Ian Vine', 'revenue': 4573.98}, {'rank': 10, 'title': 'Siviiliuhri', 'artist': 'Jukka Poika ja Kompostikopla', 'revenue': 4548.4400000000005}]}

exec(code, env_args)
