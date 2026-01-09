code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs_2022 = load_records(var_call_NZJkfTDqLIsk7PFQBeRVaweQ)
fund = load_records(var_call_DzrJsyGi8yVyguqqLp4vcoWd)

park_keywords = re.compile(r'\b(park|playground|bluffs|skate)\b', re.I)

completed_projects = set()
for d in docs_2022:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'Construction was completed', ln, re.I) and '2022' in ln:
            # find nearest preceding non-empty line that looks like a title (often contains Park etc)
            cand = None
            for j in range(i-1, max(-1, i-30), -1):
                b = lines[j]
                if not b:
                    continue
                if re.search(r'^(\(cid:|Updates|Project|Page|Agenda Item|Capital Improvement|Disaster)', b, re.I):
                    continue
                # stop if hit another completion/update block
                if re.search(r'Construction was completed', b, re.I):
                    break
                # project names often have title case and no colon
                if ':' in b:
                    continue
                if len(b) <= 120:
                    cand = b
                    break
            if cand and park_keywords.search(cand):
                completed_projects.add(cand)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
matched = fund_df[fund_df['Project_Name'].isin(completed_projects)].copy()

out = {
    'completed_park_projects_2022': sorted(completed_projects),
    'matched_funding_rows': matched[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records'),
    'total_funding': int(matched['total_amount'].sum())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PF945Zw0JElUWZwT5KGXqZEA': 'file_storage/call_PF945Zw0JElUWZwT5KGXqZEA.json', 'var_call_DzrJsyGi8yVyguqqLp4vcoWd': 'file_storage/call_DzrJsyGi8yVyguqqLp4vcoWd.json', 'var_call_T91ysjF9P7VgpzVdTV1ByLnj': {'total_funding': 0, 'matched_projects': []}, 'var_call_CrcRzhL9q7DiYIrKy3uVxOU9': [], 'var_call_NZJkfTDqLIsk7PFQBeRVaweQ': 'file_storage/call_NZJkfTDqLIsk7PFQBeRVaweQ.json', 'var_call_Cax9yluJNVoPSK6RKDEvS3oN': 'file_storage/call_Cax9yluJNVoPSK6RKDEvS3oN.json', 'var_call_zww0BUzO2UrMING15mJ6npN2': 'file_storage/call_zww0BUzO2UrMING15mJ6npN2.json'}

exec(code, env_args)
