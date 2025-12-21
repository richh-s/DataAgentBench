code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-8682200878932963124'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8682200878932962997'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_merged = pd.merge(df_tracks, df_sales, on='track_id', how='left')
df_merged['total_revenue'] = df_merged['total_revenue'].fillna(0)

def normalize(s):
    if not isinstance(s, str):
        return ''
    s_clean = s.strip().lower()
    if s_clean == 'none' or s_clean == '':
        return ''
    s_clean = re.sub(r'[^\w\s]', '', s_clean)
    return s_clean.strip()

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

df_clean = df_merged[df_merged['norm_title'] != '']
grouped = df_clean.groupby(['norm_title', 'norm_artist']).agg({
    'total_revenue': 'sum',
    'title': 'first',
    'artist': 'first'
}).reset_index()

grouped = grouped.sort_values('total_revenue', ascending=False)
top_20 = grouped.head(20).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_20))"""

env_args = {'var_function-call-8682200878932963124': 'file_storage/function-call-8682200878932963124.json', 'var_function-call-8682200878932962997': 'file_storage/function-call-8682200878932962997.json', 'var_function-call-1519880724859668680': {'title': 'None', 'artist': 'None', 'revenue': 17139.25, 'norm_title': '', 'norm_artist': ''}, 'var_function-call-1274804052475506745': [{'norm_title': '004', 'norm_artist': '', 'total_revenue': 7271.32, 'title': '004-/', 'artist': 'None'}, {'norm_title': '003', 'norm_artist': '', 'total_revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'norm_title': '005', 'norm_artist': '', 'total_revenue': 6155.29, 'title': '005', 'artist': 'None'}, {'norm_title': '009', 'norm_artist': '', 'total_revenue': 5045.7, 'title': '009-  ', 'artist': ' '}, {'norm_title': '002', 'norm_artist': '', 'total_revenue': 5013.4400000000005, 'title': '002-', 'artist': 'None'}]}

exec(code, env_args)
