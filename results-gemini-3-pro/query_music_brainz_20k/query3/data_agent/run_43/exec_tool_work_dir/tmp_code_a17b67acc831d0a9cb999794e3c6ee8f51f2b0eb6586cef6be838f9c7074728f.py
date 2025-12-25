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

df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

def normalize_string(s):
    if not isinstance(s, str) or s.lower() == 'none' or s.strip() == '':
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

ids_1 = df[df['n_title'].str.contains('kiä meil pahanu', case=False, na=False)]['track_id'].tolist()
ids_2 = df[df['n_title'] == 'groovey']['track_id'].tolist()

print("__RESULT__:")
print(json.dumps({"kiä": ids_1, "groovey": ids_2}))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json', 'var_function-call-5674796126939342252': 'file_storage/function-call-5674796126939342252.json', 'var_function-call-436051087863725612': 'file_storage/function-call-436051087863725612.json', 'var_function-call-14566705962041392697': 'file_storage/function-call-14566705962041392697.json', 'var_function-call-5965808366396911371': {'title': 'None', 'artist': 'None', 'revenue': 5201.42, 'ids': ['9788', '18790', '5048']}, 'var_function-call-15825784688763583739': {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'ids': ['1154', '12644']}, 'var_function-call-13714549246989091495': [{'track_id': '5048', 'source_id': '5', 'source_track_id': '12615860', 'title': 'None', 'artist': 'None', 'album': '20032010', 'year': '2010', 'length': '329000', 'language': 'None'}, {'track_id': '9788', 'source_id': '2', 'source_track_id': 'MBox15227023-HH', 'title': 'None', 'artist': 'None', 'album': 'The Metal Years: Gothic Doom', 'year': '02', 'length': '249', 'language': 'English'}, {'track_id': '18790', 'source_id': '2', 'source_track_id': 'MBox14734213-HH', 'title': 'None', 'artist': 'None', 'album': 'Ultimo Trem', 'year': 'None', 'length': '358', 'language': 'Portuguese'}], 'var_function-call-10112719935390993771': 'Done', 'var_function-call-15657660763049207833': [{'n_title': 'the fire still burns', 'n_artist': 'russ ballard', 'total_revenue': 3807.4}, {'n_title': 'three seasons', 'n_artist': 'swallow', 'total_revenue': 3803.5}, {'n_title': 'lescalade obscure', 'n_artist': 'charles koechlin', 'total_revenue': 3802.76}, {'n_title': 'stormy', 'n_artist': 'scott walker', 'total_revenue': 3792.1799999999994}, {'n_title': 'too beautiful', 'n_artist': 'will kimbrough', 'total_revenue': 3784.37}], 'var_function-call-16342077319805248095': {'the fire still burns | russ ballard': ['1154', '12644'], 'three seasons | swallow': ['6829', '2844'], 'lescalade obscure | charles koechlin': ['3775', '847']}, 'var_function-call-16922889568658719996': [{'track_id': '847', 'source_id': '5', 'source_track_id': '6413125', 'title': "L'Escalade obscure", 'artist': 'Charles Koechlin', 'album': 'Les Heures Persanes, Op. 65 (Kathryn Stott)', 'year': '2003', 'length': '211693', 'language': 'French'}, {'track_id': '1154', 'source_id': '1', 'source_track_id': 'WoM1704813', 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'album': 'The Fire Still Burns', 'year': 'None', 'length': '05:36', 'language': 'None'}, {'track_id': '2844', 'source_id': '1', 'source_track_id': 'WoM18417521', 'title': 'Three Seasons (Aresco)', 'artist': 'Swallow', 'album': 'Aresco', 'year': '2005', 'length': '04:01', 'language': 'None'}, {'track_id': '3775', 'source_id': '1', 'source_track_id': 'WoM12826241', 'title': "L'Escalade obscure (Les Heures Persanes, Op. 65 (Kathryn Stott))", 'artist': 'Charles Koechlin', 'album': 'Les Heures Persanes, Op. 65 (Kathryn Stott)', 'year': '2003', 'length': '03:31', 'language': 'None'}, {'track_id': '6829', 'source_id': '5', 'source_track_id': '9208755', 'title': 'Three Seasons', 'artist': 'Swallow', 'album': 'Aresco', 'year': '3005', 'length': '241786', 'language': 'Korean'}, {'track_id': '12644', 'source_id': '5', 'source_track_id': '852397', 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'album': 'The Fire Still Burns', 'year': 'None', 'length': '336866', 'language': 'English'}], 'var_function-call-3355862399934285287': 'Done', 'var_function-call-5895912729063434086': [2522.82, 1539.05], 'var_function-call-17459771876471873779': 19375, 'var_function-call-13270550622448143963': [{'count(*)': '19375'}], 'var_function-call-11975093273394770584': 'file_storage/function-call-11975093273394770584.json', 'var_function-call-12968849740624379504': {'title': '003-', 'artist': ' ', 'revenue': 8582.15, 'ids': ['5576', '14373', '11778', '10208', '15920', '7540', '3833', '9453', '19156']}, 'var_function-call-2986781660930395108': [{'n_title': '003', 'n_artist': 'none', 'total_revenue': 8582.15}, {'n_title': '001', 'n_artist': 'none', 'total_revenue': 7467.97}, {'n_title': '004', 'n_artist': 'none', 'total_revenue': 7271.32}, {'n_title': '005', 'n_artist': 'none', 'total_revenue': 6155.29}, {'n_title': '009', 'n_artist': 'none', 'total_revenue': 5045.700000000001}, {'n_title': '002', 'n_artist': 'none', 'total_revenue': 5013.4400000000005}, {'n_title': 'kiä meil pahanu', 'n_artist': 'none', 'total_revenue': 4916.110000000001}, {'n_title': '010', 'n_artist': 'none', 'total_revenue': 4734.36}, {'n_title': '012', 'n_artist': 'none', 'total_revenue': 4641.08}, {'n_title': '006', 'n_artist': 'none', 'total_revenue': 4366.82}], 'var_function-call-13399397623142841419': [{'n_title': 'kiä meil pahanu', 'n_artist': 'none', 'title': 'Kiä meil pahanu? (Mina lätsi Siidile)', 'artist': '[tiidmäldä]', 'revenue': 4916.110000000001}, {'n_title': 'groovey', 'n_artist': 'rich matteson', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 4128.59}, {'n_title': 'the fire still burns', 'n_artist': 'russ ballard', 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4}, {'n_title': 'three seasons', 'n_artist': 'swallow', 'title': 'Three Seasons', 'artist': 'Swallow', 'revenue': 3803.5}, {'n_title': 'lescalade obscure', 'n_artist': 'charles koechlin', 'title': "L'Escalade obscure (Les Heures Persanes, Op. 65 (Kathryn Stott))", 'artist': 'Charles Koechlin', 'revenue': 3802.76}, {'n_title': 'stormy', 'n_artist': 'scott walker', 'title': 'Stormy', 'artist': 'Scott Walker', 'revenue': 3792.1799999999994}, {'n_title': 'too beautiful', 'n_artist': 'will kimbrough', 'title': 'Too Beautiful (Godsend)', 'artist': 'Will Kimbrough', 'revenue': 3784.37}, {'n_title': 'zo gaat het leven aan je voor', 'n_artist': 'syb van der ploeg', 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 3779.05}, {'n_title': 'vostok', 'n_artist': 'craig padilla', 'title': 'Vostok', 'artist': 'Craig Padilla', 'revenue': 3767.95}, {'n_title': 'travel', 'n_artist': 'guts pie earshot', 'title': 'Travel (live)', 'artist': 'Guts Pie Earshot', 'revenue': 3703.98}]}

exec(code, env_args)
