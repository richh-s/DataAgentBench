code = """import json, re, pandas as pd
from pathlib import Path

# Load civic docs
civic_path = Path(var_call_OpAEF1DppthqRjuyE6pdH84Q)
with civic_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding per project
fund_path = Path(var_call_0gLih5cnNSVVW64UwaxJO1Ug)
with fund_path.open('r', encoding='utf-8') as f:
    fund_rows = json.load(f)

fund_map = {r['Project_Name']: int(r['Total_Amount']) for r in fund_rows if r.get('Project_Name') is not None and r.get('Total_Amount') is not None}

# Extract projects with "Begin Construction" in Spring 2022
proj_to_begin = {}

# Regex patterns
begin_re = re.compile(r"^\s*(?P<name>.+?)\s*$")
season_re = re.compile(r"Begin\s+Construction\s*:\s*(?P<when>[^\n\r]+)", re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # Keep last seen project name when encountering Begin Construction line
    last_project = None
    for i, line in enumerate(lines):
        l = line.strip()
        if not l:
            continue
        # project name lines often stand alone and are not bullet markers
        # Heuristic: line not starting with common prefixes and not containing ':' and not too long
        if ':' not in l and not re.match(r"^(\(cid:|Page\s+\d+|Agenda\s+Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Updates|Project Description)\b", l, re.IGNORECASE):
            if len(l) <= 120:
                last_project = l
        m = season_re.search(line)
        if m and last_project:
            when = m.group('when').strip()
            # normalize punctuation
            when_norm = when.replace(',', ' ').strip()
            # Match Spring 2022
            if re.search(r"\bSpring\b", when_norm, re.IGNORECASE) and re.search(r"\b2022\b", when_norm):
                proj_to_begin[last_project] = when

projects = sorted(proj_to_begin.keys())
count_projects = len(projects)

# Sum funding for those projects that exist in funding map
matched = [p for p in projects if p in fund_map]
total_funding = sum(fund_map[p] for p in matched)

result = {
    "projects_started_spring_2022": count_projects,
    "projects_with_funding_match": len(matched),
    "total_funding_usd": total_funding,
    "projects": projects,
    "unmatched_projects": [p for p in projects if p not in fund_map]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OpAEF1DppthqRjuyE6pdH84Q': 'file_storage/call_OpAEF1DppthqRjuyE6pdH84Q.json', 'var_call_0gLih5cnNSVVW64UwaxJO1Ug': 'file_storage/call_0gLih5cnNSVVW64UwaxJO1Ug.json'}

exec(code, env_args)
