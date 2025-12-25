code = """import json

sales_data = locals()['var_function-call-9916321827820728224']
# sales_data is a list of dicts: [{"store": "...", "total_revenue": "..."}]

# Convert revenue to float and find max
max_revenue = -1.0
best_store = ""

for record in sales_data:
    store = record['store']
    rev = float(record['total_revenue'])
    if rev > max_revenue:
        max_revenue = rev
        best_store = store

result = {
    "store": best_store,
    "revenue": max_revenue
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11067573077550652297': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_function-call-11394413483197730491': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_function-call-9916321827820728224': [{'store': 'Apple Music', 'total_revenue': '116.20000000000002'}, {'store': 'iTunes', 'total_revenue': '505.61'}, {'store': 'Amazon Music', 'total_revenue': '304.13'}], 'var_function-call-11561123250209475518': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}]}

exec(code, env_args)
