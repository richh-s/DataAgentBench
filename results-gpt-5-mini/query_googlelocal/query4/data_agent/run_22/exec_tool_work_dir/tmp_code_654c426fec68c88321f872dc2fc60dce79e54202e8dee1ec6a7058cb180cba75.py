code = """import json
# Access previous query results
rl1 = var_call_dtBYbxhOqBKkXexz5hfu6h1W
rl2 = var_call_tzqjbclcoli9OsLgGCGguzqi

# Convert high_reviews to int and build dict
counts = {r['gmap_id']: int(r['high_reviews']) for r in rl1}
names = {b['gmap_id']: b['name'] for b in rl2}

# Merge and prepare final ordered list
result_list = []
for gid, cnt in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    name = names.get(gid, None)
    result_list.append({'name': name, 'high_reviews': cnt})

# Ensure only top 3
result_list = result_list[:3]

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_dtBYbxhOqBKkXexz5hfu6h1W': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}], 'var_call_tzqjbclcoli9OsLgGCGguzqi': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
