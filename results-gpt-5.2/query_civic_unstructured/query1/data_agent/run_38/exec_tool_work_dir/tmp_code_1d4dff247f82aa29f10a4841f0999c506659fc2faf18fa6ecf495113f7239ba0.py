code = """import json, re, pandas as pd

# load funding projects > 50000
fund_path = var_call_NweUKmP8wRxYGq72jEKdQqDe
with open(fund_path,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_names = set(r['Project_Name'] for r in fund)

# regex to find capital design projects block and extract candidate project lines
cap_design_projects = set()

text_path = var_call_f0QFc0X1u41wMPrD94VOHPxE
with open(text_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

for d in docs:
    t = d.get('text','')
    # find section start
    m = re.search(r'Capital Improvement Projects \(Design\)', t, flags=re.IGNORECASE)
    if not m:
        continue
    after = t[m.end():]
    # cut off at next section header
    m2 = re.search(r'\n\s*Capital Improvement Projects \((Construction|Not Started)\)', after, flags=re.IGNORECASE)
    if m2:
        after = after[:m2.start()]
    lines = [ln.strip() for ln in after.splitlines()]
    for ln in lines:
        if not ln: 
            continue
        # skip bullets/labels
        if re.match(r'^(\(cid:|Updates:|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION|Page\s+\d+|Agenda Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)', ln, flags=re.IGNORECASE):
            continue
        # project names often appear as standalone line without punctuation
        # exclude lines with colon
        if ':' in ln:
            continue
        # exclude obvious non-project sentences
        if len(ln) < 5 or len(ln) > 120:
            continue
        if re.search(r'\b(Complete Design|Advertise|Begin Construction|Staff|City|Consultant|Plans)\b', ln, flags=re.IGNORECASE):
            continue
        # remove trailing weird characters
        ln_clean = re.sub(r'\s{2,}', ' ', ln).strip(' -\t')
        # keep if matches a funded project name
        if ln_clean in fund_names:
            cap_design_projects.add(ln_clean)

count = len(cap_design_projects)
result = {
    "count": count,
    "projects": sorted(cap_design_projects)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ntwr1sXagDFWOkaZDApyDUaL': ['Funding'], 'var_call_08xChGuq85lx0au1CFXtvNA1': ['civic_docs'], 'var_call_NweUKmP8wRxYGq72jEKdQqDe': 'file_storage/call_NweUKmP8wRxYGq72jEKdQqDe.json', 'var_call_f0QFc0X1u41wMPrD94VOHPxE': 'file_storage/call_f0QFc0X1u41wMPrD94VOHPxE.json'}

exec(code, env_args)
