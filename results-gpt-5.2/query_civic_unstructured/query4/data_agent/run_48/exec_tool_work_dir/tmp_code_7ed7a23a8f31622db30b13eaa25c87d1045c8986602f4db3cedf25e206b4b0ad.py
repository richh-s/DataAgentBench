code = """import json, re
from pathlib import Path

civic_path = Path(var_call_OpAEF1DppthqRjuyE6pdH84Q)
with civic_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)

fund_path = Path(var_call_0gLih5cnNSVVW64UwaxJO1Ug)
with fund_path.open('r', encoding='utf-8') as f:
    fund_rows = json.load(f)

fund_map = {r.get('Project_Name'): int(r.get('Total_Amount')) for r in fund_rows if r.get('Project_Name') is not None and r.get('Total_Amount') is not None}

season_re = re.compile(r"Begin\s+Construction\s*:\s*(?P<when>[^\n\r]+)", re.IGNORECASE)
ignore_prefix = re.compile(r"^(\(cid:|Page\s+\d+|Agenda\s+Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Updates|Project Description)", re.IGNORECASE)

proj_to_when = {}
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    last_project = None
    for line in lines:
        l = line.strip()
        if not l:
            continue
        if (':' not in l) and (not ignore_prefix.match(l)) and (len(l) <= 120):
            last_project = l
        m = season_re.search(line)
        if m and last_project:
            when = m.group('when').strip()
            if re.search(r"\bSpring\b", when, re.IGNORECASE) and re.search(r"\b2022\b", when):
                proj_to_when[last_project] = when

projects = sorted(proj_to_when.keys())
matched = [p for p in projects if p in fund_map]

out = {
    "count_projects": len(projects),
    "total_funding_usd": sum(fund_map[p] for p in matched),
    "projects": projects
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OpAEF1DppthqRjuyE6pdH84Q': 'file_storage/call_OpAEF1DppthqRjuyE6pdH84Q.json', 'var_call_0gLih5cnNSVVW64UwaxJO1Ug': 'file_storage/call_0gLih5cnNSVVW64UwaxJO1Ug.json'}

exec(code, env_args)
