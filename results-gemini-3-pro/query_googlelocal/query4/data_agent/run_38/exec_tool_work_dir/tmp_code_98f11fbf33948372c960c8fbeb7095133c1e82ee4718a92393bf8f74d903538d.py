code = """import json

reviews = locals()['var_function-call-14771073921437583124']
businesses = locals()['var_function-call-16886062111038634036']

# Create a dictionary for business names
bus_dict = {item['gmap_id']: item['name'] for item in businesses}

results = []
for r in reviews:
    g_id = r['gmap_id']
    name = bus_dict.get(g_id, "Unknown")
    count = r['review_count']
    results.append(f"{name} ({count})")

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11033070636827247163': [{'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2021-04-12 17:07:52', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2018-04-23 16:24:26', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2017-07-10 22:12:19', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'gmap_id': 'gmap_44'}], 'var_function-call-12188502300510195127': [{'gmap_id': 'gmap_35', 'review_count': '19'}, {'gmap_id': 'gmap_53', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'review_count': '14'}], 'var_function-call-16886062111038634036': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}], 'var_function-call-14771073921437583124': [{'gmap_id': 'gmap_35', 'review_count': '19'}, {'gmap_id': 'gmap_53', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'review_count': '14'}]}

exec(code, env_args)
