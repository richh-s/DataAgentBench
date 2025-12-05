code = """import json, re
from pathlib import Path

path = Path(var_call_nm23grDgsyjqkAjo1EdhoO4i)
data = json.loads(path.read_text())

results = []
for row in data:
    pi = row.get('Patents_info','')
    if 'assignee_harmonized:' in pi:
        m = re.search(r'assignee_harmonized:\s*([^,.;]+)', pi)
        if not m:
            continue
        assignee = m.group(1).strip()
        if assignee == 'UNIV CALIFORNIA':
            continue
        citations = row.get('citation','') or ''
        if 'UNIV CALIFORNIA' not in citations:
            continue
        cpc_raw = row.get('cpc') or '[]'
        try:
            cpc_list = json.loads(cpc_raw)
        except Exception:
            cpc_list = []
        primary = None
        for entry in cpc_list:
            if isinstance(entry, dict) and entry.get('first'):
                primary = entry.get('code')
                break
        if not primary and cpc_list:
            entry = cpc_list[0]
            if isinstance(entry, dict):
                primary = entry.get('code')
        if primary:
            results.append({'assignee': assignee, 'primary_cpc': primary})

# deduplicate
uniq = {}
for r in results:
    key = (r['assignee'], r['primary_cpc'])
    uniq[key] = r

result_list = list(uniq.values())

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_call_nm23grDgsyjqkAjo1EdhoO4i': 'file_storage/call_nm23grDgsyjqkAjo1EdhoO4i.json', 'var_call_lsjOwnI5Azke52dQqxRkp0Jo': []}

exec(code, env_args)
