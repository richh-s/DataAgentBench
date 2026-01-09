code = """import json, re
import pandas as pd

# Load civic docs
path_docs = var_call_K0diklJrRpOPLUMHrtUNxDcF
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding > 50k
path_fund = var_call_tZl3OtNVfLtmXP8FKDzWqUQ1
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

fund_names = set([r['Project_Name'] for r in fund if r.get('Project_Name')])

# Heuristic: identify project names listed under section "Capital Improvement Projects (Design)"
# We'll scan each doc for that header and collect subsequent non-empty lines until next header starts.
header_pat = re.compile(r'^Capital Improvement Projects\s*\(Design\)\s*$', re.IGNORECASE)
stop_pat = re.compile(r'^Capital Improvement Projects\s*\((Construction|Not Started)\)\s*$', re.IGNORECASE)
other_stop_pat = re.compile(r'^(Disaster Recovery Projects|RECOMMENDED ACTION|DISCUSSION)\b', re.IGNORECASE)

capital_design_projects = set()

for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    i = 0
    while i < len(lines):
        if header_pat.match(lines[i]):
            i += 1
            # collect until stop
            while i < len(lines):
                ln = lines[i].strip()
                if not ln:
                    i += 1
                    continue
                if stop_pat.match(ln) or other_stop_pat.match(ln):
                    break
                # Exclude bullets/updates/schedule labels and page markers
                if re.match(r'^(\(cid:|Page\s+\d+\s+of\s+\d+|Agenda Item|Project Schedule|Estimated Schedule|Updates:|Project Description:|\uf0be|\uf0b7|\u2022)', ln, re.IGNORECASE):
                    i += 1
                    continue
                # likely a project name line: no colon, not too long
                if ':' not in ln and len(ln) <= 120:
                    capital_design_projects.add(ln)
                i += 1
        else:
            i += 1

# Count those that have funding > 50k
count = sum(1 for p in capital_design_projects if p in fund_names)

out = {
    "count": int(count),
    "matched_projects_sample": sorted([p for p in capital_design_projects if p in fund_names])[:25],
    "total_extracted_capital_design_projects": int(len(capital_design_projects))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vAd4mk5lt2ewS0WUG9mhIAGw': [{'cnt': '276'}], 'var_call_K0diklJrRpOPLUMHrtUNxDcF': 'file_storage/call_K0diklJrRpOPLUMHrtUNxDcF.json', 'var_call_tZl3OtNVfLtmXP8FKDzWqUQ1': 'file_storage/call_tZl3OtNVfLtmXP8FKDzWqUQ1.json'}

exec(code, env_args)
