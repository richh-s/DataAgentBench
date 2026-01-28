code = """import json, pandas as pd, re

# load funding per project
path_f = var_call_EddKUdtrHfUENIuRSVP6kHw6
with open(path_f, 'r', encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['total_amount'] = pd.to_numeric(df_f['total_amount'])

# load civic docs
path_docs = var_call_hzyk155rCtz87y8Vrbq5qY0i
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

project_years = {}  # name -> set(years)

year_re = re.compile(r'\b(20\d{2})\b')

for d in docs:
    text = d.get('text','')
    # find any start indicators followed by year/season/month; keep same line capture
    # capture lines like: Begin Construction: Fall 2023 OR Start: 2022-Spring
    for line in text.splitlines():
        if re.search(r'\b(Begin Construction|Begin construction|Start|Start Date|Project Schedule|Estimated Schedule)\b', line):
            continue
    # extract project blocks: assume project name is a standalone line (no colon) followed later by schedule lines.
    lines = [ln.strip() for ln in text.splitlines()]
    # identify candidate project names: lines that match funding project names exactly
    # build a lookup set for fast containment

lookup = set(df_f['Project_Name'].dropna().tolist())

# process each doc by scanning for each project name and nearby schedule lines
for d in docs:
    text = d.get('text','')
    for pname in lookup:
        if pname in text:
            # for each occurrence, take a window around it
            for m in re.finditer(re.escape(pname), text):
                start = max(0, m.start()-500)
                end = min(len(text), m.end()+800)
                window = text[start:end]
                # infer disaster by FEMA/CalOES/Disaster Recovery keywords in name or window
                is_disaster = bool(re.search(r'\b(Disaster Recovery|FEMA|CalOES|Woolsey|CalJPIA)\b', pname, re.IGNORECASE) or 
                                  re.search(r'\b(Disaster Recovery|FEMA|CalOES|Woolsey|CalJPIA)\b', window, re.IGNORECASE))
                if not is_disaster:
                    continue
                # find start date/year cues in window
                # prioritize 'Begin Construction' lines; else any 'Begin' or 'Start'
                years = set()
                for ln in window.splitlines():
                    if re.search(r'\b(Begin Construction|Begin construction|Start)\b', ln):
                        yrs = year_re.findall(ln)
                        for y in yrs:
                            years.add(int(y))
                # fallback: if none found, look for patterns like 'Begin Construction: Fall 2023' in window regardless of line
                if not years:
                    for y in year_re.findall(window):
                        # too broad; only keep if near 'Begin Construction' within 40 chars
                        for mm in re.finditer(y, window):
                            seg = window[max(0, mm.start()-40):mm.end()+40]
                            if re.search(r'\b(Begin Construction|Begin construction|Start)\b', seg):
                                years.add(int(y))
                if years:
                    project_years.setdefault(pname, set()).update(years)

# projects disaster-related that started in 2022
started_2022 = [p for p, yrs in project_years.items() if 2022 in yrs]

df_sel = df_f[df_f['Project_Name'].isin(started_2022)].copy()

total = int(df_sel['total_amount'].sum())

out = {
    "total_funding_disaster_projects_started_2022": total,
    "num_projects": int(df_sel.shape[0]),
    "projects": df_sel.sort_values('total_amount', ascending=False).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EddKUdtrHfUENIuRSVP6kHw6': 'file_storage/call_EddKUdtrHfUENIuRSVP6kHw6.json', 'var_call_hzyk155rCtz87y8Vrbq5qY0i': 'file_storage/call_hzyk155rCtz87y8Vrbq5qY0i.json'}

exec(code, env_args)
