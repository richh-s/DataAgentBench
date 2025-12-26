code = """import json
import pandas as pd
# Load project names with funding > $50,000
with open(var_call_ahtNvy0j3gEUzAg6tZcyRzw1, 'r') as f:
    funding_projects = json.load(f)
project_names = set([entry['Project_Name'] for entry in funding_projects])

# Load civic docs text
with open(var_call_g0aAyqNqzIYzjLGdHFCuTC7H, 'r') as f:
    civic_docs = json.load(f)
all_text = ' '.join(doc['text'] for doc in civic_docs)

# Find project names in the text which have 'design' status and are type 'capital'
# Lower-case everything for easier search
text_lower = all_text.lower()

capital_design_projects = set()
for name in project_names:
    name_lc = name.lower()
    # Check if project name is present and the status is 'design' and type is 'capital'
    # Look for keywords near the project name
    idx = text_lower.find(name_lc)
    if idx != -1:
        # Search around the name for status/type
        window = text_lower[max(0, idx-300):idx+300]
        if 'design' in window and 'capital' in window:
            capital_design_projects.add(name)
            continue
        # Sometimes 'capital improvement project(s)' is used, so check that variant
        if 'design' in window and 'capital improvement' in window:
            capital_design_projects.add(name)
            continue

result = len(capital_design_projects)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ahtNvy0j3gEUzAg6tZcyRzw1': 'file_storage/call_ahtNvy0j3gEUzAg6tZcyRzw1.json', 'var_call_g0aAyqNqzIYzjLGdHFCuTC7H': 'file_storage/call_g0aAyqNqzIYzjLGdHFCuTC7H.json'}

exec(code, env_args)
