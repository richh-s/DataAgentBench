code = """import json, re
import pandas as pd

# Load funding rows
path = var_call_mQrjm1h02WQM3utfLB3BmZuz
with open(path, 'r') as f:
    funding = json.load(f)

# Load civic docs subset (disaster keyword docs)
path2 = var_call_9NvOPp8Od4Z86I4e0PwQ75Pc
with open(path2, 'r') as f:
    docs = json.load(f)

# Heuristic parse: in these agenda reports, disaster projects appear under heading 'Disaster Recovery Projects'
# We'll extract lines between that heading and next major heading (or end), then within that block pick project name lines.

disaster_projects=set()
for d in docs:
    text=d.get('text','')
    m = re.search(r'(?im)^\s*Disaster Recovery Projects.*$', text)
    if not m:
        continue
    start = m.end()
    # end at next 'Capital Improvement Projects' or 'Public Safety' etc; simple: next all-caps heading with 'Projects'
    endm = re.search(r'(?im)^\s*Capital Improvement Projects\b', text[start:])
    end = start + endm.start() if endm else len(text)
    block = text[start:end]
    # Candidate project name lines: non-empty lines without bullets, short-ish, Title Case, not containing ':'
    for line in block.splitlines():
        line=line.strip()
        if not line:
            continue
        # stop at schedule section markers
        if re.search(r'(?i)updates|project schedule|estimated schedule|project description', line):
            continue
        # exclude bullet artifacts
        if line.startswith(('(cid', 'Page', 'Agenda', 'Item')):
            continue
        # likely project names include 'FEMA' 'CalOES' 'CalJPIA' 'Road' 'Culvert' etc
        if len(line)>3 and len(line)<120 and not ':' in line:
            # avoid generic headings
            if re.fullmatch(r'(?i)(design|construction|not started)', line):
                continue
            if re.search(r'(?i)projects status|recommended action|discussion', line):
                continue
            # accept if contains typical disaster markers or appears in funding list later
            disaster_projects.add(line)

# Determine start year 2022 for each disaster project by finding its schedule line with 2022 'Begin Construction' or 'Start'
# We'll search entire doc text around each project occurrence for 'Begin Construction' lines containing 2022.
started_2022=set()
for d in docs:
    text=d.get('text','')
    for pname in disaster_projects:
        idx = text.find(pname)
        if idx==-1:
            continue
        window = text[idx: idx+2000]
        # look for begin construction / start / advertise with 2022
        if re.search(r'(?i)(begin construction|start(ed)?|construction begin|project schedule).*2022', window, re.S):
            started_2022.add(pname)
        else:
            # also if any line within window mentions 2022 and begin construction
            if re.search(r'(?im)^.*Begin Construction.*2022.*$', window):
                started_2022.add(pname)

# Join with funding by exact Project_Name match
fund_df=pd.DataFrame(funding)
fund_df['Amount']=pd.to_numeric(fund_df['Amount'], errors='coerce')

started_list=sorted(started_2022)
match_df=fund_df[fund_df['Project_Name'].isin(started_list)]

total = float(match_df['Amount'].sum()) if not match_df.empty else 0.0

out = {
    'total_funding_disaster_projects_started_2022': int(total),
    'matched_projects_count': int(match_df['Project_Name'].nunique()),
    'matched_projects': started_list
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Fc0oL0hrbVYTe8YLBCBpfWKq': ['Funding'], 'var_call_mQrjm1h02WQM3utfLB3BmZuz': 'file_storage/call_mQrjm1h02WQM3utfLB3BmZuz.json', 'var_call_9NvOPp8Od4Z86I4e0PwQ75Pc': 'file_storage/call_9NvOPp8Od4Z86I4e0PwQ75Pc.json'}

exec(code, env_args)
