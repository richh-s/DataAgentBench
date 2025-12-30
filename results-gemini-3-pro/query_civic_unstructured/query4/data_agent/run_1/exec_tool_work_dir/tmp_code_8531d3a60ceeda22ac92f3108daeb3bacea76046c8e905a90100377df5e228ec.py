code = """import json
import re

# Load data
funding_path = locals()['var_function-call-12281122830220394756']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

docs_path = locals()['var_function-call-3253055519445541233']
with open(docs_path, 'r') as f:
    docs = json.load(f)

lines = []
for d in docs:
    lines.extend(d['text'].splitlines())

target_projects = ["Bluffs Park Shade Structure", "Marie Canyon Green Streets"]
target_dates = ["spring 2022", "march 2022", "april 2022", "may 2022"]
start_markers = ["begin construction", "start date", "construction start"]

matches = []

for i, line in enumerate(lines):
    line_clean = line.strip()
    matched_name = None
    for name in target_projects:
        if name.lower() in line_clean.lower() and len(line_clean) < len(name) + 15:
            matched_name = name
            break
            
    if matched_name:
        chunk = lines[i:i+20]
        for c_line in chunk:
            c_line_lower = c_line.lower()
            if any(td in c_line_lower for td in target_dates):
                if any(sm in c_line_lower for sm in start_markers):
                    matches.append({"project": matched_name, "context": c_line})

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-3253055519445541233': 'file_storage/function-call-3253055519445541233.json', 'var_function-call-14502065749304076563': ['Funding'], 'var_function-call-12281122830220394756': 'file_storage/function-call-12281122830220394756.json', 'var_function-call-6279881010501383237': {'count': 2, 'total_funding': 71000, 'projects': ['Bluffs Park Shade Structure', 'Marie Canyon Green Streets']}}

exec(code, env_args)
