code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-2511588746331634384'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-1045009178916472453'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def resolve_entity(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    if artist.lower() in ['none', 'null', '[unknown]', '']:
        artist = None
    
    if artist is None and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            artist = parts[0].strip()
            title = parts[1].strip()
            
    if artist is None:
        artist = "Unknown Artist"
        
    return pd.Series([title, artist])

df[['clean_title', 'clean_artist']] = df.apply(resolve_entity, axis=1)

def normalize_text(text):
    if not text: return ""
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    text = re.sub(r'^\d+[\s\.\-]+', '', text)
    return text.strip()

df['norm_title'] = df['clean_title'].apply(normalize_text)
df['norm_artist'] = df['clean_artist'].apply(normalize_text)

# Inspect Fischerspooner
fs_group = df[(df['norm_artist'] == 'fischerspooner') & (df['norm_title'] == 'emerge')]
fs_info = fs_group[['track_id', 'clean_title', 'clean_artist', 'total_revenue']].to_dict(orient='records')

# Inspect Syb van der Ploeg
syb_group = df[(df['norm_artist'] == 'syb van der ploeg') & (df['norm_title'] == 'zo gaat het leven aan je voor')]
syb_info = syb_group[['track_id', 'clean_title', 'clean_artist', 'total_revenue']].to_dict(orient='records')

# Inspect Ske
ske_group = df[(df['norm_artist'] == 'ske') & (df['norm_title'] == 'vagga')]
ske_info = ske_group[['track_id', 'clean_title', 'clean_artist', 'total_revenue']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps({"fischerspooner": fs_info, "syb": syb_info, "ske": ske_info}))"""

env_args = {'var_function-call-2511588746331634384': 'file_storage/function-call-2511588746331634384.json', 'var_function-call-1045009178916472453': 'file_storage/function-call-1045009178916472453.json', 'var_function-call-4121161695158870877': {'title': 'None', 'artist': 'Unknown Artist', 'total_revenue': 14647.52}, 'var_function-call-8228987460129439052': [{'norm_artist': 'unknown artist', 'norm_title': 'none', 'total_revenue': 14647.52}, {'norm_artist': 'unknown artist', 'norm_title': '003-', 'total_revenue': 6841.18}, {'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'total_revenue': 5417.34}, {'norm_artist': 'unknown artist', 'norm_title': '005-', 'total_revenue': 5222.0}, {'norm_artist': 'unknown artist', 'norm_title': '009-', 'total_revenue': 5045.7}, {'norm_artist': 'unknown artist', 'norm_title': '004-', 'total_revenue': 4868.47}, {'norm_artist': 'unknown artist', 'norm_title': '010-', 'total_revenue': 4734.36}, {'norm_artist': 'unknown artist', 'norm_title': '002-', 'total_revenue': 4119.89}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say (album version)', 'total_revenue': 4110.55}, {'norm_artist': 'kerstin gier', 'norm_title': 'kapitel 01', 'total_revenue': 4091.12}, {'norm_artist': 'damian marley', 'norm_title': 'beautiful (instrumental)', 'total_revenue': 4004.42}, {'norm_artist': 'matthew barber', 'norm_title': 'the story of your life', 'total_revenue': 3962.97}, {'norm_artist': 'unknown artist', 'norm_title': '006-', 'total_revenue': 3946.78}, {'norm_artist': 'sir william gilbert & sir arthur sullivan', 'norm_title': 'a wand\'ring minstrel i, from "the mikado"', 'total_revenue': 3877.43}, {'norm_artist': 'russ ballard', 'norm_title': 'the fire still burns', 'total_revenue': 3807.4}, {'norm_artist': 'craig padilla', 'norm_title': 'vostok', 'total_revenue': 3767.95}, {'norm_artist': 'byzantine', 'norm_title': 'oblivion beckons', 'total_revenue': 3759.01}, {'norm_artist': 'unknown artist', 'norm_title': '001-', 'total_revenue': 3742.44}, {'norm_artist': 'kenny rogers', 'norm_title': 'so in love with you', 'total_revenue': 3642.04}, {'norm_artist': 'unknown artist', 'norm_title': '012-', 'total_revenue': 3635.13}], 'var_function-call-2198972168939360834': [{'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'total_revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'total_revenue': 6611.56}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'total_revenue': 6259.3}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'total_revenue': 6125.34}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'total_revenue': 6008.71}, {'norm_artist': 'guts pie earshot', 'norm_title': 'travel', 'total_revenue': 5825.26}, {'norm_artist': 'hotstylz', 'norm_title': 'lookin boy', 'total_revenue': 5712.89}, {'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'total_revenue': 5668.5}, {'norm_artist': 'pras', 'norm_title': 'ghetto supastar', 'total_revenue': 5514.57}]}

exec(code, env_args)
