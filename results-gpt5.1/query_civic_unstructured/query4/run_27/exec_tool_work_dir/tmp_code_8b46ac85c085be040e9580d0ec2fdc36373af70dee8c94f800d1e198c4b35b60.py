code = """import re, json, pandas as pd

path_civic = var_call_srw8dg07quPgYw1Yevp5xaph
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

path_funding = var_call_4Z80jcpVk3hmtIXwHqHLembF
with open(path_funding, 'r') as f:
    funding = json.load(f)

project_keywords = ["Project", "Improvements", "Repairs", "Drain", "Road", "Playground", "Park", "Bridge", "Canyon", "Storm", "Median", "Signals", "Water", "Skate", "Walkway", "Biofilter", "Slope", "Roof", "Shade", "HVAC"]

project_records = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        if any(k in line_clean for k in project_keywords) and len(line_clean) > 10:
            current_project = line_clean
        if current_project:
            pattern = r"(Begin Construction|Start|Project Start)[^0-9A-Za-z]*(Spring 2022|2022-Spring|March 2022|April 2022|May 2022|2022-March|2022-04|2022-05)"
            m = re.search(pattern, line_clean, re.IGNORECASE)
            if m:
                st = m.group(2)
                project_records.append({"Project_Name": current_project, "st": st})

proj_start = {}
for rec in project_records:
    name = rec['Project_Name']
    if name not in proj_start:
        proj_start[name] = rec['st']

spring_projects = list(proj_start.keys())

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched_funding = []
for pname in spring_projects:
    for _, row in fund_df.iterrows():
        fn = row['Project_Name']
        if pname == fn or pname in fn or fn in pname:
            matched_funding.append({"Project_Name": pname, "Funding_Project_Name": fn, "Amount": int(row['Amount'])})

if matched_funding:
    total_funding = sum(r['Amount'] for r in matched_funding)
    num_projects = len(set(r['Project_Name'] for r in matched_funding))
else:
    total_funding = 0
    num_projects = 0

result = {"num_projects_spring_2022": num_projects, "total_funding_spring_2022": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_srw8dg07quPgYw1Yevp5xaph': 'file_storage/call_srw8dg07quPgYw1Yevp5xaph.json', 'var_call_4Z80jcpVk3hmtIXwHqHLembF': 'file_storage/call_4Z80jcpVk3hmtIXwHqHLembF.json'}

exec(code, env_args)
