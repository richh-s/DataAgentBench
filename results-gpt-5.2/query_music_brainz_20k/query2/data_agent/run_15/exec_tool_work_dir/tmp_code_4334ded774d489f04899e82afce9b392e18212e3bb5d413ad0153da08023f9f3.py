code = """import json
# var_call_FABQS3qzbORWD2YqFAAGOzqd is store totals
rows = var_call_FABQS3qzbORWD2YqFAAGOzqd
# ensure numeric
for r in rows:
    r['revenue_usd'] = float(r['revenue_usd'])
# top store
top = max(rows, key=lambda x: x['revenue_usd'])
result = {"store": top['store'], "revenue_usd": round(top['revenue_usd'], 2)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Fx5o83gYnpferTUACu5BEFGK': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_ofAFWjNyXOq0m2M0iL3CN5e7': [{'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}, {'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_FABQS3qzbORWD2YqFAAGOzqd': [{'store': 'iTunes', 'revenue_usd': '505.61'}, {'store': 'Amazon Music', 'revenue_usd': '304.13'}, {'store': 'Apple Music', 'revenue_usd': '116.20000000000002'}], 'var_call_TRQRZjjOB81VTzOyYFBc4A0S': [{'track_id': '4122', 'store': 'Apple Music', 'country': 'Germany', 'units_sold': '47', 'revenue_usd': '47.52'}, {'track_id': '4122', 'store': 'Amazon Music', 'country': 'France', 'units_sold': '262', 'revenue_usd': '304.13'}, {'track_id': '4628', 'store': 'iTunes', 'country': 'France', 'units_sold': '469', 'revenue_usd': '505.61'}, {'track_id': '14080', 'store': 'Apple Music', 'country': 'UK', 'units_sold': '59', 'revenue_usd': '68.68'}], 'var_call_gCjlMmBjlS3pxPf9SNi7qSLF': [{'track_id': '4628', 'revenue_usd': '505.61'}, {'track_id': '4122', 'revenue_usd': '351.65'}, {'track_id': '14080', 'revenue_usd': '68.68'}]}

exec(code, env_args)
