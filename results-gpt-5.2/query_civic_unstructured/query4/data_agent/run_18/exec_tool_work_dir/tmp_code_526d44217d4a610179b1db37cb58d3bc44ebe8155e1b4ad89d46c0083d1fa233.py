code = """import json, re, pandas as pd

def load_mongo_docs(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

docs = load_mongo_docs(var_call_0f7yDI4ecmLKSKpoaVFu2vZD)
fund = var_call_27VpEJXZf7UZvZlIuZtK2xrL
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# parse project blocks and extract schedule lines
spring2022_projects = set()

# patterns for start schedule
spring22_pat = re.compile(r"\b(Spring\s*2022|2022\s*-\s*Spring|2022\s*Spring)\b", re.IGNORECASE)
# project title line: non-empty, not bullet label
bad_starts = re.compile(r"^(\(cid:|Page\s+\d+\s+of\s+\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Estimated Schedule|Updates:|Project Updates:|Project Description:|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)$", re.IGNORECASE)

for d in docs:
    text = d.get('text','')
    # normalize line endings
    lines = [ln.strip() for ln in text.splitlines()]
    n = len(lines)
    for i, ln in enumerate(lines):
        if spring22_pat.search(ln):
            # ensure this is a start/begin/advertise line
            if re.search(r"\b(Begin|Start|Advertise)\b", ln, re.IGNORECASE):
                # look back for nearest plausible project name line
                j = i-1
                name = None
                while j >= 0 and i-j <= 25:
                    cand = lines[j].strip()
                    if not cand:
                        j -= 1
                        continue
                    if bad_starts.search(cand):
                        j -= 1
                        continue
                    # avoid schedule labels
                    if re.search(r"\b(Complete|Begin|Advertise|Final Design|Preliminary design|Estimated Schedule|Project Schedule|Updates)\b", cand, re.IGNORECASE):
                        j -= 1
                        continue
                    # candidate should not end with ':'
                    if cand.endswith(':'):
                        j -= 1
                        continue
                    # likely project title: mostly words, maybe ampersand
                    if len(cand) >= 4 and len(cand) <= 120:
                        name = cand
                        break
                    j -= 1
                if name:
                    spring2022_projects.add(name)

# compute funding totals for matched names
matched = []
missing = []
total = 0
for p in sorted(spring2022_projects):
    amt = fund_map.get(p)
    if amt is None:
        missing.append(p)
    else:
        matched.append({'Project_Name': p, 'Funding': amt})
        total += amt

result = {
    'spring_2022_project_count': len(spring2022_projects),
    'spring_2022_total_funding_matched': int(total),
    'matched_project_count': len(matched),
    'missing_funding_project_count': len(missing),
    'missing_projects_sample': missing[:20]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0f7yDI4ecmLKSKpoaVFu2vZD': 'file_storage/call_0f7yDI4ecmLKSKpoaVFu2vZD.json', 'var_call_27VpEJXZf7UZvZlIuZtK2xrL': 'file_storage/call_27VpEJXZf7UZvZlIuZtK2xrL.json'}

exec(code, env_args)
