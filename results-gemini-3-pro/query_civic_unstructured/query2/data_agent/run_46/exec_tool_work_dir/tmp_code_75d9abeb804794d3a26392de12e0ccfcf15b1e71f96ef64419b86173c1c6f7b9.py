code = """import json
import re

# Load data
with open(locals()['var_function-call-14713834321312381364'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-14713834321312381855'], 'r') as f:
    civic_docs = json.load(f)
full_text = " ".join([doc.get('text', '') for doc in civic_docs])

# Projects to check
check_list = []
for p in funding_data:
    name = p['Project_Name']
    if any(k in name.lower() for k in ['park', 'point dume', 'legacy', 'playground']):
        check_list.append(name)

results = {}

for name in check_list:
    starts = [m.start() for m in re.finditer(re.escape(name), full_text)]
    snippets = []
    for start in starts:
        # Use replace with escaped newline char for python string
        snippet = full_text[start:start+500].replace('\n', ' ') 
        snippets.append(snippet)
    results[name] = snippets

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-14713834321312381364': 'file_storage/function-call-14713834321312381364.json', 'var_function-call-14713834321312381855': 'file_storage/function-call-14713834321312381855.json', 'var_function-call-14503968957198369253': {'matched_projects': ['Bluffs Park Shade Structure'], 'total_funding': 21000}}

exec(code, env_args)
