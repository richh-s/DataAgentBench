code = """# Re-print the top 10 from the previous result (I computed it but only printed top 3 detailed)
# I will just run the grouping and print top 10 summary.

import json
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

def clean_string(s):
    if not isinstance(s, str): return ""
    return s.lower().strip()

def extract_artist_title(row):
    title = row['title']
    artist = row['artist']
    if not isinstance(title, str): title = ""
    if not isinstance(artist, str): artist = ""
    title_clean = title.strip()
    artist_clean = artist.strip()
    if artist_clean.lower() in ['none', '[unknown]', '']:
        if " - " in title_clean:
            parts = title_clean.split(" - ", 1)
            return parts[0], parts[1]
        else:
            return "unknown", title_clean
    return artist_clean, title_clean

normalized_data = []
for idx, row in df.iterrows():
    artist, title = extract_artist_title(row)
    title_norm = re.sub(r'^\d+[\.\-\s]+', '', title)
    title_core = re.sub(r'\s*\(.*?\)', '', title_norm)
    title_core = re.sub(r'\s*\[.*?\]', '', title_core)
    title_core = clean_string(title_core)
    artist_norm = clean_string(artist)
    
    if title_core in ['', 'none', 'unknown', 'track']: continue
    if artist_norm in ['', 'none', 'unknown']: continue
        
    normalized_data.append({
        'norm_artist': artist_norm,
        'norm_title': title_core,
        'revenue': row['total_revenue']
    })

df_norm = pd.DataFrame(normalized_data)
grouped = df_norm.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()
grouped = grouped.sort_values('revenue', ascending=False)

print("__RESULT__:")
print(json.dumps(grouped.head(10).to_dict(orient='records')))"""

env_args = {'var_function-call-9165943318207358128': 'file_storage/function-call-9165943318207358128.json', 'var_function-call-1686680427873547385': 'file_storage/function-call-1686680427873547385.json', 'var_function-call-13708768064711140461': [{'norm_artist': 'unknown', 'norm_title': '', 'revenue': 59287.18}, {'norm_artist': 'unknown', 'norm_title': 'none', 'revenue': 14647.52}, {'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5668.5}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say (album version)', 'revenue': 5180.93}, {'norm_artist': 'pras', 'norm_title': 'ghetto supastar (that is what you are)', 'revenue': 4933.98}, {'norm_artist': 'frankie goes to hollywood', 'norm_title': 'the power of love (rob searle club mix)', 'revenue': 4909.04}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue': 4881.42}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'revenue': 4770.54}, {'norm_artist': 'the turtles', 'norm_title': 'happy together', 'revenue': 4747.049999999999}, {'norm_artist': 'lemon d', 'norm_title': 'jah love (vip remix)', 'revenue': 4645.110000000001}], 'var_function-call-5994004812808301628': [{'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'revenue': 6611.56}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'revenue': 6259.3}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'revenue': 6125.339999999999}], 'var_function-call-14363952485309310589': [{'track_id': '6988', 'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner', 'revenue': 1762.8000000000002}, {'track_id': '7575', 'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner', 'revenue': 850.86}, {'track_id': '10606', 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 672.1200000000001}, {'track_id': '17167', 'title': '027-Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 1769.03}], 'var_function-call-18416138488497890443': [{'artist': 'fischerspooner', 'title': 'emerge', 'revenue': 6665.2699999999995, 'records': [{'original_title': 'Fischerspooner - Emerge (Dexter remix)', 'original_artist': 'None', 'revenue': 1610.46}, {'original_title': 'Emerge (Dexter remix) (#1)', 'original_artist': 'Fischerspooner', 'revenue': 1762.8000000000002}, {'original_title': 'Emerge (Dave Clarke remix)', 'original_artist': 'Fischerspooner', 'revenue': 850.86}, {'original_title': 'Emerge (Dexter remix)', 'original_artist': 'Fischerspooner', 'revenue': 672.1200000000001}, {'original_title': '027-Emerge (Dexter remix)', 'original_artist': 'Fischerspooner', 'revenue': 1769.03}]}, {'artist': 'syb van der ploeg', 'title': 'zo gaat het leven aan je voor', 'revenue': 6636.1, 'records': [{'original_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'original_artist': 'Syb van der Ploeg', 'revenue': 1754.6800000000003}, {'original_title': 'Zo gaat het leven aan je voor', 'original_artist': 'Syb van der Ploeg', 'revenue': 2024.37}, {'original_title': '006-Zo gaat het leven aan je voor', 'original_artist': 'Syb van der Ploeg', 'revenue': 1379.6699999999998}, {'original_title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'original_artist': 'None', 'revenue': 1477.38}]}, {'artist': 'ske', 'title': 'vagga', 'revenue': 6611.560000000001, 'records': [{'original_title': 'Ske - Vagga', 'original_artist': 'None', 'revenue': 1459.5600000000002}, {'original_title': 'Vagga', 'original_artist': 'Ske', 'revenue': 1358.13}, {'original_title': 'Vagga (Feelings Are Great)', 'original_artist': 'Ske', 'revenue': 2163.69}, {'original_title': '011-Vagga', 'original_artist': 'Ske', 'revenue': 1630.18}]}]}

exec(code, env_args)
