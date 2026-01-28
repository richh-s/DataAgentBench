code = """import json, pandas as pd, re

# load sales top track_ids (already list)
sales_top = var_call_WeMdThnlSO2XpofTObMjZB9Q
# load tracks full from json path
path = var_call_8XZTNsWdvhSxJTOMCVquJ2sf
with open(path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_top)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

df_tracks = pd.DataFrame(tracks)
for c in ['track_id']:
    df_tracks[c] = df_tracks[c].astype(int)

def norm(s):
    if s is None:
        return ''
    s = str(s).lower().strip()
    if s == 'none' or s == '[unknown]':
        return ''
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    return s.strip()

df_tracks['n_title'] = df_tracks['title'].apply(norm)
df_tracks['n_artist'] = df_tracks['artist'].apply(norm)
df_tracks['n_album'] = df_tracks['album'].apply(norm)

def norm_year(y):
    if y is None:
        return None
    y = str(y).strip().strip("'")
    if y.lower() == 'none' or y == '':
        return None
    # keep digits
    dig = re.sub(r'[^0-9]', '', y)
    if dig == '':
        return None
    if len(dig) == 4:
        return int(dig)
    if len(dig) == 2:
        v = int(dig)
        return 1900+v if v >= 30 else 2000+v
    if len(dig) == 1:
        return None
    # other lengths: take last 4 if possible
    if len(dig) > 4:
        return int(dig[-4:])
    return None

df_tracks['n_year'] = df_tracks['year'].apply(norm_year)

# canonical key for entity resolution: title+artist primarily; fallback to title+album if artist missing
key1 = df_tracks['n_title'] + '|' + df_tracks['n_artist']
key2 = df_tracks['n_title'] + '|alb|' + df_tracks['n_album']
df_tracks['entity_key'] = key1.where(df_tracks['n_artist']!='', key2)

# map track_id to entity_key and representative metadata
id_to_key = df_tracks.set_index('track_id')['entity_key'].to_dict()

# representative per entity: prefer rows with non-empty artist and album, and with a plausible year
rep = df_tracks.copy()
rep['score'] = (rep['n_artist'].ne('').astype(int)*4 + rep['n_album'].ne('').astype(int)*2 + rep['n_year'].notna().astype(int))
rep = rep.sort_values(['entity_key','score'], ascending=[True, False])
rep_best = rep.groupby('entity_key', as_index=False).first()[['entity_key','title','artist','album','n_year']]

# aggregate revenue by entity across top track_ids list only (may miss if entity has multiple ids not in top 200)
# So compute across ALL sales track_ids would be needed; but we only have top 200 per-track. We'll instead compute entity revenue using full sales table via another query? can't here.
# We'll approximate by querying full sales aggregation by entity keys using join in python by fetching all sales by track_id.

print('__RESULT__:')
print(json.dumps({'need_full_sales': True, 'top_track_id': int(df_sales.iloc[0].track_id), 'top_track_revenue': float(df_sales.iloc[0].total_revenue_usd)}))"""

env_args = {'var_call_WeMdThnlSO2XpofTObMjZB9Q': 'file_storage/call_WeMdThnlSO2XpofTObMjZB9Q.json', 'var_call_8XZTNsWdvhSxJTOMCVquJ2sf': 'file_storage/call_8XZTNsWdvhSxJTOMCVquJ2sf.json'}

exec(code, env_args)
