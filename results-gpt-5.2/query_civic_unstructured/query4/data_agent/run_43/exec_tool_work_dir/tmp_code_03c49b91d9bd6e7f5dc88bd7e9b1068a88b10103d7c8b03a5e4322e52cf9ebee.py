code = """import json, re
import pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str) and maybe_path_or_records.endswith('.json'):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

civic_docs = load_records(var_call_EO4v1yp3Uj7WyrQzaRGJbxtD)
funding = load_records(var_call_LbdE6UW2GnuMIdmVDJSZoy3B)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# Parse projects from civic documents by section headings.
projects = []
for doc in civic_docs:
    text = doc.get('text','') or ''
    # normalize
    t = text.replace('\r','')
    # Find blocks that look like project entries: a line (project name) followed by bullet sections containing 'Project Schedule'
    # We'll scan linewise.
    lines = [ln.strip() for ln in t.split('\n')]
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        # candidate project name line: non-empty, not a heading like 'Capital Improvement Projects (Design)' etc.
        if line and len(line) < 120 and not re.search(r'Projects\b|Agenda|Page \d|Item|Recommended Action|DISCUSSION|To:|Prepared by:|Subject:|Updates:|Project Schedule', line, re.I):
            # look ahead for 'Project Schedule' within next 25 lines
            window = '\n'.join(lines[i:i+35])
            if re.search(r'Project Schedule', window, re.I):
                # extract schedule lines after 'Project Schedule'
                m = re.search(r'Project Schedule[^\n]*:\s*(.*)', window, re.I|re.S)
                sched_block = m.group(1) if m else window
                # get first occurrence of Begin Construction / Begin Design etc
                st = None
                for pat in [r'Begin Construction\s*:\s*([^\n]+)', r'Begin\s+Construction\s*:\s*([^\n]+)', r'Begin\s+Design\s*:\s*([^\n]+)']:
                    mm = re.search(pat, window, re.I)
                    if mm:
                        st = mm.group(1).strip()
                        break
                # some schedules use 'Start Construction'
                if st is None:
                    mm = re.search(r'Start\s+Construction\s*:\s*([^\n]+)', window, re.I)
                    if mm:
                        st = mm.group(1).strip()
                projects.append({'Project_Name': line, 'st': st, 'filename': doc.get('filename')})
                # advance a bit to avoid duplicates within same block
                i += 5
                continue
        i += 1

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','st'])

# Spring 2022: st contains 'Spring' and '2022' OR a month in Mar/Apr/May 2022
spring_months = ['march','april','may']

def is_spring_2022(st):
    if st is None:
        return False
    s = str(st).strip().lower()
    if '2022' not in s:
        return False
    if 'spring' in s:
        return True
    # month name
    for m in spring_months:
        if m in s:
            return True
    # numeric month
    mnum = re.search(r'2022[-/](0?3|0?4|0?5)\b', s)
    if mnum:
        return True
    return False

spring_df = proj_df[proj_df['st'].apply(is_spring_2022)].copy()

# Join funding by exact Project_Name
spring_df['funding'] = spring_df['Project_Name'].map(fund_map).fillna(0).astype(int)

count_projects = int(spring_df['Project_Name'].nunique())
total_funding = int(spring_df.drop_duplicates(subset=['Project_Name'])['funding'].sum())

result = {'projects_started_spring_2022': count_projects, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EO4v1yp3Uj7WyrQzaRGJbxtD': 'file_storage/call_EO4v1yp3Uj7WyrQzaRGJbxtD.json', 'var_call_LbdE6UW2GnuMIdmVDJSZoy3B': 'file_storage/call_LbdE6UW2GnuMIdmVDJSZoy3B.json'}

exec(code, env_args)
