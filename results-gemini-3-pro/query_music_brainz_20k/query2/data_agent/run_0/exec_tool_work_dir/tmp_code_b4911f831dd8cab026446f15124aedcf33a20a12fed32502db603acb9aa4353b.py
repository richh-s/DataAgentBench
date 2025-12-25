code = """import json

sales_data = locals()['var_function-call-13739172751475832139']
# sales_data is a list of dicts: [{'store': 'iTunes', 'total_revenue': '505.61'}, ...]
# Note: total_revenue might be a string from the DB result.

max_revenue = -1.0
top_store = None

for record in sales_data:
    store = record['store']
    revenue = float(record['total_revenue'])
    if revenue > max_revenue:
        max_revenue = revenue
        top_store = store

result = {"top_store": top_store, "revenue": max_revenue}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2333264696016038417': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000'}], 'var_function-call-3486650620407779114': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_function-call-13739172751475832139': [{'store': 'iTunes', 'total_revenue': '505.61'}, {'store': 'Amazon Music', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'total_revenue': '116.20000000000002'}]}

exec(code, env_args)
