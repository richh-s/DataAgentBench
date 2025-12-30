code = """import json, re
import pandas as pd

# Load full civic docs
path = var_call_0QPmnUbxHRQuJFaWcbbomhQ7
with open(path, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]

# Heuristic: project lines are those that look like project titles (capitalized, possibly with year) and not bullets
project_lines = []
for text in texts:
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Ignore bullets and obvious non-project headers
        if line.startswith(('(', 'cid:', '', '1', '-', '0')):
            continue
        if any(kw in line for kw in ['Project Description', 'Updates', 'Project Schedule', 'Estimated Schedule']):
            continue
        # Heuristic: contain keywords like 'Project', 'Improvements', 'Repairs', 'Park', 'Road', 'Bridge', 'Facility', 'Study', 'Playground', 'Warning', 'Drain', 'Slope', 'Canyon', 'Median', 'Crosswalk', 'Water', 'Storm'
        if any(kw in line for kw in ['Project', 'Improvements', 'Repairs', 'Park', 'Road', 'Bridge', 'Facility', 'Study', 'Playground', 'Warning', 'Drain', 'Slope', 'Canyon', 'Median', 'Crosswalk', 'Water', 'Storm']):
            project_lines.append(line)

# Deduplicate
project_names = sorted(set(project_lines))

# Now extract approximate start dates associated with each project by scanning surrounding text windows for patterns like 'Begin Construction: Spring 2022' or 'Start: 2022-Spring'

projects = []
for text in texts:
    lines = [l.strip() for l in text.split('\n')]
    for i, line in enumerate(lines):
        if line.strip() in project_names:
            name = line.strip()
            window = '\n'.join(lines[i:i+15])
            # Look for Spring 2022 indicators
            st = None
            # Patterns like 'Begin Construction: Spring 2022' or 'Start: Spring 2022'
            m = re.search(r'(Begin Construction|Start|Start Date)[:\s]+(Spring 2022|2022 Spring|2022-Spring|March 2022|April 2022|May 2022|2022-03|2022-04|2022-05|2022-March|2022-April|2022-May)', window, re.IGNORECASE)
            if m:
                st = m.group(2)
            # Also capture bullet list where year-season appears alone
            if not st:
                m2 = re.search(r'(Spring 2022|2022 Spring|2022-Spring)', window, re.IGNORECASE)
                if m2:
                    st = m2.group(1)
            if st:
                projects.append({'Project_Name': name, 'st': st})

# Filter to Spring 2022 start
spring_projects = [p for p in projects if re.search(r'2022', p['st']) and re.search(r'Spring', p['st'], re.IGNORECASE)]

# Deduplicate by project name
spring_df = pd.DataFrame(spring_projects)
if not spring_df.empty:
    spring_df = spring_df.drop_duplicates(subset=['Project_Name'])
    spring_project_names = spring_df['Project_Name'].tolist()
else:
    spring_project_names = []

# Load funding aggregated
path2 = var_call_A0hxgifrMmW4cOEJ4UAR0lqG
with open(path2, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)

# Join on Project_Name
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
