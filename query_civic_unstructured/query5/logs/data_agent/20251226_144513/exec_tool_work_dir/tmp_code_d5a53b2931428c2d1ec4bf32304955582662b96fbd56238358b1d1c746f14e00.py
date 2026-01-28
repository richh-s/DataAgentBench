code = """import pandas as pd
import json
with open(var_call_5QN77jpOE7FA1Nn31rsikxfH) as f:
    civic_docs = json.load(f)
with open(var_call_ap8UDFILoneRTWeHLiiAuxdH) as f:
    funding = json.load(f)
# Step 1: Extract disaster-related projects that started in 2022 from civic_docs
import re
disaster_projects = []
for doc in civic_docs:
    text = doc['text']
    # Attempt to extract sections that mention 'disaster' or disaster recovery and project descriptions
    # Look for project lines that mention 2022 as start, and disaster type
    # Commonly formatted: <Project Name> ... (Design/Construction/Not Started) or Project Schedule with Begin Construction: ...
    # For each line, look for keywords indicating disaster projects that started in 2022
    project_sections = re.findall(r'([^\n]+?(disaster|Disaster)[^\n]*)', text)
    for project_line, _ in project_sections:
        # Try to find start date/year
        if re.search(r'(Start|Begin|Complete|Advertise)[^0-9]*2022', project_line) or re.search(r'2022', project_line):
            disaster_projects.append(project_line)
    # Additionally, scan for 'Disaster Recovery Projects' section for projects with a 2022 date
    lines = text.split('\n')
    current_type = None
    current_name = None
    start_year = None
    for line in lines:
        if 'Disaster Recovery Project' in line or 'Disaster Project' in line or 'disaster' in line.lower():
            current_type = 'disaster'
        if 'Project Schedule:' in line or 'Begin Construction:' in line or 'Advertise:' in line or 'Complete Design:' in line:
            match = re.search(r'([A-Za-z ]+): ([A-Za-z ]+) (\d{4})', line)
            if match:
                descr, phase, year = match.groups()
                if year == '2022' and current_type == 'disaster':
                    disaster_projects.append(line)
        # Try extracting project name if it immediately follows 'Disaster Recovery Projects Status Report'
        if ('Disaster Recovery Projects Status Report' in line or 'Disaster Recovery Projects' in line) and (len(lines) > 0):
            # Look ahead for project names by finding next lines
            for subline in lines[lines.index(line)+1:lines.index(line)+5]:
                if subline.strip() and any(x in subline.lower() for x in ['project', 'repair']):
                    disaster_projects.append(subline)
# Now extract clean project names from those lines
project_names = set()
for line in disaster_projects:
    name_match = re.search(r'^([A-Za-z0-9 &\'-.]+?)(?: Project| Repair| Improvements| Status| Construction| Design|$)', line)
    if name_match:
        name = name_match.group(1).strip()
        if name:
            project_names.add(name)
# Step 2: Find matching project names in funding table
funding_df = pd.DataFrame(funding)
filtered_funding = funding_df[funding_df['Project_Name'].apply(lambda x: any(n in x for n in project_names))]
# Step 3: Total funding amount
total_funding = filtered_funding['Amount'].astype(int).sum()
print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_call_5QN77jpOE7FA1Nn31rsikxfH': 'file_storage/call_5QN77jpOE7FA1Nn31rsikxfH.json', 'var_call_ap8UDFILoneRTWeHLiiAuxdH': 'file_storage/call_ap8UDFILoneRTWeHLiiAuxdH.json'}

exec(code, env_args)
