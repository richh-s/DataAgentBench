code = """import json, re, pandas as pd

fp = var_call_PPxV9IzyfLu0xdah4vRUKX2g
with open(fp, 'r', encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['Total_Amount'] = pd.to_numeric(df_f['Total_Amount'], errors='coerce').fillna(0).astype(int)

dp = var_call_C7c77UPxzLteMXnoDXddPBny
with open(dp, 'r', encoding='utf-8') as f:
    docs = json.load(f)

name_list = df_f['Project_Name'].dropna().unique().tolist()
name_list_sorted = sorted(name_list, key=len, reverse=True)

proj_info = {n: {'disaster': False, 'start_2022': False} for n in name_list}

begin_re = re.compile(r'Begin Construction\s*:\s*([^\n\r]+)', re.IGNORECASE)
start_re = re.compile(r'\bStart\b\s*:\s*([^\n\r]+)', re.IGNORECASE)
st_any_re = re.compile(r'\b(Advertise|Final Design|Complete Design|Begin construction|Begin Construction|Construction Start)\s*:\s*([^\n\r]+)', re.IGNORECASE)

def has_2022(s):
    return (s is not None) and ('2022' in s)

for d in docs:
    text = d.get('text', '')
    parts = re.split(r'Disaster Recovery Projects', text, flags=re.IGNORECASE)
    disaster_section = None
    if len(parts) > 1:
        after = parts[1]
        disaster_section = re.split(r'Capital Improvement Projects', after, flags=re.IGNORECASE)[0]

    for pname in name_list_sorted:
        if pname not in text:
            continue
        tagged = bool(re.search(r'\((?:FEMA|CalOES|CalJPIA)', pname, flags=re.IGNORECASE)) or bool(re.search(r'\bFEMA\b|\bCalOES\b|\bCalJPIA\b', pname, flags=re.IGNORECASE))
        in_disaster = (disaster_section is not None) and (pname in disaster_section)
        if tagged or in_disaster:
            proj_info[pname]['disaster'] = True

        idx = text.find(pname)
        window = text[idx: idx + 1200]
        m = begin_re.search(window) or start_re.search(window)
        if m and has_2022(m.group(1)):
            proj_info[pname]['start_2022'] = True
        else:
            for mm in st_any_re.finditer(window):
                if has_2022(mm.group(2)):
                    proj_info[pname]['start_2022'] = True
                    break

sel = [p for p, info in proj_info.items() if info['disaster'] and info['start_2022']]

total = int(df_f[df_f['Project_Name'].isin(sel)]['Total_Amount'].sum())

out = {'total_funding': total, 'project_count': int(len(sel)), 'projects': sorted(sel)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Wrm2jsteTKBbvAH00TqFgOdC': ['Funding'], 'var_call_FpdtMAjnEbqq1d0kqNAhcXQO': ['civic_docs'], 'var_call_PPxV9IzyfLu0xdah4vRUKX2g': 'file_storage/call_PPxV9IzyfLu0xdah4vRUKX2g.json', 'var_call_C7c77UPxzLteMXnoDXddPBny': 'file_storage/call_C7c77UPxzLteMXnoDXddPBny.json'}

exec(code, env_args)
