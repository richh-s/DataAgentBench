code = """import json

data = locals()['var_function-call-10338142524448314340']
# data is a list of dicts: [{'store': 'iTunes', 'total_revenue': '505.61'}, ...]
# convert revenue to float just in case
for d in data:
    d['total_revenue'] = float(d['total_revenue'])

# Sort by revenue
sorted_data = sorted(data, key=lambda x: x['total_revenue'], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_data))"""

env_args = {'var_function-call-1744611271622826051': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis'}], 'var_function-call-13868021498345207579': [{'store': 'Amazon Music', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'total_revenue': '47.52'}], 'var_function-call-11448880110634180468': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_function-call-10338142524448314340': [{'store': 'iTunes', 'total_revenue': '505.61'}, {'store': 'Amazon Music', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'total_revenue': '116.20000000000002'}]}

exec(code, env_args)
