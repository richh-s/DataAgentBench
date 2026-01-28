code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_ZxUhaAI37K4GBm8xBBT0DT9b)
fund = load_json_maybe(var_call_ijXcqP4PgqQoWbsuEISz7Brt)

# Extract (project_name, completion_line) pairs where completion_line contains 2022
pairs = []
for d in docs:
    lines = [ln.strip() for ln in (d.get('text','') or '').splitlines()]
    current = None
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # project name candidate: line followed soon by 'Updates' or 'Project Description'
        if len(ln) <= 100 and not re.search(r'\bUpdates\b|\bProject\s+Schedule\b|\bEstimated\s+Schedule\b', ln, flags=re.I) and ':' not in ln:
            # lookahead
            look = ' '.join(lines[i+1:i+6]).lower()
            if ('updates' in look) or ('project description' in look) or ('project schedule' in look) or ('estimated schedule' in look):
                # exclude obvious headers
                if not re.match(r'^(capital improvement projects|disaster recovery projects|public works|agenda|recommended action|discussion)\b', ln, flags=re.I):
                    current = ln
        if current and re.search(r'\bcompleted\b', ln, flags=re.I) and '2022' in ln:
            pairs.append((current, ln))

# Determine park-related by presence of park/playground/skate in project name
park_projects = {p for p, ln in pairs if re.search(r'\b(park|playground|skate)\b', p, flags=re.I)}

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

matched = fund_df[fund_df['Project_Name'].isin(sorted(park_projects))]

total = int(matched['total_amount'].sum())

out = {
    'identified_completed_2022_lines': [{'Project_Name':p,'completion_line':ln} for p,ln in pairs],
    'park_related_completed_2022_projects': sorted(park_projects),
    'matched_funding_rows': matched.to_dict(orient='records'),
    'total_funding_usd': total
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UofbwvMTW9eL8ESjJ7gV8qC2': ['Funding'], 'var_call_BTYCgoMO7sRs5ron6p1T0tv6': ['civic_docs'], 'var_call_Bj4yPTTHhPADOYlzfQxBnD8h': 'file_storage/call_Bj4yPTTHhPADOYlzfQxBnD8h.json', 'var_call_ijXcqP4PgqQoWbsuEISz7Brt': 'file_storage/call_ijXcqP4PgqQoWbsuEISz7Brt.json', 'var_call_NyHUPX899qUjNuhaOSB6OKnM': {'park_related_completed_2022_projects': [], 'total_funding_usd': 0}, 'var_call_ZxUhaAI37K4GBm8xBBT0DT9b': 'file_storage/call_ZxUhaAI37K4GBm8xBBT0DT9b.json'}

exec(code, env_args)
