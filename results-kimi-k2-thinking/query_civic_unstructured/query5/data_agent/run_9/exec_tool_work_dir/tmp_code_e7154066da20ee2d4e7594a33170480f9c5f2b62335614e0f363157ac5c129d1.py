code = """import json
import re

# Load the civic documents
civic_docs_path = var_functions.query_db_6
civic_docs_data = []
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Load the funding data
funding_path = var_functions.query_db_8
funding_data = []
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert to DataFrame
import pandas as pd
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract disaster projects from civic_docs
projects = []
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        is_disaster = False
        if any(keyword in line for keyword in disaster_keywords):
            is_disaster = True
        if re.search(r'\((FEMA|CalOES|CalJPIA)( Project)?\)', line):
            is_disaster = True
            
        if is_disaster and len(line) > 10:
            project_name = line
            date_str = ''
            
            # Look for dates in context
            for j in range(max(0, i-3), min(len(lines), i+4)):
                ctx_line = lines[j].strip()
                if '2022' in ctx_line:
                    if any(word in ctx_line for word in ['Start', 'Begin', 'Complete', 'Design', 'Construction']):
                        date_str += ctx_line + '; '
            
            if '2022' in project_name:
                date_str = '2022'
                
            projects.append({
                'Project_Name': project_name,
                'st': date_str
            })

# Build set of disaster project names that started in 2022
disaster_2022_projects = set()
for proj in projects:
    st = proj['st']
    name = proj['Project_Name']
    if '2022' in st or '2022' in name:
        disaster_2022_projects.add(name)

# Also add funding records with 2022 and disaster keywords
for _, row in funding_df.iterrows():
    proj_name = row['Project_Name']
    if '2022' in proj_name and any(kw in proj_name for kw in disaster_keywords):
        disaster_2022_projects.add(proj_name)

# Sum funding for matching projects
total_funding = 0
matched = set()

for _, row in funding_df.iterrows():
    fund_name = row['Project_Name']
    amount = row['Amount']
    
    for disaster_proj in disaster_2022_projects:
        if fund_name == disaster_proj:
            total_funding += amount
            matched.add(fund_name)
            break
        elif disaster_proj in fund_name or fund_name in disaster_proj:
            if any(kw in fund_name for kw in disaster_keywords):
                total_funding += amount
                matched.add(fund_name)
                break

result = {
    'total_funding': int(total_funding),
    'number_of_projects': len(matched),
    'projects': list(matched)
}

print('%s__RESULT__:%s' % ('', ''))
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
