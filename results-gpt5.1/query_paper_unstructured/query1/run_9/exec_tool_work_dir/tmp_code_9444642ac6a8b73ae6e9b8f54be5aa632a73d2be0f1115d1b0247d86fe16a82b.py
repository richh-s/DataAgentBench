code = """import json, os
import pandas as pd

# Load full mongo result
with open(var_call_fBQqAp1gdyOhHK8muUcfhLvu, 'r') as f:
    mongo_records = json.load(f)

# Derive titles (filename without .txt)
food_titles = set()
for doc in mongo_records:
    fname = doc.get('filename', '')
    if fname.lower().endswith('.txt'):
        title = fname[:-4]
    else:
        title = fname
    food_titles.add(title)

# Load full citations result
with open(var_call_w9YXpclQ6GtGXYJqThP7MSmv, 'r') as f:
    cit_records = json.load(f)

# Filter citations to those whose title is in food_titles
food_citations = [r for r in cit_records if r.get('title') in food_titles]

# Sum citation_count (ensure int)
 total_citations = 0
for r in food_citations:
    try:
        total_citations += int(r.get('citation_count', 0))
    except Exception:
        pass

result = json.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_fBQqAp1gdyOhHK8muUcfhLvu': 'file_storage/call_fBQqAp1gdyOhHK8muUcfhLvu.json', 'var_call_w9YXpclQ6GtGXYJqThP7MSmv': 'file_storage/call_w9YXpclQ6GtGXYJqThP7MSmv.json'}

exec(code, env_args)
