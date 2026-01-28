code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_8KSFHPME3XKGlM1dBcPsJJ9B)
records_docs = json.loads(path_docs.read_text())
texts = [r['text'] for r in records_docs]

keywords = ['Project','Improvements','Repairs','Resurfacing','Storm Drain','Playground','Shade Structure','Water Treatment','Traffic Study','Warning Signs','Warning Sirens','Park','Bridge','Culvert','Biofilter','Roof Replacement','HVAC Replacement','Median Improvements','Green Streets','Benches','Arbors','Workout Station','Water Quality']

project_infos = {}

for text in texts:
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if any(k in line for k in keywords):
            name = line
            window = '\n'.join(lines[i:i+15])
            m = re.search(r'Begin Construction:\s*([A-Za-z]+\s+\d{4})', window)
            st = None
            if m:
                st = m.group(1)
            else:
                m2 = re.search(r'(Spring|Summer|Fall|Winter)\s+2022', window)
                if m2:
                    st = m2.group(0)
            if st:
                key = name.strip()
                if key not in project_infos:
                    project_infos[key] = st

spring_projects = {n:s for n,s in project_infos.items() if 'Spring 2022' in s}

path_fund = Path(var_call_y37apTzdrARp93qO32zeMKUL)
fund_records = json.loads(path_fund.read_text())
fund_df = pd.DataFrame(fund_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched = fund_df[fund_df['Project_Name'].isin(spring_projects.keys())]

result = {
    'projects_started_spring_2022_count': int(len(matched)),
    'total_funding': int(matched['Amount'].sum()),
    'matched_projects': matched['Project_Name'].tolist(),
    'spring_projects_detected': spring_projects
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8KSFHPME3XKGlM1dBcPsJJ9B': 'file_storage/call_8KSFHPME3XKGlM1dBcPsJJ9B.json', 'var_call_y37apTzdrARp93qO32zeMKUL': 'file_storage/call_y37apTzdrARp93qO32zeMKUL.json'}

exec(code, env_args)
