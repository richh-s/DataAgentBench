code = """import json, re

fund_path = var_call_NweUKmP8wRxYGq72jEKdQqDe
with open(fund_path,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_names = set(r['Project_Name'] for r in fund)

cap_design_projects = set()

text_path = var_call_f0QFc0X1u41wMPrD94VOHPxE
with open(text_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

skip_prefix_re = re.compile(r'^(\(cid:|Updates:|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION|Page\s+\d+|Agenda Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)', re.IGNORECASE)
section_end_re = re.compile(r'\n\s*Capital Improvement Projects \((Construction|Not Started)\)', re.IGNORECASE)

for d in docs:
    t = d.get('text','')
    m = re.search(r'Capital Improvement Projects \(Design\)', t, flags=re.IGNORECASE)
    if not m:
        continue
    after = t[m.end():]
    m2 = section_end_re.search(after)
    if m2:
        after = after[:m2.start()]
    for ln in after.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if skip_prefix_re.match(ln):
            continue
        if ':' in ln:
            continue
        if len(ln) < 5 or len(ln) > 120:
            continue
        if re.search(r'\b(Complete Design|Advertise|Begin Construction|Staff|City|Consultant|Plans)\b', ln, flags=re.IGNORECASE):
            continue
        ln_clean = re.sub(r'\s{2,}', ' ', ln).strip(' -\t')
        if ln_clean in fund_names:
            cap_design_projects.add(ln_clean)

result = {"count": len(cap_design_projects), "projects": sorted(cap_design_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ntwr1sXagDFWOkaZDApyDUaL': ['Funding'], 'var_call_08xChGuq85lx0au1CFXtvNA1': ['civic_docs'], 'var_call_NweUKmP8wRxYGq72jEKdQqDe': 'file_storage/call_NweUKmP8wRxYGq72jEKdQqDe.json', 'var_call_f0QFc0X1u41wMPrD94VOHPxE': 'file_storage/call_f0QFc0X1u41wMPrD94VOHPxE.json'}

exec(code, env_args)
