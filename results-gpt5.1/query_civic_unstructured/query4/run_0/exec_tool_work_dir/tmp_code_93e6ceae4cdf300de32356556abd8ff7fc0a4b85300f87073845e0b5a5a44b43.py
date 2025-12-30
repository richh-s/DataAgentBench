code = """import json, re
import pandas as pd

path = var_call_0QPmnUbxHRQuJFaWcbbomhQ7
with open(path, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]

project_lines = []
for text in texts:
    for raw_line in text.split('\n'):
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(('(', 'cid:', '\u0019', '\u00131', '-', '\u00190')):
            continue
        if any(kw in line for kw in ['Project Description', 'Updates', 'Project Schedule', 'Estimated Schedule']):
            continue
        if any(kw in line for kw in ['Project', 'Improvements', 'Repairs', 'Park', 'Road', 'Bridge', 'Facility', 'Study', 'Playground', 'Warning', 'Drain', 'Slope', 'Canyon', 'Median', 'Crosswalk', 'Water', 'Storm']):
            project_lines.append(line)

project_names = sorted(set(project_lines))

projects = []
for text in texts:
    lines = [l.strip() for l in text.split('\n')]
    for i, line in enumerate(lines):
        if line.strip() in project_names:
            name = line.strip()
            window = '\n'.join(lines[i:i+15])
            st = None
            m = re.search(r'(Begin Construction|Start|Start Date)[:\s]+(Spring 2022|2022 Spring|2022-Spring|March 2022|April 2022|May 2022|2022-03|2022-04|2022-05|2022-March|2022-April|2022-May)', window, re.IGNORECASE)
            if m:
                st = m.group(2)
            if not st:
                m2 = re.search(r'(Spring 2022|2022 Spring|2022-Spring)', window, re.IGNORECASE)
                if m2:
                    st = m2.group(1)
            if st:
                projects.append({'Project_Name': name, 'st': st})

spring_projects = [p for p in projects if re.search(r'2022', p['st']) and re.search(r'Spring', p['st'], re.IGNORECASE)]

spring_df = pd.DataFrame(spring_projects)
if not spring_df.empty:
    spring_df = spring_df.drop_duplicates(subset=['Project_Name'])
    spring_project_names = spring_df['Project_Name'].tolist()
else:
    spring_project_names = []

path2 = var_call_A0hxgifrMmW4cOEJ4UAR0lqG
with open(path2, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)

if spring_project_names:
    fund_spring = fund_df[fund_df['Project_Name'].isin(spring_project_names)]
    total_funding = fund_spring['Total_Amount'].astype(float).sum()
    project_count = len(spring_project_names)
else:
    total_funding = 0.0
    project_count = 0

result = {'project_count_spring_2022': int(project_count), 'total_funding_spring_2022': float(total_funding), 'project_names_spring_2022': spring_project_names}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0QPmnUbxHRQuJFaWcbbomhQ7': 'file_storage/call_0QPmnUbxHRQuJFaWcbbomhQ7.json', 'var_call_A0hxgifrMmW4cOEJ4UAR0lqG': 'file_storage/call_A0hxgifrMmW4cOEJ4UAR0lqG.json', 'var_call_IN4fnhtRRnta3ArWWAdAWHya': ['civic_docs'], 'var_call_Vk8R2MhPF3ZR60FL2OPIFHba': ['Funding']}

exec(code, env_args)
