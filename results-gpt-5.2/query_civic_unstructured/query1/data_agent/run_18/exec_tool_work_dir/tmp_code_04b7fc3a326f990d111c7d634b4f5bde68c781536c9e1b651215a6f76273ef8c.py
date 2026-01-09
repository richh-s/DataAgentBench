code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_records(var_call_uNEWWIgoazl4OEa45raLQHJF)
docs = load_records(var_call_EoYnjBLEIy4e8ssN5tTokANC)

funding_names = set(r['Project_Name'] for r in funding if r.get('Project_Name') is not None)

# Build a big text blob to search for each project name near a 'Design' section
full_text = "\n".join(d.get('text','') for d in docs)

# Heuristic: consider project 'design status' if it appears in a 'Capital Improvement Projects (Design)' section
# or a line like 'Project (Design)' before it.

def is_design_in_docs(name):
    # escape for regex
    n = re.escape(name)
    patterns = [
        rf"Capital Improvement Projects \(Design\)[\s\S]{{0,5000}}\b{n}\b",
        rf"\b{n}\b[\s\S]{{0,200}}\(Design\)",
        rf"\(Design\)[\s\S]{{0,200}}\b{n}\b"
    ]
    for p in patterns:
        if re.search(p, full_text, flags=re.IGNORECASE):
            return True
    return False

count = 0
matched = []
for name in sorted(funding_names):
    if is_design_in_docs(name):
        count += 1
        matched.append(name)

result = {"count": count, "matched_projects": matched}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FzQfpdMuis5pWlSBX6WBYRDU': ['Funding'], 'var_call_LPLFPLfnq4ss3HNzr908cp14': ['civic_docs'], 'var_call_uNEWWIgoazl4OEa45raLQHJF': 'file_storage/call_uNEWWIgoazl4OEa45raLQHJF.json', 'var_call_EoYnjBLEIy4e8ssN5tTokANC': 'file_storage/call_EoYnjBLEIy4e8ssN5tTokANC.json'}

exec(code, env_args)
