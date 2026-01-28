code = """import json
import pandas as pd

df = pd.DataFrame(var_call_id1qZxekEFpfguAKNCiSiXh1)
# convert revenue to float
df['revenue_usd'] = df['revenue_usd'].astype(float)
# aggregate revenue by store across all track_ids
group = df.groupby('store', as_index=False)['revenue_usd'].sum()
# round to 2 decimals
group['revenue_usd'] = group['revenue_usd'].round(2)
# find max
max_row = group.loc[group['revenue_usd'].idxmax()]
result = {"store": max_row['store'], "revenue_usd": float(max_row['revenue_usd'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vUYVsmDtIhcltgfTECEoT6hm': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_call_8kukIpZCnWnepgr1S9LzQa2H': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '13758', 'source_id': '1', 'source_track_id': 'WoM21220012', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005', 'length': 'None', 'language': '02:57'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_call_id1qZxekEFpfguAKNCiSiXh1': [{'track_id': '4122', 'store': 'Amazon Music', 'revenue_usd': '304.13'}, {'track_id': '13758', 'store': 'Apple Music', 'revenue_usd': '477.06'}, {'track_id': '13758', 'store': 'iTunes', 'revenue_usd': '148.95'}, {'track_id': '14080', 'store': 'Apple Music', 'revenue_usd': '68.68'}, {'track_id': '4628', 'store': 'iTunes', 'revenue_usd': '505.61'}, {'track_id': '4122', 'store': 'Apple Music', 'revenue_usd': '47.52'}, {'track_id': '13758', 'store': 'Amazon Music', 'revenue_usd': '378.1'}, {'track_id': '13758', 'store': 'Google Play', 'revenue_usd': '51.4'}]}

exec(code, env_args)
