code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_0f7yDI4ecmLKSKpoaVFu2vZD)
fund = load_json_maybe(var_call_27VpEJXZf7UZvZlIuZtK2xrL)

if not isinstance(fund, list):
    fund = []

fund_df = pd.DataFrame.from_records(fund)
if fund_df.empty:
    fund_df = pd.DataFrame(columns=['Project_Name','total_amount'])

fund_df['total_amount'] = pd.to_numeric(fund_df.get('total_amount'), errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

spring2022_projects = set()

spring22_pat = re.compile(r"\b(Spring\s*2022|2022\s*-\s*Spring|2022\s*Spring)\b", re.IGNORECASE)
bad_starts = re.compile(r"^(\(cid:|Page\s+\d+\s+of\s+\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Estimated Schedule|Updates:|Project Updates:|Project Description:|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)$", re.IGNORECASE)

for d in docs:
    text = d.get('text','') if isinstance(d, dict) else ''
    lines = [ln.strip() for ln in str(text).splitlines()]
    for i, ln in enumerate(lines):
        if spring22_pat.search(ln) and re.search(r"\b(Begin|Start|Advertise)\b", ln, re.IGNORECASE):
            name = None
            j = i-1
            while j >= 0 and i-j <= 25:
                cand = lines[j].strip()
                if not cand:
                    j -= 1
                    continue
                if bad_starts.search(cand):
                    j -= 1
                    continue
                if re.search(r"\b(Complete|Begin|Advertise|Final Design|Preliminary design|Estimated Schedule|Project Schedule|Updates)\b", cand, re.IGNORECASE):
                    j -= 1
                    continue
                if cand.endswith(':'):
                    j -= 1
                    continue
                if 4 <= len(cand) <= 120:
                    name = cand
                    break
                j -= 1
            if name:
                spring2022_projects.add(name)

matched = []
missing = []
total = 0
for p in sorted(spring2022_projects):
    if p in fund_map:
        amt = int(fund_map[p])
        matched.append({'Project_Name': p, 'Funding': amt})
        total += amt
    else:
        missing.append(p)

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
