code = """import json
import pandas as pd
import re

def load_result(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

funding = load_result(var_call_bOOz23WYBvTWRqo0YznHKIHe)
docs = load_result(var_call_lErE1gjrVmu0A0NLFQ7uSw3P)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype('int64')

pattern_section = re.compile(r"Disaster\s+Recovery\s+Projects(?:\s*\([^\)]*\))?\s*(?:\r?\n)+(?P<body>.*?)(?=\r?\n\s*Capital\s+Improvement\s+Projects|\Z)", re.IGNORECASE|re.DOTALL)
pattern_begin_2022 = re.compile(r"\b(Begin|Start)\b[^\n]*\b2022\b", re.IGNORECASE)

# Very conservative: treat project name as a standalone line followed within next 15 lines by a Begin/Start containing 2022

def extract_projects(text):
    res = set()
    if not text:
        return res
    for m in pattern_section.finditer(text):
        body = m.group('body')
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        for i, ln in enumerate(lines):
            if len(ln) > 120:
                continue
            if ln.endswith(':'):
                continue
            if re.search(r"^(Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION)\b", ln, re.IGNORECASE):
                continue
            if re.search(r"^Page\s+\d+\s+of\s+\d+", ln, re.IGNORECASE):
                continue
            if re.search(r"Agenda Item", ln, re.IGNORECASE):
                continue
            if not re.search(r"[A-Za-z]", ln):
                continue
            if not ln[0].isupper():
                continue
            window = "\n".join(lines[i+1:i+16])
            if pattern_begin_2022.search(window):
                res.add(ln)
    return res

started_2022_projects = set()
for d in docs:
    started_2022_projects |= extract_projects(d.get('text',''))

sel = fund_df[fund_df['Project_Name'].isin(started_2022_projects)]
total = int(sel['total_amount'].sum())

out = {
    'total_funding_usd': total,
    'matched_projects_count': int(sel['Project_Name'].nunique()),
    'matched_projects': sel.sort_values('total_amount', ascending=False)[['Project_Name','total_amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bOOz23WYBvTWRqo0YznHKIHe': 'file_storage/call_bOOz23WYBvTWRqo0YznHKIHe.json', 'var_call_lErE1gjrVmu0A0NLFQ7uSw3P': 'file_storage/call_lErE1gjrVmu0A0NLFQ7uSw3P.json'}

exec(code, env_args)
