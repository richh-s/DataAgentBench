code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_records(var_call_PF945Zw0JElUWZwT5KGXqZEA)
fund = load_records(var_call_DzrJsyGi8yVyguqqLp4vcoWd)

docs_2022 = [d for d in docs if '2022' in (d.get('filename','') + ' ' + d.get('text',''))]

# Extract completed-in-2022 projects with park-related keywords from 2022 docs.
# Heuristic: In each doc, find lines like "<Project Name>" followed soon by a line containing 'Construction was completed' with '2022'.
park_keywords = re.compile(r'\b(park|playground|bluffs|skate)\b', re.I)
completed_2022 = set()

for d in docs_2022:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'Construction was completed', ln, flags=re.I) and '2022' in ln:
            # look back up to 8 lines for a plausible project name
            back = lines[max(0,i-8):i]
            cand = None
            for b in reversed(back):
                if not b: 
                    continue
                if b.lower().startswith(('updates', 'project schedule', 'estimated schedule', 'project description', 'page', 'agenda item')):
                    continue
                # likely a project name is a relatively short line without punctuation
                if len(b) <= 120 and not re.search(r'[:\u2013\-]{1,}', b) and not re.search(r'\b(cid|page)\b', b, re.I):
                    cand = b
                    break
            if cand and park_keywords.search(cand):
                completed_2022.add(cand)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

matched = fund_df[fund_df['Project_Name'].isin(completed_2022)]

total = int(matched['total_amount'].sum())

out = {
    'total_funding': total,
    'matched_projects': matched[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PF945Zw0JElUWZwT5KGXqZEA': 'file_storage/call_PF945Zw0JElUWZwT5KGXqZEA.json', 'var_call_DzrJsyGi8yVyguqqLp4vcoWd': 'file_storage/call_DzrJsyGi8yVyguqqLp4vcoWd.json'}

exec(code, env_args)
