code = """# Continue from previous context
import json
import pandas as pd
import re

# We assume data is already loaded in previous step variables, but let's reload to be safe/clean
with open(locals()['var_function-call-3992495390837066285'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-7409539752900977037'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_record(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    invalid_values = ['None', '[unknown]', 'Unknown', '', 'nan']
    
    is_artist_invalid = artist in invalid_values
    if is_artist_invalid and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            potential_artist = parts[0].strip()
            potential_title = parts[1].strip()
            if len(potential_artist) < 50 and not re.match(r'^\d+$', potential_artist):
                artist = potential_artist
                title = potential_title

    if title in invalid_values: title = ""
    if artist in invalid_values: artist = ""
    return pd.Series([title, artist])

merged[['clean_title', 'clean_artist']] = merged.apply(clean_record, axis=1)

def normalize_text(text):
    if not text: return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()
    return text

merged['norm_title'] = merged['clean_title'].apply(normalize_text)
merged['norm_artist'] = merged['clean_artist'].apply(normalize_text)

# Filter: Require non-empty artist and title
# Also filter out titles that are just numbers
valid_merged = merged[
    (merged['norm_title'] != "") & 
    (merged['norm_artist'] != "") & 
    (~merged['norm_title'].str.match(r'^\d+$'))
]

grouped = valid_merged.groupby(['norm_title', 'norm_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values('revenue_usd', ascending=False)

top_candidates = []
for i in range(10):
    if i >= len(grouped): break
    row = grouped.iloc[i]
    nt = row['norm_title']
    na = row['norm_artist']
    rev = row['revenue_usd']
    
    subset = valid_merged[(valid_merged['norm_title'] == nt) & (valid_merged['norm_artist'] == na)]
    display_title = subset['clean_title'].mode()[0]
    display_artist = subset['clean_artist'].mode()[0]
    track_count = subset['track_id'].nunique()
    
    top_candidates.append({
        "rank": i+1,
        "title": display_title,
        "artist": display_artist,
        "revenue": rev,
        "track_count": track_count
    })

print("__RESULT__:")
print(json.dumps(top_candidates))"""

env_args = {'var_function-call-3992495390837066285': 'file_storage/function-call-3992495390837066285.json', 'var_function-call-7409539752900977037': 'file_storage/function-call-7409539752900977037.json', 'var_function-call-16025719920181743167': {'top_20': [{'norm_title': '', 'norm_artist': '', 'revenue_usd': 203103.18}, {'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 5417.34}, {'norm_title': '', 'norm_artist': 'unknown', 'revenue_usd': 4851.83}, {'norm_title': '001', 'norm_artist': 'none', 'revenue_usd': 4681.75}, {'norm_title': 'tv', 'norm_artist': '', 'revenue_usd': 4527.58}, {'norm_title': '005', 'norm_artist': 'none', 'revenue_usd': 4281.18}, {'norm_title': '002', 'norm_artist': 'none', 'revenue_usd': 4237.16}, {'norm_title': '010', 'norm_artist': 'none', 'revenue_usd': 4163.48}, {'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur', 'norm_artist': 'syb van der ploeg', 'revenue_usd': 4132.27}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'revenue_usd': 4110.55}, {'norm_title': 'kapitel 01', 'norm_artist': 'kerstin gier', 'revenue_usd': 4091.12}, {'norm_title': '004', 'norm_artist': '', 'revenue_usd': 4026.71}, {'norm_title': 'beautiful instrumental', 'norm_artist': 'damian marley', 'revenue_usd': 4004.42}, {'norm_title': 'the story of your life', 'norm_artist': 'matthew barber', 'revenue_usd': 3962.97}, {'norm_title': 'thousand finger man salsoul 30th', 'norm_artist': 'candido', 'revenue_usd': 3934.83}, {'norm_title': 'a wandring minstrel i from the mikado', 'norm_artist': 'sir william gilbert sir arthur sullivan', 'revenue_usd': 3877.43}, {'norm_title': 'fret one grow old inside your wave', 'norm_artist': 'ugly winner', 'revenue_usd': 3844.09}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95}], 'winner': {'title': 'Όνειρα ζωής', 'artist': 'Χρήστος Δάντης', 'revenue': 203103.18}}, 'var_function-call-6781856173906030022': [{'rank': 1, 'title': '004-', 'artist': '', 'norm_title': '004', 'norm_artist': '', 'revenue': 7271.32, 'track_count': 8}, {'rank': 2, 'title': '003-', 'artist': '', 'norm_title': '003', 'norm_artist': '', 'revenue': 7090.13, 'track_count': 7}, {'rank': 3, 'title': '001-', 'artist': '', 'norm_title': '001', 'norm_artist': '', 'revenue': 6283.24, 'track_count': 6}, {'rank': 4, 'title': '005-', 'artist': '', 'norm_title': '005', 'norm_artist': '', 'revenue': 6155.29, 'track_count': 8}, {'rank': 5, 'title': 'Groovey', 'artist': 'Rich Matteson', 'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue': 5417.34, 'track_count': 4}, {'rank': 6, 'title': '009-', 'artist': '', 'norm_title': '009', 'norm_artist': '', 'revenue': 5045.7, 'track_count': 4}, {'rank': 7, 'title': '002-', 'artist': '', 'norm_title': '002', 'norm_artist': '', 'revenue': 5013.4400000000005, 'track_count': 4}, {'rank': 8, 'title': '010-', 'artist': '', 'norm_title': '010', 'norm_artist': '', 'revenue': 4734.360000000001, 'track_count': 5}, {'rank': 9, 'title': '012-', 'artist': '', 'norm_title': '012', 'norm_artist': '', 'revenue': 4641.08, 'track_count': 4}, {'rank': 10, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur', 'norm_artist': 'syb van der ploeg', 'revenue': 4132.27, 'track_count': 2}]}

exec(code, env_args)
