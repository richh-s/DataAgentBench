code = """import json, re
# Access previous query result and mapping
top = var_call_59Wif8bCw8BI2UrHXD8swYZH
map_entry = var_call_ITRhurQYqmqouZ6E2lmh638H

# map_entry may be a filepath (string) or a dict
if isinstance(map_entry, str):
    with open(map_entry, 'r') as f:
        mapping = json.load(f)
else:
    mapping = map_entry

company_map = mapping.get('company_map', {})

def extract_name(desc):
    if not desc or not isinstance(desc, str):
        return desc
    parts = re.split(r"\s(?:is|specializes|offers|provides|operates|focuses|is an|is a|is part|is renowned|is primarily|is dedicated|is a leading|is an investment|is an independent|is known|specializing)\b", desc, maxsplit=1, flags=re.I)
    name = parts[0].strip()
    return name

names = []
for rec in top:
    sym = rec.get('symbol')
    desc = company_map.get(sym, '')
    name = extract_name(desc)
    if not name:
        name = sym
    names.append(name)

# Output JSON-serializable string
print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_call_XHd94ZK4eaI4ZdpusJOXlZv5': 'file_storage/call_XHd94ZK4eaI4ZdpusJOXlZv5.json', 'var_call_JlxE4BuJT5co98rQkeCxMO0k': 'file_storage/call_JlxE4BuJT5co98rQkeCxMO0k.json', 'var_call_ITRhurQYqmqouZ6E2lmh638H': 'file_storage/call_ITRhurQYqmqouZ6E2lmh638H.json', 'var_call_59Wif8bCw8BI2UrHXD8swYZH': [{'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}, {'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}, {'symbol': 'CRM', 'up': '137.0', 'down': '113.0'}, {'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}, {'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}]}

exec(code, env_args)
