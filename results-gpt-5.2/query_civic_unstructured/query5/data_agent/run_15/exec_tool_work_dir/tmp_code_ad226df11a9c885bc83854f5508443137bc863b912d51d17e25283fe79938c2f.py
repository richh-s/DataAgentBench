code = """import json, re, pandas as pd

# Load funding totals per project
fp = var_call_PPxV9IzyfLu0xdah4vRUKX2g
with open(fp,'r',encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['Total_Amount'] = pd.to_numeric(df_f['Total_Amount'], errors='coerce').fillna(0).astype(int)

# Load civic docs subset
dp = var_call_C7c77UPxzLteMXnoDXddPBny
with open(dp,'r',encoding='utf-8') as f:
    docs = json.load(f)

# Candidate projects: those in funding table with disaster-ish suffix
name_list = df_f['Project_Name'].dropna().unique().tolist()
name_list_sorted = sorted(name_list, key=len, reverse=True)

# Identify disaster-related projects by explicit tags in name OR by appearing under a 'Disaster Recovery Projects' section
# We'll extract a mapping: project -> earliest start-year mention based on nearby schedule lines.
proj_info = {n: {'disaster': False, 'start_2022': False} for n in name_list}

# regex helpers
sched_re = re.compile(r'Project Schedule:|Estimated Schedule:|Schedule:', re.IGNORECASE)
begin_re = re.compile(r'Begin Construction\s*:\s*([^\n\r]+)', re.IGNORECASE)
start_re = re.compile(r'\bStart\b\s*:\s*([^\n\r]+)', re.IGNORECASE)
st_any_re = re.compile(r'\b(Advertise|Final Design|Complete Design|Begin construction|Begin Construction|Construction Start)\s*:\s*([^\n\r]+)', re.IGNORECASE)

def has_2022(s):
    return s is not None and ('2022' in s)

for d in docs:
    text = d.get('text','')
    low = text.lower()
    # Determine if doc includes Disaster Recovery Projects section
    # We'll locate section boundaries roughly by headings
    # Use simple split around 'Disaster Recovery Projects'
    parts = re.split(r'Disaster Recovery Projects', text, flags=re.IGNORECASE)
    disaster_section = None
    if len(parts) > 1:
        # take text after first occurrence up to next big heading 'Capital Improvement Projects' if present
        after = parts[1]
        cut = re.split(r'Capital Improvement Projects', after, flags=re.IGNORECASE)[0]
        disaster_section = cut

    # For each project name that appears, infer disaster status
    for pname in name_list_sorted:
        if pname not in text:
            continue
        # disaster if name contains FEMA/CalOES/CalJPIA or if found within disaster section
        tagged = bool(re.search(r'\((?:FEMA|CalOES|CalJPIA)', pname, flags=re.IGNORECASE)) or bool(re.search(r'\bFEMA\b|\bCalOES\b|\bCalJPIA\b', pname, flags=re.IGNORECASE))
        in_disaster_section = False
        if disaster_section is not None and pname in disaster_section:
            in_disaster_section = True
        if tagged or in_disaster_section:
            proj_info[pname]['disaster'] = True
        # attempt extract schedule lines near occurrence for start in 2022
        idx = text.find(pname)
        window = text[idx: idx+1200]
        # look for begin construction or start lines
        m = begin_re.search(window) or start_re.search(window)
        if m:
            if has_2022(m.group(1)):
                proj_info[pname]['start_2022'] = True
        else:
            # fallback: any schedule field containing 2022 close by
            for mm in st_any_re.finditer(window):
                if has_2022(mm.group(2)):
                    # treat earliest schedule as start-ish; conservative require begin construction/start/advertise in 2022? We'll include advertise as start of project.
                    if mm.group(1).lower() in ['advertise','final design','complete design','construction start','begin construction','begin construction']:
                        proj_info[pname]['start_2022'] = True
                        break

# Build list of disaster projects started 2022
sel = [p for p,info in proj_info.items() if info['disaster'] and info['start_2022']]

# Sum funding
total = int(df_f[df_f['Project_Name'].isin(sel)]['Total_Amount'].sum())

out = {'total_funding': total, 'project_count': len(sel), 'projects': sorted(sel)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Wrm2jsteTKBbvAH00TqFgOdC': ['Funding'], 'var_call_FpdtMAjnEbqq1d0kqNAhcXQO': ['civic_docs'], 'var_call_PPxV9IzyfLu0xdah4vRUKX2g': 'file_storage/call_PPxV9IzyfLu0xdah4vRUKX2g.json', 'var_call_C7c77UPxzLteMXnoDXddPBny': 'file_storage/call_C7c77UPxzLteMXnoDXddPBny.json'}

exec(code, env_args)
