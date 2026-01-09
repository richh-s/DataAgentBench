code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_ktn2NXP67hv32AVFGAlEMGmp
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding totals by project
path_fund = var_call_QPGkwQMFhoAS3XLLfcXdXfAi
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)

fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

# Extract project names and schedules from docs using a heuristic parser tailored to agenda format
projects = []

sched_line_re = re.compile(r'^(?:\s*\(cid:131\)\s*)?(Complete Design|Final Design|Advertise|Begin Construction|Complete Construction)\s*:\s*(.+?)\s*$')

for d in docs:
    text = d.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    i = 0
    while i < len(lines):
        ln = lines[i].strip()
        # Identify a plausible project heading line: non-empty, not bullet label, not section header, title-like
        # We'll treat a line as project name if next few lines contain 'Updates:' and 'Project Schedule'/'Estimated Schedule'
        if ln and len(ln) <= 120 and not ln.endswith(':') and ln.lower() not in {'updates','project schedule','estimated schedule','project description'}:
            # lookahead window
            window = '\n'.join(lines[i:i+25])
            if ('Updates' in window) and ('Project Schedule' in window or 'Estimated Schedule' in window):
                pname = ln
                st = None
                # scan following lines until blank line after schedule block or next heading
                j = i
                in_sched = False
                for k in range(i, min(i+60, len(lines))):
                    lnk = lines[k].strip()
                    if 'Project Schedule' in lnk or 'Estimated Schedule' in lnk:
                        in_sched = True
                        continue
                    if in_sched:
                        m = sched_line_re.match(lnk)
                        if m:
                            label, val = m.group(1), m.group(2)
                            if label == 'Begin Construction':
                                st = val
                                break
                    # end schedule if encounter another project-like heading and already saw schedule
                    if in_sched and lnk and len(lnk) <= 120 and not lnk.endswith(':') and ('Updates' in '\n'.join(lines[k:k+10])) and k != i:
                        break
                projects.append({'Project_Name': pname, 'st': st})
                i += 1
                continue
        i += 1

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

# Determine projects started in Spring 2022
# Spring: March-May 2022; accept formats like 'Spring 2022', 'Spring, 2022', '2022-Spring', 'March 2022', 'May 2022', '2022-03', '2022-04', '2022-05'

def is_spring_2022(s):
    if not isinstance(s, str) or not s.strip():
        return False
    t = s.strip().lower()
    # normalize commas
    t = t.replace(',', ' ')
    # spring keyword
    if 'spring' in t and '2022' in t:
        return True
    # month words
    if '2022' in t and any(m in t for m in ['march', 'april', 'may']):
        return True
    # numeric months
    # look for 2022-03 etc
    if re.search(r'2022\s*[-/]\s*0?3\b', t) or re.search(r'2022\s*[-/]\s*0?4\b', t) or re.search(r'2022\s*[-/]\s*0?5\b', t):
        return True
    # MM/2022
    if re.search(r'\b0?3\s*[-/]\s*2022\b', t) or re.search(r'\b0?4\s*[-/]\s*2022\b', t) or re.search(r'\b0?5\s*[-/]\s*2022\b', t):
        return True
    return False

spring_df = proj_df[proj_df['st'].apply(is_spring_2022)].copy()

# Join with funding totals
spring_df['Total_Funding'] = spring_df['Project_Name'].map(fund_map).fillna(0).astype(int)

count_projects = int(spring_df.shape[0])
total_funding = int(spring_df['Total_Funding'].sum())

out = {'projects_started_spring_2022': count_projects, 'total_funding': total_funding}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CxHqyMELXWVY83oXrfOfhBAQ': ['Funding'], 'var_call_ktn2NXP67hv32AVFGAlEMGmp': 'file_storage/call_ktn2NXP67hv32AVFGAlEMGmp.json', 'var_call_QPGkwQMFhoAS3XLLfcXdXfAi': 'file_storage/call_QPGkwQMFhoAS3XLLfcXdXfAi.json'}

exec(code, env_args)
