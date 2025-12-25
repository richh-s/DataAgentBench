code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-9894359997541209422'], 'r') as f:
    tracks = json.load(f)
with open(locals()['var_function-call-9894359997541209045'], 'r') as f:
    sales = json.load(f)

df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0)

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_string(s):
    if s is None:
        return ""
    s = str(s).strip()
    if s.lower() in ["none", "[unknown]", "unknown", ""]:
        return ""
    return s

def extract_artist_title(row):
    title = clean_string(row['title'])
    artist = clean_string(row['artist'])
    if not artist and " - " in title:
        parts = title.split(" - ", 1)
        if len(parts) == 2:
            return parts[1].strip(), parts[0].strip()
    return title, artist

processed = merged.apply(extract_artist_title, axis=1, result_type='expand')
merged['clean_title'] = processed[0]
merged['clean_artist'] = processed[1]
merged['norm_title'] = merged['clean_title'].str.lower().str.strip()
merged['norm_artist'] = merged['clean_artist'].str.lower().str.strip()

# Filter
def is_valid_title(s):
    if not s: return False
    if s in ["none", "unknown", "track", "audio"]: return False
    if re.match(r'^\d{2,}-?$', s): return False
    return True

merged = merged[merged['norm_title'].apply(is_valid_title)]

# Inspect "groovey"
mask = (merged['norm_title'] == "groovey") & (merged['norm_artist'] == "rich matteson")
constituents = merged[mask][['track_id', 'title', 'artist', 'total_revenue']]

print("__RESULT__:")
print(constituents.to_json(orient='records'))"""

env_args = {'var_function-call-9894359997541209422': 'file_storage/function-call-9894359997541209422.json', 'var_function-call-9894359997541209045': 'file_storage/function-call-9894359997541209045.json', 'var_function-call-9024924983516554567': {'title': 'unknown', 'artist': 'None', 'revenue': 17865.87, 'norm_title': '', 'norm_artist': ''}, 'var_function-call-8087983147323971888': [{'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, {'norm_title': '010-', 'norm_artist': 'none', 'total_revenue': 4163.48}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': '001-', 'norm_artist': 'none', 'total_revenue': 3742.44}, {'norm_title': '003-', 'norm_artist': 'none', 'total_revenue': 3446.78}, {'norm_title': '003-', 'norm_artist': '', 'total_revenue': 3394.4}, {'norm_title': '005-', 'norm_artist': 'none', 'total_revenue': 3347.89}, {'norm_title': '002-', 'norm_artist': 'none', 'total_revenue': 3343.61}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63}, {'norm_title': 'unknown', 'norm_artist': 'none', 'total_revenue': 3218.35}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'total_revenue': 3052.75}, {'norm_title': 'al stewart - year of the cat', 'norm_artist': 'none', 'total_revenue': 3049.93}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'total_revenue': 3008.01}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'total_revenue': 2969.33}], 'var_function-call-10487997172863458026': [{'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 5417.34}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 4110.55}, {'norm_title': 'kapitel 01', 'norm_artist': 'kerstin gier', 'total_revenue': 4091.12}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 4004.42}, {'norm_title': 'the story of your life', 'norm_artist': 'matthew barber', 'total_revenue': 3962.97}, {'norm_title': 'a wand\'ring minstrel i, from "the mikado"', 'norm_artist': 'sir william gilbert & sir arthur sullivan', 'total_revenue': 3877.43}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': 'oblivion beckons', 'norm_artist': 'byzantine', 'total_revenue': 3759.01}, {'norm_title': 'so in love with you', 'norm_artist': 'kenny rogers', 'total_revenue': 3642.04}]}

exec(code, env_args)
