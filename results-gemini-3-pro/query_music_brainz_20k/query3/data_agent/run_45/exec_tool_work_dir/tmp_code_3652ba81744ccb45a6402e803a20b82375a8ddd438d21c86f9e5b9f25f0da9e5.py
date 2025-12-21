code = """import json
import pandas as pd
import re

sales_file_path = locals()['var_function-call-9165943318207358128']
tracks_file_path = locals()['var_function-call-1686680427873547385']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks = pd.DataFrame(tracks_data)
df = pd.merge(df_tracks, df_sales, on='track_id', how='inner')

# Filter for the top candidate
target_artist = "fischerspooner"
target_title = "emerge"

matched_records = []

def clean_string(s):
    if not isinstance(s, str):
        return ""
    return s.lower().strip()

for idx, row in df.iterrows():
    title = row['title']
    artist = row['artist']
    if not isinstance(title, str): title = ""
    if not isinstance(artist, str): artist = ""
    
    # Logic from previous step
    artist_clean = artist.strip()
    if artist_clean.lower() in ['none', '[unknown]', '']:
        if " - " in title:
            artist_clean = title.split(" - ", 1)[0]
    
    artist_norm = clean_string(artist_clean)
    
    title_norm = re.sub(r'^\d+[\.\-\s]+', '', title)
    title_core = re.sub(r'\s*\(.*?\)', '', title_norm)
    title_core = re.sub(r'\s*\[.*?\]', '', title_core)
    title_core = clean_string(title_core)
    
    if artist_norm == target_artist and title_core == target_title:
        matched_records.append({
            'track_id': row['track_id'],
            'title': row['title'],
            'artist': row['artist'],
            'revenue': row['total_revenue']
        })

print("__RESULT__:")
print(json.dumps(matched_records))"""

env_args = {'var_function-call-9165943318207358128': 'file_storage/function-call-9165943318207358128.json', 'var_function-call-1686680427873547385': 'file_storage/function-call-1686680427873547385.json', 'var_function-call-13708768064711140461': [{'norm_artist': 'unknown', 'norm_title': '', 'revenue': 59287.18}, {'norm_artist': 'unknown', 'norm_title': 'none', 'revenue': 14647.52}, {'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5668.5}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say (album version)', 'revenue': 5180.93}, {'norm_artist': 'pras', 'norm_title': 'ghetto supastar (that is what you are)', 'revenue': 4933.98}, {'norm_artist': 'frankie goes to hollywood', 'norm_title': 'the power of love (rob searle club mix)', 'revenue': 4909.04}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue': 4881.42}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'revenue': 4770.54}, {'norm_artist': 'the turtles', 'norm_title': 'happy together', 'revenue': 4747.049999999999}, {'norm_artist': 'lemon d', 'norm_title': 'jah love (vip remix)', 'revenue': 4645.110000000001}], 'var_function-call-5994004812808301628': [{'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'revenue': 6611.56}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'revenue': 6259.3}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'revenue': 6125.339999999999}]}

exec(code, env_args)
