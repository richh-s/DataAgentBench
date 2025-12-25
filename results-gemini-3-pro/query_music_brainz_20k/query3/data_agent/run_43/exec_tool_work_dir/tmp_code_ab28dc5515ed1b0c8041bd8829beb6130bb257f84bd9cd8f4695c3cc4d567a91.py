code = """import json
import pandas as pd
import re

# Load sales data
sales_file_path = locals()['var_function-call-14714155237110464570']
with open(sales_file_path, 'r') as f:
    sales_list = json.load(f)

# Load tracks data
tracks_file_path = locals()['var_function-call-14566705962041392697']
with open(tracks_file_path, 'r') as f:
    tracks_list = json.load(f)

df_sales = pd.DataFrame(sales_list)
df_tracks = pd.DataFrame(tracks_list)

df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

def normalize_string(s):
    if not isinstance(s, str) or s.lower() == 'none':
        return "none"
    s = s.lower()
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^]]*\]', '', s)
    s = re.sub(r'[^\w\s]', '', s)
    s = " ".join(s.split())
    if not s: return "none"
    return s

def clean_row(row):
    title = row['title']
    artist = row['artist']
    n_title = normalize_string(title)
    n_artist = normalize_string(artist)
    return pd.Series([n_title, n_artist])

df[['n_title', 'n_artist']] = df.apply(clean_row, axis=1)

grouped = df.groupby(['n_title', 'n_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)
valid_grouped = grouped[grouped['n_title'] != 'none']

top_3 = valid_grouped.head(3)

ids_map = {}
for index, row in top_3.iterrows():
    key = f"{row['n_title']} | {row['n_artist']}"
    ids = df[(df['n_title'] == row['n_title']) & (df['n_artist'] == row['n_artist'])]['track_id'].tolist()
    ids_map[key] = ids

print("__RESULT__:")
print(json.dumps(ids_map))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json', 'var_function-call-5674796126939342252': 'file_storage/function-call-5674796126939342252.json', 'var_function-call-436051087863725612': 'file_storage/function-call-436051087863725612.json', 'var_function-call-14566705962041392697': 'file_storage/function-call-14566705962041392697.json', 'var_function-call-5965808366396911371': {'title': 'None', 'artist': 'None', 'revenue': 5201.42, 'ids': ['9788', '18790', '5048']}, 'var_function-call-15825784688763583739': {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'ids': ['1154', '12644']}, 'var_function-call-13714549246989091495': [{'track_id': '5048', 'source_id': '5', 'source_track_id': '12615860', 'title': 'None', 'artist': 'None', 'album': '20032010', 'year': '2010', 'length': '329000', 'language': 'None'}, {'track_id': '9788', 'source_id': '2', 'source_track_id': 'MBox15227023-HH', 'title': 'None', 'artist': 'None', 'album': 'The Metal Years: Gothic Doom', 'year': '02', 'length': '249', 'language': 'English'}, {'track_id': '18790', 'source_id': '2', 'source_track_id': 'MBox14734213-HH', 'title': 'None', 'artist': 'None', 'album': 'Ultimo Trem', 'year': 'None', 'length': '358', 'language': 'Portuguese'}], 'var_function-call-10112719935390993771': 'Done', 'var_function-call-15657660763049207833': [{'n_title': 'the fire still burns', 'n_artist': 'russ ballard', 'total_revenue': 3807.4}, {'n_title': 'three seasons', 'n_artist': 'swallow', 'total_revenue': 3803.5}, {'n_title': 'lescalade obscure', 'n_artist': 'charles koechlin', 'total_revenue': 3802.76}, {'n_title': 'stormy', 'n_artist': 'scott walker', 'total_revenue': 3792.1799999999994}, {'n_title': 'too beautiful', 'n_artist': 'will kimbrough', 'total_revenue': 3784.37}]}

exec(code, env_args)
