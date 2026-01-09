code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_0f7yDI4ecmLKSKpoaVFu2vZD)
fund = load_json_maybe(var_call_27VpEJXZf7UZvZlIuZtK2xrL)
fund_df = pd.DataFrame.from_records(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

spring2022_projects=set()

spring22_pat = re.compile(r"\bSpring\s*[,\-]?\s*2022\b", re.IGNORECASE)

bad = re.compile(r"^(\(cid:|Page\s+\d+\s+of\s+\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Estimated Schedule|Updates:|Project Updates:|Project Description:|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)$", re.IGNORECASE)

for d in docs:
    text=str(d.get('text',''))
    lines=[ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if spring22_pat.search(ln) and re.search(r"\b(Begin|Start)\b", ln, re.IGNORECASE):
            name=None
            j=i-1
            while j>=0 and i-j<=30:
                cand=lines[j].strip()
                if not cand:
                    j-=1; continue
                if bad.search(cand):
                    j-=1; continue
                if re.search(r"\b(Complete|Begin|Advertise|Final Design|Estimated Schedule|Project Schedule|Updates)\b", cand, re.IGNORECASE):
                    j-=1; continue
                if cand.endswith(':'):
                    j-=1; continue
                name=cand
                break
            if name:
                spring2022_projects.add(name)

matched=[]
missing=[]
total=0
for p in sorted(spring2022_projects):
    if p in fund_map:
        amt=int(fund_map[p]); total+=amt
        matched.append({'Project_Name':p,'Funding':amt})
    else:
        missing.append(p)

print('__RESULT__:')
print(json.dumps({
    'projects_started_spring_2022': sorted(spring2022_projects),
    'project_count': len(spring2022_projects),
    'total_funding_matched': int(total),
    'matched_count': len(matched),
    'missing_count': len(missing),
    'missing_projects': missing
}))"""

env_args = {'var_call_0f7yDI4ecmLKSKpoaVFu2vZD': 'file_storage/call_0f7yDI4ecmLKSKpoaVFu2vZD.json', 'var_call_27VpEJXZf7UZvZlIuZtK2xrL': 'file_storage/call_27VpEJXZf7UZvZlIuZtK2xrL.json', 'var_call_WYLUmmwObGXwduLEEijbEoV5': {'spring_2022_project_count': 0, 'spring_2022_total_funding_matched': 0, 'matched_project_count': 0, 'missing_funding_project_count': 0, 'missing_projects_sample': []}, 'var_call_XLDXr8FDGIphVyw4C4Q3qfWR': {'line_hits': 0, 'samples': []}, 'var_call_i92AmPWPnkGbKjl9Z3o4vfog': {'docs_with_spring2022': 4, 'samples': [' Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'dian Improvement\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Constructio']}}

exec(code, env_args)
