code = """import json
import pandas as pd
import re

# Load datasets
funding_file = locals()['var_functions.query_db:5']
civic_file = locals()['var_functions.query_db:0']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Convert to DataFrames
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Identify disaster-related projects in funding
disaster_pattern = r'FEMA|Cal.?OES|CalJPIA|disaster|recovery|fire'
disaster_mask = funding_df['Project_Name'].str.contains(disaster_pattern, case=False, na=False)
disaster_funding_df = funding_df[disaster_mask].copy()

# Extract project information from civic documents
project_info = []

for doc in civic_data:
    text = doc.get('text', '')
    # Split into sections that likely contain project info
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        # Check for disaster-related content
        if re.search(disaster_pattern, section, re.IGNORECASE):
            # Extract project names and dates
            lines = section.split('\n')
            project_name = None
            start_date = None
            
            for i, line in enumerate(lines):
                line = line.strip()
                # Look for project name (usually first line or bolded)
                if not project_name and len(line) > 5 and len(line) < 100:
                    if any(keyword in line.lower() for keyword in ['project', 'improvement', 'repair', 'replacement']):
                        if not line.startswith(('(', '•', '-', '●')):
                            project_name = line
                
                # Look for 2022 start dates
                if re.search(r'2022', line):
                    start_date = line
                    break
            
            if project_name:
                project_info.append({
                    'Project_Name': project_name,
                    'Section': section[:200],
                    'Has_2022': bool(start_date)
                })

# Create a mapping of project names that started in 202n
projects_with_2022 = set()
for info in project_info:
    if info['Has_2022']:
        # Clean project name for matching
        clean_name = info['Project_Name'].split('(')[0].strip()
        projects_with_2022.add(clean_name)

# Match funding data with projects that started in 2022
total_funding_2022 = 0
matched_projects = []

for _, row in disaster_funding_df.iterrows():
    fund_name = row['Project_Name']
    fund_amount = row['Amount']
    
    # Check if this project name contains 2022 or matches a project with 2022 start
    if '2022' in fund_name:
        total_funding_2022 += fund_amount
        matched_projects.append(fund_name)
    else:
        # Check against extracted project names
        for proj_name in projects_with_2022:
            if fund_name.startswith(proj_name) or proj_name in fund_name:
                total_funding_2022 += fund_amount
                matched_projects.append(fund_name)
                break

result_dict = {
    'total_funding_2022_disaster': int(total_funding_2022),
    'matched_projects': matched_projects,
    'total_disaster_projects': len(disaster_funding_df),
    'total_disaster_funding': int(disaster_funding_df['Amount'].sum())
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
