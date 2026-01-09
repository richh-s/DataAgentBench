code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

funding = load_records(var_call_CaYqFq1nvNpK0x4afuvjnm4O)
docs = load_records(var_call_iOuiPIMZ0ofOEYlt9RLLncwJ)

funding_names = set(r['Project_Name'] for r in funding)

# compile patterns per name (word boundary-ish)
patterns = {name: re.compile(r'(?i)(?<![A-Za-z0-9])' + re.escape(name) + r'(?![A-Za-z0-9])') for name in funding_names}
status_pat = re.compile(r'Capital Improvement Projects\s*\(\s*Design\s*\)|\bDesign\b', re.I)

found_design = set()

for d in docs:
    text = d.get('text','')
    if not status_pat.search(text):
        continue
    # If document has explicit section "Capital Improvement Projects (Design)", assume projects listed there are design.
    # We'll capture projects between that header and next header "Capital Improvement Projects (Construction|Not Started)" or "Disaster".
    m = re.search(r'Capital Improvement Projects\s*\(\s*Design\s*\)(.*?)(Capital Improvement Projects\s*\(|Disaster Recovery Projects|$)', text, flags=re.I|re.S)
    section = m.group(1) if m else text
    # For each funding project name, check presence in section
    for name, pat in patterns.items():
        if name in found_design:
            continue
        if pat.search(section):
            found_design.add(name)

result = {"count": int(len(found_design)), "projects": sorted(found_design)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Yyn4aDzD8lw12o0IVTW3S0s8': ['Funding'], 'var_call_1gQXiHOPYXhuyZMgwNqZSGLc': ['civic_docs'], 'var_call_CaYqFq1nvNpK0x4afuvjnm4O': 'file_storage/call_CaYqFq1nvNpK0x4afuvjnm4O.json', 'var_call_iOuiPIMZ0ofOEYlt9RLLncwJ': 'file_storage/call_iOuiPIMZ0ofOEYlt9RLLncwJ.json'}

exec(code, env_args)
