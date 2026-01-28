code = """import json, re
import pandas as pd

# Load civic docs
civic_src = var_call_J7eGwEXhjIzwwKUfPFoudyfW
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding totals > 50k
fund_src = var_call_XdOjpbUIRZETuOjgdLVI09nb
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src

fund_projects = set(r['Project_Name'] for r in fund_rows)

# Extract project names listed under 'Capital Improvement Projects (Design)'
capital_design = set()
pattern_header = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text','') or ''
    for m in pattern_header.finditer(text):
        start = m.end()
        window = text[start:start+6000]
        # stop at next section header
        stop_match = re.search(r"\n\s*Capital Improvement Projects\s*\(Construction\)|\n\s*Disaster Recovery Projects|\n\s*Capital Improvement Projects\s*\(Not Started\)", window, flags=re.IGNORECASE)
        if stop_match:
            window = window[:stop_match.start()]
        # Candidate lines: non-empty lines, not bullet/updates/schedule/page etc.
        for line in window.splitlines():
            s = line.strip()
            if not s:
                continue
            if len(s) < 4:
                continue
            # skip obvious non-project lines
            if re.match(r"^(\(cid:|Updates\b|Project Schedule\b|Estimated Schedule\b|Complete Design\b|Advertise\b|Begin Construction\b|Final Design\b|Page\b|Agenda Item\b|DISCUSSION\b|RECOMMENDED ACTION\b)", s, flags=re.IGNORECASE):
                continue
            # remove trailing punctuation
            s2 = re.sub(r"\s{2,}", " ", s).strip(' -:\t')
            # heuristic: project names are Title Case-ish and not too long
            if len(s2) > 120:
                continue
            # avoid sentences (contain period) 
            if '.' in s2:
                continue
            capital_design.add(s2)

# intersect with funded projects > 50k
result_set = sorted(capital_design.intersection(fund_projects))
answer = str(len(result_set))

print("__RESULT__:")
print(json.dumps({"count": len(result_set), "projects_sample": result_set[:20]}))"""

env_args = {'var_call_LOtBju6RNpgkJofPvIFclz34': [{'project_count': '276'}], 'var_call_J7eGwEXhjIzwwKUfPFoudyfW': 'file_storage/call_J7eGwEXhjIzwwKUfPFoudyfW.json', 'var_call_XdOjpbUIRZETuOjgdLVI09nb': 'file_storage/call_XdOjpbUIRZETuOjgdLVI09nb.json'}

exec(code, env_args)
