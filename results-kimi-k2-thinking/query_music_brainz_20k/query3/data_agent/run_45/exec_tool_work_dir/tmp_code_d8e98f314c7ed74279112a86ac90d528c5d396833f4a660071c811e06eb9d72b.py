code = """import json
import pandas as pd
import re

sales_file = var_functions.query_db:22
tracks_file = var_functions.query_db:23

with open(sales_file, 'r') as f:
    sales = json.load(f)
with open(tracks_file, 'r') as f:
    tracks = json.load(f)

sdf = pd.DataFrame(sales)
tdf = pd.DataFrame(tracks)

# Process data
sdf['total_revenue'] = sdf['total_revenue'].astype(float)
tdf['year'] = tdf['year'].astype(str)

# Normalize
def norm(x):
    s = str(x)
    return re.sub(r'[^\w]', '', s.lower())

tdf['key'] = tdf['title'].apply(norm) + '|' + tdf['artist'].apply(norm)

# Merge and aggregate
merged = pd.merge(sdf, tdf[['track_id','key','title','artist','album','year']], on='track_id', how='inner')
result = merged.groupby('key').agg({
    'total_revenue': 'sum',
    'title': lambda x: x.iloc[0],
    'artist': lambda x: x.iloc[0],
    'album': lambda x: x.iloc[0],
    'year': lambda x: x.iloc[0]
}).reset_index().sort_values('total_revenue', ascending=False)

top = result.iloc[0]
output = {
    'title': top['title'],
    'artist': top['artist'],
    'album': top['album'],
    'year': top['year'],
    'total_revenue': round(float(top['total_revenue']), 2)
}

print('__RESULT__:')
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 123}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json'}

exec(code, env_args)
