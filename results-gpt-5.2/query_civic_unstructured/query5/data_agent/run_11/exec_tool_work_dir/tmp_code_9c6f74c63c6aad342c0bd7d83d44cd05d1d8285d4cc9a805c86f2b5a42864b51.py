code = """import json, re
import pandas as pd

with open(var_call_ivRvrB6C6c4E1YIc1nGaYvPo, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

with open(var_call_8fkncmUqzr1w9RAFHBU5aXKQ, 'r') as f:
    docs = json.load(f)

begin_pat = re.compile('Begin\\s+Construction\\s*:\\s*([^\\n\\r]+)', re.IGNORECASE)

# project names are often a line followed by a bullet Updates. Use that pattern.
proj_line_pat = re.compile('^\\s*([A-Z0-9][A-Za-z0-9].{3,120})\\s*$')

bad_starts = ('(cid:', 'Page', 'Agenda Item', 'RECOMMENDED', 'DISCUSSION', 'Subject', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date')

def looks_like_project(name):
    n=name.strip()
    if len(n) < 5 or len(n) > 120: return False
    if n.startswith(bad_starts): return False
    low=n.lower()
    if 'begin construction' in low or 'complete design' in low or 'advertise' in low: return False
    # avoid sentences
    if n.endswith('.') and '(' not in n: return False
    # must contain either (FEMA/CalOES/CalJPIA/Project) or typical infrastructure keywords
    if re.search('\\((fema|caloes|caljpia).*?\\)', low): return True
    if 'project' in low: return True
    # or a road/park/canyon etc
    if any(k in low for k in ['road','canyon','storm','drain','guardrail','sirens','warning','culvert','bridge','slope','retaining','fire']):
        return True
    return False

projects=set()

for d in docs:
    lines = d.get('text','').splitlines()
    in_disaster=False
    current=None
    for i,line in enumerate(lines):
        if re.search('^\\s*Disaster\\s+Projects', line, re.IGNORECASE) or re.search('^\\s*Disaster\\s+Recovery\\s+Projects', line, re.IGNORECASE):
            in_disaster=True
            current=None
            continue
        if in_disaster and re.search('^\\s*Capital\\s+Improvement\\s+Projects', line, re.IGNORECASE):
            in_disaster=False
            current=None
            continue
        if not in_disaster:
            continue
        # set current if next non-empty line contains '(cid:190) Updates' etc.
        m=proj_line_pat.match(line)
        if m:
            cand=m.group(1).strip()
            if looks_like_project(cand):
                # look ahead for Updates or Project Schedule within next 3 lines
                ahead='\n'.join([l.strip() for l in lines[i+1:i+4]])
                if re.search('Updates', ahead, re.IGNORECASE) or re.search('Project Schedule', ahead, re.IGNORECASE) or re.search('Estimated Schedule', ahead, re.IGNORECASE):
                    current=cand
                    continue
        bm=begin_pat.search(line)
        if bm and current:
            if '2022' in bm.group(1):
                projects.add(current)

# sum funding
missing=[]
total=0
for p in sorted(projects):
    if p in fund_map:
        total += int(fund_map[p])
    else:
        missing.append(p)

out={'projects_started_2022_disaster': sorted(projects), 'project_count': len(projects), 'total_funding': total, 'missing_in_funding_table': missing}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yAUEJ8JKx4IeDyLqvdXX7Jdg': ['Funding'], 'var_call_R0TM1H3XPtIHjyIdLKkamUlz': ['civic_docs'], 'var_call_ivRvrB6C6c4E1YIc1nGaYvPo': 'file_storage/call_ivRvrB6C6c4E1YIc1nGaYvPo.json', 'var_call_AkQRhbxir44oE575dYS4n4Rj': 'file_storage/call_AkQRhbxir44oE575dYS4n4Rj.json', 'var_call_TfvforcoJQxTdlqpzOWf4soP': {'projects_started_2022_disaster': [], 'project_count': 0, 'total_funding': 0, 'missing_in_funding_table': []}, 'var_call_ZpccyN8b09rFWpVlJ0NdzBGw': 'file_storage/call_ZpccyN8b09rFWpVlJ0NdzBGw.json', 'var_call_8fkncmUqzr1w9RAFHBU5aXKQ': 'file_storage/call_8fkncmUqzr1w9RAFHBU5aXKQ.json', 'var_call_2VfP9GZDGXvo6Mayz9Rm0JxC': {'projects_started_2022_disaster': ['Fire.', 'Summer 2022.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'beginning in April 2022.', 'beginning in Fall 2022.', 'beginning in Spring 2022.', 'bid with bids due November 17.', 'coming weeks.', 'completing the final design.', 'damaged by the Woolsey Fire.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'final design and preparing the project for public bidding.', 'guardrails within the project limits.', 'is finalizing the bid documents.', 'of 2022.', 'started and is anticipated to be completed by the Spring of 2022.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'project_count': 22, 'total_funding': 87000, 'missing_in_funding_table': ['Fire.', 'Summer 2022.', 'Westward Beach Road.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'beginning in April 2022.', 'beginning in Fall 2022.', 'beginning in Spring 2022.', 'bid with bids due November 17.', 'coming weeks.', 'completing the final design.', 'damaged by the Woolsey Fire.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'final design and preparing the project for public bidding.', 'guardrails within the project limits.', 'is finalizing the bid documents.', 'of 2022.', 'started and is anticipated to be completed by the Spring of 2022.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}}

exec(code, env_args)
