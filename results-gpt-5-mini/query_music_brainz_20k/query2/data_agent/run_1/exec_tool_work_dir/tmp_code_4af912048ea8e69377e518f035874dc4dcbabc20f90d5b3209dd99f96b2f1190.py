code = """import json
sales = var_call_CykEEL2rMUm5yzounzxz5Rg0
# Convert revenue strings to floats and find max
for r in sales:
    try:
        r['total_revenue_usd'] = float(r['total_revenue_usd'])
    except:
        r['total_revenue_usd'] = None

# Find store with max revenue
max_store = max(sales, key=lambda x: (x['total_revenue_usd'] is not None, x['total_revenue_usd']))

output = {'top_store': max_store['store'], 'revenue_usd': max_store['total_revenue_usd'], 'all_stores': sales}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_JeNOHXWVJNWbh4shv0ffr1hv': 'file_storage/call_JeNOHXWVJNWbh4shv0ffr1hv.json', 'var_call_E3QFM2kxbpqtDlvt7N6LhNcX': {'track_ids': [7, 4122, 4628, 13758, 14080], 'matches_count': 5, 'matches_sample': [{'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '13758', 'source_id': '1', 'source_track_id': 'WoM21220012', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005', 'length': 'None', 'language': '02:57'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}]}, 'var_call_CykEEL2rMUm5yzounzxz5Rg0': [{'store': 'Amazon Music', 'total_revenue_usd': '1108.99'}, {'store': 'Apple Music', 'total_revenue_usd': '984.48'}, {'store': 'iTunes', 'total_revenue_usd': '916.8600000000001'}, {'store': 'Google Play', 'total_revenue_usd': '51.4'}]}

exec(code, env_args)
