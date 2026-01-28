code = """import json
# Access previous query results available as variables
a = var_call_kixf60Yb3uBUic9aLlOhLzs6
b = var_call_FK0012lD6kQmHZmvvmyVz5Qx
# Build name map
name_map = {rec['gmap_id']: rec['name'] for rec in b}
# Merge and convert counts to int
res = []
for rec in a:
    gid = rec['gmap_id']
    try:
        count = int(rec['high_reviews'])
    except:
        # if already int or cannot convert, keep as is
        count = rec['high_reviews']
    name = name_map.get(gid)
    res.append({'gmap_id': gid, 'name': name, 'high_reviews': count})
# Sort by high_reviews desc
res_sorted = sorted(res, key=lambda x: -x['high_reviews'])
# Output as JSON string
out = json.dumps(res_sorted)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kixf60Yb3uBUic9aLlOhLzs6': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}], 'var_call_FK0012lD6kQmHZmvvmyVz5Qx': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
