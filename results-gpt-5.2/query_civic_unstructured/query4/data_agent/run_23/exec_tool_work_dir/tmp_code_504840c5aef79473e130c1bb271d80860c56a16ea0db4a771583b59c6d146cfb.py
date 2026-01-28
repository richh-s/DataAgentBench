code = """import json, re, pandas as pd

path_docs = var_call_ktn2NXP67hv32AVFGAlEMGmp
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_fund = var_call_QPGkwQMFhoAS3XLLfcXdXfAi
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

projects = []
sched_line_re = re.compile(r'^(?:\s*\(cid:131\)\s*)?(Complete Design|Final Design|Advertise|Begin Construction|Complete Construction)\s*:\s*(.+?)\s*$')

for d in docs:
    text = d.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    i = 0
    while i < len(lines):
        ln = lines[i].strip()
        if ln and len(ln) <= 120 and (not ln.endswith(':')):
            window = '\\n'.join(lines[i:i+25])
            if ('Updates' in window) and (('Project Schedule' in window) or ('Estimated Schedule' in window)):
                pname = ln
                st = None
                in_sched = False
                for k in range(i, min(i+60, len(lines))):
                    lnk = lines[k].strip()
                    if ('Project Schedule' in lnk) or ('Estimated Schedule' in lnk):
                        in_sched = True
                        continue
                    if in_sched:
                        m = sched_line_re.match(lnk)
                        if m:
                            label, val = m.group(1), m.group(2)
                            if label == 'Begin Construction':
                                st = val
                                break
                projects.append({'Project_Name': pname, 'st': st})
        i += 1

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

def is_spring_2022(s):
    if not isinstance(s, str) or not s.strip():
        return False
    t = s.strip().lower().replace(',', ' ')
    if ('spring' in t) and ('2022' in t):
        return True
    if ('2022' in t) and any(m in t for m in ['march','april','may']):
        return True
    if re.search(r'2022\s*[-/]\s*0?3\b', t) or re.search(r'2022\s*[-/]\s*0?4\b', t) or re.search(r'2022\s*[-/]\s*0?5\b', t):
        return True
    if re.search(r'\b0?3\s*[-/]\s*2022\b', t) or re.search(r'\b0?4\s*[-/]\s*2022\b', t) or re.search(r'\b0?5\s*[-/]\s*2022\b', t):
        return True
    return False

spring_df = proj_df[proj_df['st'].apply(is_spring_2022)].copy()
spring_df['Total_Funding'] = spring_df['Project_Name'].map(fund_map).fillna(0).astype(int)

out = {
    'projects_started_spring_2022': int(spring_df.shape[0]),
    'total_funding': int(spring_df['Total_Funding'].sum())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CxHqyMELXWVY83oXrfOfhBAQ': ['Funding'], 'var_call_ktn2NXP67hv32AVFGAlEMGmp': 'file_storage/call_ktn2NXP67hv32AVFGAlEMGmp.json', 'var_call_QPGkwQMFhoAS3XLLfcXdXfAi': 'file_storage/call_QPGkwQMFhoAS3XLLfcXdXfAi.json'}

exec(code, env_args)
