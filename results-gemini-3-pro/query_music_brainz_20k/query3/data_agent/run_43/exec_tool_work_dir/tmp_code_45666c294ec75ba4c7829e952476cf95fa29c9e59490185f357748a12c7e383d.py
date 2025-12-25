code = """import json
import pandas as pd
import re

# Load sales data
sales_file_path = locals()['var_function-call-14714155237110464570']
with open(sales_file_path, 'r') as f:
    sales_list = json.load(f)

# Load tracks data
tracks_file_path = locals()['var_function-call-11975093273394770584']
with open(tracks_file_path, 'r') as f:
    tracks_list = json.load(f)

df_sales = pd.DataFrame(sales_list)
df_tracks = pd.DataFrame(tracks_list)

# Ensure types match
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
df = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

# Normalization
def normalize_string(s):
    if not isinstance(s, str) or s.lower() == 'none' or s.strip() == '':
        return "none"
    s = s.lower()
    # Remove text in parenthesis (often contains remix info, year, etc which might differ)
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^]]*\]', '', s)
    # Remove punctuation
    s = re.sub(r'[^\w\s]', '', s)
    # Remove extra whitespace
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

# Group
grouped = df.groupby(['n_title', 'n_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Filter invalid
valid_grouped = grouped[(grouped['n_title'] != 'none')]

# Get Top 1
if not valid_grouped.empty:
    top_row = valid_grouped.iloc[0]
    top_n_title = top_row['n_title']
    top_n_artist = top_row['n_artist']
    
    # Get original display info (just pick one)
    original_rows = df[(df['n_title'] == top_n_title) & (df['n_artist'] == top_n_artist)]
    best_display = original_rows.iloc[0]
    
    result = {
        "title": best_display['title'],
        "artist": best_display['artist'],
        "revenue": top_row['total_revenue'],
        "ids": original_rows['track_id'].tolist()
    }
else:
    result = {"error": "No valid tracks"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json', 'var_function-call-5674796126939342252': 'file_storage/function-call-5674796126939342252.json', 'var_function-call-436051087863725612': 'file_storage/function-call-436051087863725612.json', 'var_function-call-14566705962041392697': 'file_storage/function-call-14566705962041392697.json', 'var_function-call-5965808366396911371': {'title': 'None', 'artist': 'None', 'revenue': 5201.42, 'ids': ['9788', '18790', '5048']}, 'var_function-call-15825784688763583739': {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'ids': ['1154', '12644']}, 'var_function-call-13714549246989091495': [{'track_id': '5048', 'source_id': '5', 'source_track_id': '12615860', 'title': 'None', 'artist': 'None', 'album': '20032010', 'year': '2010', 'length': '329000', 'language': 'None'}, {'track_id': '9788', 'source_id': '2', 'source_track_id': 'MBox15227023-HH', 'title': 'None', 'artist': 'None', 'album': 'The Metal Years: Gothic Doom', 'year': '02', 'length': '249', 'language': 'English'}, {'track_id': '18790', 'source_id': '2', 'source_track_id': 'MBox14734213-HH', 'title': 'None', 'artist': 'None', 'album': 'Ultimo Trem', 'year': 'None', 'length': '358', 'language': 'Portuguese'}], 'var_function-call-10112719935390993771': 'Done', 'var_function-call-15657660763049207833': [{'n_title': 'the fire still burns', 'n_artist': 'russ ballard', 'total_revenue': 3807.4}, {'n_title': 'three seasons', 'n_artist': 'swallow', 'total_revenue': 3803.5}, {'n_title': 'lescalade obscure', 'n_artist': 'charles koechlin', 'total_revenue': 3802.76}, {'n_title': 'stormy', 'n_artist': 'scott walker', 'total_revenue': 3792.1799999999994}, {'n_title': 'too beautiful', 'n_artist': 'will kimbrough', 'total_revenue': 3784.37}], 'var_function-call-16342077319805248095': {'the fire still burns | russ ballard': ['1154', '12644'], 'three seasons | swallow': ['6829', '2844'], 'lescalade obscure | charles koechlin': ['3775', '847']}, 'var_function-call-16922889568658719996': [{'track_id': '847', 'source_id': '5', 'source_track_id': '6413125', 'title': "L'Escalade obscure", 'artist': 'Charles Koechlin', 'album': 'Les Heures Persanes, Op. 65 (Kathryn Stott)', 'year': '2003', 'length': '211693', 'language': 'French'}, {'track_id': '1154', 'source_id': '1', 'source_track_id': 'WoM1704813', 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'album': 'The Fire Still Burns', 'year': 'None', 'length': '05:36', 'language': 'None'}, {'track_id': '2844', 'source_id': '1', 'source_track_id': 'WoM18417521', 'title': 'Three Seasons (Aresco)', 'artist': 'Swallow', 'album': 'Aresco', 'year': '2005', 'length': '04:01', 'language': 'None'}, {'track_id': '3775', 'source_id': '1', 'source_track_id': 'WoM12826241', 'title': "L'Escalade obscure (Les Heures Persanes, Op. 65 (Kathryn Stott))", 'artist': 'Charles Koechlin', 'album': 'Les Heures Persanes, Op. 65 (Kathryn Stott)', 'year': '2003', 'length': '03:31', 'language': 'None'}, {'track_id': '6829', 'source_id': '5', 'source_track_id': '9208755', 'title': 'Three Seasons', 'artist': 'Swallow', 'album': 'Aresco', 'year': '3005', 'length': '241786', 'language': 'Korean'}, {'track_id': '12644', 'source_id': '5', 'source_track_id': '852397', 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'album': 'The Fire Still Burns', 'year': 'None', 'length': '336866', 'language': 'English'}], 'var_function-call-3355862399934285287': 'Done', 'var_function-call-5895912729063434086': [2522.82, 1539.05], 'var_function-call-17459771876471873779': 19375, 'var_function-call-13270550622448143963': [{'count(*)': '19375'}], 'var_function-call-11975093273394770584': 'file_storage/function-call-11975093273394770584.json'}

exec(code, env_args)
