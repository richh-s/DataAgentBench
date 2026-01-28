code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_TE6eIzVlJX7wery4Q3ItVuZm, 'r') as f:
    tracks = json.load(f)
with open(var_call_2SwKV6Zc2c9SKoa2EQ7QMvj0, 'r') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure revenue is numeric
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Aggregate sales by track_id
sales_by_track = df_sales.groupby('track_id', as_index=False)['revenue_usd'].sum().rename(columns={'revenue_usd': 'total_revenue'})

# Normalize function for entity resolution
def normalize(s):
    s = (s or '')
    s = str(s).lower()
    s = re.sub(r"\(.*?\)", ' ', s)  # remove parenthetical content
    s = re.sub(r"feat\.?|ft\.?", ' ', s)
    s = re.sub(r"[^a-z0-9\s]", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# Prepare tracks fields
df_tracks['title'] = df_tracks['title'].fillna('').astype(str)
df_tracks['artist'] = df_tracks['artist'].fillna('').astype(str)

df_tracks['norm_title'] = df_tracks['title'].apply(normalize)
# For artist, when 'None' or empty, keep as empty
df_tracks['norm_artist'] = df_tracks['artist'].apply(lambda x: '' if x in [None, 'None', ''] else normalize(x))

# Entity key
df_tracks['entity_key'] = df_tracks['norm_title'] + '||' + df_tracks['norm_artist']

# Merge sales totals into tracks
merged = pd.merge(df_tracks, sales_by_track, on='track_id', how='left')
merged['total_revenue'] = pd.to_numeric(merged['total_revenue']).fillna(0.0)

# Group by entity (resolved song) and sum revenues across track_ids
grouped = merged.groupby('entity_key').agg({
    'total_revenue': 'sum',
    'title': lambda x: x.dropna().astype(str).iloc[0] if len(x.dropna())>0 else '',
    'artist': lambda x: x.dropna().astype(str).iloc[0] if len(x.dropna())>0 else '',
    'track_id': lambda x: list(x)
}).reset_index()

# Select the entity with highest total revenue
if len(grouped) == 0:
    result = {'title': None, 'artist': None, 'total_revenue': 0.0, 'contributing_track_ids': []}
else:
    best = grouped.sort_values('total_revenue', ascending=False).iloc[0]
    result = {
        'title': best['title'],
        'artist': best['artist'],
        'total_revenue': float(best['total_revenue']),
        'contributing_track_ids': best['track_id']
    }

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_zB7bi0wlD6IymtPIl9UemnSj': ['tracks'], 'var_call_sMBknNVlGcy0V5p6dgFqYDga': ['sales'], 'var_call_FY6Q6UNe8BDvoEF16xXX7JAC': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}, {'track_id': '12984', 'total_revenue': '2401.71'}, {'track_id': '6208', 'total_revenue': '2385.0299999999997'}, {'track_id': '666', 'total_revenue': '2382.74'}, {'track_id': '12620', 'total_revenue': '2377.59'}, {'track_id': '19232', 'total_revenue': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue': '2365.59'}, {'track_id': '3462', 'total_revenue': '2359.23'}, {'track_id': '9639', 'total_revenue': '2351.68'}, {'track_id': '18760', 'total_revenue': '2349.33'}, {'track_id': '2516', 'total_revenue': '2346.18'}, {'track_id': '6326', 'total_revenue': '2331.91'}, {'track_id': '5836', 'total_revenue': '2321.31'}, {'track_id': '9988', 'total_revenue': '2317.41'}, {'track_id': '18508', 'total_revenue': '2308.44'}, {'track_id': '10760', 'total_revenue': '2293.1099999999997'}, {'track_id': '9002', 'total_revenue': '2288.23'}, {'track_id': '14169', 'total_revenue': '2281.23'}, {'track_id': '9649', 'total_revenue': '2276.7200000000003'}, {'track_id': '10856', 'total_revenue': '2275.85'}, {'track_id': '7422', 'total_revenue': '2275.04'}, {'track_id': '8705', 'total_revenue': '2273.46'}, {'track_id': '5933', 'total_revenue': '2271.62'}, {'track_id': '5809', 'total_revenue': '2269.24'}, {'track_id': '16084', 'total_revenue': '2259.8599999999997'}, {'track_id': '9652', 'total_revenue': '2251.2200000000003'}, {'track_id': '3412', 'total_revenue': '2250.04'}, {'track_id': '15664', 'total_revenue': '2249.3900000000003'}, {'track_id': '12207', 'total_revenue': '2248.7200000000003'}, {'track_id': '5467', 'total_revenue': '2246.94'}, {'track_id': '13102', 'total_revenue': '2244.51'}, {'track_id': '4145', 'total_revenue': '2243.27'}, {'track_id': '13132', 'total_revenue': '2238.21'}, {'track_id': '13211', 'total_revenue': '2233.62'}, {'track_id': '2244', 'total_revenue': '2230.04'}, {'track_id': '18846', 'total_revenue': '2227.95'}, {'track_id': '2029', 'total_revenue': '2226.42'}, {'track_id': '3488', 'total_revenue': '2222.25'}, {'track_id': '17669', 'total_revenue': '2212.4700000000003'}, {'track_id': '12969', 'total_revenue': '2211.97'}, {'track_id': '12551', 'total_revenue': '2210.78'}], 'var_call_TE6eIzVlJX7wery4Q3ItVuZm': 'file_storage/call_TE6eIzVlJX7wery4Q3ItVuZm.json', 'var_call_2SwKV6Zc2c9SKoa2EQ7QMvj0': 'file_storage/call_2SwKV6Zc2c9SKoa2EQ7QMvj0.json'}

exec(code, env_args)
