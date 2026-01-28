code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_zl52m9mn8D1cMBUR9ENZQ8n5)
fund = load_records(var_call_XVHE2S4YMwyqfgnXLhph61QL)

fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

park_keywords = re.compile(r'\b(park|playground|bluffs|skate)\b', re.I)
completed_2022 = re.compile(r'completed[^\n\r]*2022', re.I)

generic_line = re.compile(r'^(updates|project schedule|capital improvement|agenda|page\s*\d+|to:|prepared by:|subject:|recommended action|discussion)\b', re.I)

projects = set()

for d in docs:
    text = d.get('text', '') or ''
    lines = [ln.strip() for ln in re.split(r'\r?\n', text)]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if len(ln) < 4 or len(ln) > 140:
            continue
        if generic_line.search(ln):
            continue
        if park_keywords.search(ln):
            window = ' '.join(lines[i:i+10])
            if completed_2022.search(window):
                pname = re.sub(r'\s{2,}', ' ', ln).strip().strip(':')
                projects.add(pname)

matched = []
total = 0
for p in sorted(projects):
    amt = fund_map.get(p)
    if amt is not None:
        matched.append({'Project_Name': p, 'Funding': int(amt)})
        total += int(amt)
    else:
        matched.append({'Project_Name': p, 'Funding': None})

out = {
    'total_funding_completed_2022_park_related': int(total),
    'matched_projects_with_funding': matched
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VcSoEbEV11tJzvrjgzmhULMm': ['Funding'], 'var_call_B0V2TRekCl6vrNeq0NVAjjNk': ['civic_docs'], 'var_call_zl52m9mn8D1cMBUR9ENZQ8n5': 'file_storage/call_zl52m9mn8D1cMBUR9ENZQ8n5.json', 'var_call_XVHE2S4YMwyqfgnXLhph61QL': 'file_storage/call_XVHE2S4YMwyqfgnXLhph61QL.json', 'var_call_VLvf98opZ0Mh8hesFIh6m4Oh': {'ok': True}}

exec(code, env_args)
