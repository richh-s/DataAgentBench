code = """import json, re
import pandas as pd

funding_src = var_call_hcV4HbAFR0UjYoXl3PBfZSLI
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_src

docs_src = var_call_q77aXuRGuNAWf5iuF5j9W3jC
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r') as f:
        docs = json.load(f)
else:
    docs = docs_src

proj_started_2022 = set()

for d in docs:
    text = d.get('text','')
    m = re.search(r"Disaster Recovery Projects(?:\s*\([^\)]*\))?\s*(.*)", text, flags=re.I|re.S)
    if not m:
        continue
    after = m.group(1)
    stop = re.search(r"\n\s*Capital Improvement Projects\b", after, flags=re.I)
    if stop:
        after = after[:stop.start()]

    lines = [ln.strip() for ln in after.splitlines()]

    current_proj = None
    buffer = []

    def flush(proj, buf):
        if not proj:
            return
        block = "\n".join(buf)
        if re.search(r"Begin\s+Construction\s*:\s*[^\n]*2022", block, flags=re.I) or re.search(r"\bStart\b\s*:\s*[^\n]*2022", block, flags=re.I):
            proj_started_2022.add(proj)

    for ln in lines:
        if not ln:
            continue
        if (':' not in ln) and (not ln.startswith(('•','(cid','-'))):
            if re.match(r"^(Updates?|Project (Schedule|Description|Updates?)|Estimated Schedule|Page \\d+ of \\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION)\\b", ln, flags=re.I):
                continue
            if re.search(r"[A-Za-z]", ln) and len(ln) <= 120:
                flush(current_proj, buffer)
                current_proj = ln
                buffer = []
                continue
        if current_proj:
            buffer.append(ln)
    flush(current_proj, buffer)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
sel = fund_df[fund_df['Project_Name'].isin(sorted(proj_started_2022))]
answer_val = int(sel['total_amount'].sum())

out = {
    'total_funding': answer_val,
    'project_count': int(len(proj_started_2022)),
    'projects_matched_in_funding': int(sel['Project_Name'].nunique()),
    'projects_unmatched': sorted(list(proj_started_2022 - set(sel['Project_Name'])))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hcV4HbAFR0UjYoXl3PBfZSLI': 'file_storage/call_hcV4HbAFR0UjYoXl3PBfZSLI.json', 'var_call_q77aXuRGuNAWf5iuF5j9W3jC': 'file_storage/call_q77aXuRGuNAWf5iuF5j9W3jC.json'}

exec(code, env_args)
