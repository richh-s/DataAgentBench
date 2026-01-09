code = """import json, re, pandas as pd

# Load funding per project
path_funding = var_call_xpe1J6bZRj5eub6Cr9CJ7LkJ
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['total_amount'] = pd.to_numeric(df_f['total_amount'], errors='coerce').fillna(0).astype('int64')

# Load docs
path_docs = var_call_bH8yuIz4aLh3wd45vlj4LmLY
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Identify disaster projects and their start strings by parsing lines near project name
funded_projects = set(df_f['Project_Name'].dropna().astype(str))

disaster_started_2022 = set()

def is_disaster_name(name:str):
    n = name.lower()
    return ('fema' in n) or ('caloes' in n) or ('caljpia' in n) or ('disaster' in n) or ('recovery' in n) or ('fire' in n) or ('woolsey' in n)

# regex for extracting schedule fields
st_re = re.compile(r'(?i)\b(?:Start|Begin(?:\s+Construction)?|Start\s+Time|Start\s+Date)\s*:\s*([^\n\r]+)')
proj_line_re = re.compile(r'^\s*([A-Za-z0-9].{2,120}?)\s*$')

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    lines = text.splitlines()
    # scan for any funded project names appearing in this doc
    # Use simple contains to avoid heavy regex; precompute lower text once
    low_text = text.lower()
    candidates = [p for p in funded_projects if p and p.lower() in low_text]
    if not candidates:
        continue
    # map line index occurrences
    low_lines = [ln.lower() for ln in lines]
    for p in candidates:
        pl = p.lower()
        # find all line indices containing project name
        idxs = [i for i,ln in enumerate(low_lines) if pl in ln]
        if not idxs:
            continue
        if not is_disaster_name(p):
            # may still be disaster if doc categorizes it; check nearby for 'Disaster Recovery Projects'
            pass
        for idx in idxs:
            window = "\n".join(lines[idx: min(len(lines), idx+40)])
            m = st_re.search(window)
            if m:
                st = m.group(1).strip()
                if '2022' in st and is_disaster_name(p):
                    disaster_started_2022.add(p)
            else:
                # if no explicit start, attempt infer when schedule lines list 'Begin Construction: ...'
                m2 = re.search(r'(?i)\bBegin\s+Construction\s*:\s*([^\n\r]+)', window)
                if m2:
                    st = m2.group(1).strip()
                    if '2022' in st and is_disaster_name(p):
                        disaster_started_2022.add(p)

# Sum funding for these projects
sum_amt = int(df_f[df_f['Project_Name'].isin(disaster_started_2022)]['total_amount'].sum())

out = {
    "total_funding": sum_amt,
    "num_projects": int(len(disaster_started_2022)),
    "projects": sorted(disaster_started_2022)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xpe1J6bZRj5eub6Cr9CJ7LkJ': 'file_storage/call_xpe1J6bZRj5eub6Cr9CJ7LkJ.json', 'var_call_bH8yuIz4aLh3wd45vlj4LmLY': 'file_storage/call_bH8yuIz4aLh3wd45vlj4LmLY.json', 'var_call_kOBRjFba7uPAiIIvjNbnKFbZ': ['Funding'], 'var_call_giorFytyNRBYlN9KnawCT1yA': ['civic_docs']}

exec(code, env_args)
