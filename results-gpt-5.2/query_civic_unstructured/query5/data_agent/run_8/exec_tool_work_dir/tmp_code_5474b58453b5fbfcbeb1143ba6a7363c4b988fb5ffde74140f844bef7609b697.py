code = """import json, re
import pandas as pd

def load_result(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

funding = load_result(var_call_bOOz23WYBvTWRqo0YznHKIHe)
docs = load_result(var_call_lErE1gjrVmu0A0NLFQ7uSw3P)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype('int64')

# Determine disaster-related projects that started in 2022 using heuristics:
# 1) Project name appears in a "Disaster Recovery Projects" section
# 2) Within its block, a line like "Begin" or "Start" contains year 2022

def extract_disaster_projects_started_2022(text):
    results = []
    if not text:
        return results
    for m in re.finditer(r"Disaster\s+Recovery\s+Projects(?:\s*\([^\)]*\))?\s*(?:\r?\n)+(?P<body>.*?)(?=\r?\n\s*Capital\s+Improvement\s+Projects|\Z)", text, flags=re.IGNORECASE|re.DOTALL):
        body = m.group('body')
        lines = [ln.strip() for ln in body.splitlines()]
        current_name = None
        current_block = []
        def flush():
            nonlocal current_name, current_block
            if current_name is None:
                return
            block_text = "\n".join(current_block)
            started_2022 = False
            for ln in current_block:
                if re.search(r"\b(Begin|Start)\b[^\n]*\b2022\b", ln, flags=re.IGNORECASE):
                    started_2022 = True
                    break
            if not started_2022:
                if re.search(r"Begin\s+Construction\s*:\s*[^\n]*2022", block_text, flags=re.IGNORECASE):
                    started_2022 = True
                elif re.search(r"Start\s*:\s*[^\n]*2022", block_text, flags=re.IGNORECASE):
                    started_2022 = True
            if started_2022:
                results.append(current_name)
            current_name = None
            current_block = []
        
        for ln in lines:
            if not ln:
                continue
            if re.match(r"^(Design|Construction|Not Started)\b", ln, flags=re.IGNORECASE):
                continue
            if re.search(r"^Page\s+\d+\s+of\s+\d+", ln, flags=re.IGNORECASE):
                continue
            if re.search(r"Agenda Item", ln, flags=re.IGNORECASE):
                continue
            if re.search(r"^(Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION)\b", ln, flags=re.IGNORECASE):
                continue
            if ln.endswith(':'):
                continue
            if (not re.match(r"^[\(\[\u2022\*\-\u2013\u2014]|^\(cid", ln) and re.search(r"[A-Za-z]", ln) and len(ln) <= 120 and ln[0].isupper()):
                # new project title
                flush()
                current_name = ln
                current_block = []
                continue
            if current_name is not None:
                current_block.append(ln)
        flush()
    return results

started_2022_projects = set()
for d in docs:
    started_2022_projects.update(extract_disaster_projects_started_2022(d.get('text','')))

# Join funding
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
