code = """import json, re
import pandas as pd

# Load large inputs

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

funding_projects = load_json_maybe(var_call_iXindAWuUO4N6yCgMN66Sx2f)
docs = load_json_maybe(var_call_eexuAZ1nkiOzc2nwZAIjCbTK)

proj_names = [r['Project_Name'] for r in funding_projects if r.get('Project_Name')]

# Build regex to find project name as a whole line (common in agendas)
# Escape and sort longest first to prefer specific names.
escaped = sorted({re.escape(p) for p in proj_names}, key=len, reverse=True)
pattern = re.compile(r'(?im)^(?:\s*[-•\u2022\(\[]?\s*)(' + '|'.join(escaped) + r')(?:\s*\)?\s*)$')

# Identify design section blocks then capture subsequent project lines until next section header
section_re = re.compile(r'(?is)Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects|$)')

design_projects_found = set()
for d in docs:
    text = d.get('text','') or ''
    for m in section_re.finditer(text):
        block = m.group(1)
        for pm in pattern.finditer(block):
            design_projects_found.add(pm.group(1).strip())

# Count those with funding > 50000 (already filtered list) intersect design
result_count = sum(1 for p in design_projects_found if p in set(proj_names))

print('__RESULT__:')
print(json.dumps({'count': result_count, 'projects': sorted(design_projects_found)[:50], 'design_projects_total_found': len(design_projects_found)}))"""

env_args = {'var_call_7LgasxdjHDXWpIPZHzIXPOSs': [{'cnt': '276'}], 'var_call_eexuAZ1nkiOzc2nwZAIjCbTK': 'file_storage/call_eexuAZ1nkiOzc2nwZAIjCbTK.json', 'var_call_iXindAWuUO4N6yCgMN66Sx2f': 'file_storage/call_iXindAWuUO4N6yCgMN66Sx2f.json'}

exec(code, env_args)
