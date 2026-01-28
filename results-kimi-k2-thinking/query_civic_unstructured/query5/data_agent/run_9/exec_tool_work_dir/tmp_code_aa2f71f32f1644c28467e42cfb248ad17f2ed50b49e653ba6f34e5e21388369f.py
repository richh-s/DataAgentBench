code = """import json
import re

# Load civic_docs data from the file path stored in the variable
civic_docs_var = locals()['var_functions.query_db:6']
civic_docs_full = []
with open(civic_docs_var, 'r') as f:
    civic_docs_full = json.load(f)

# Load funding data from the file path stored in the variable  
funding_var = locals()['var_functions.query_db:8']
funding_full = []
with open(funding_var, 'r') as f:
    funding_full = json.load(f)

# Convert funding data to dataframe for easier lookup
import pandas as pd
funding_df = pd.DataFrame(funding_full)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract project information from civic_docs
projects = []

for doc in civic_docs_full:
    text = doc.get('text', '')
    
    # Look for project sections - they often appear with specific patterns
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for potential disaster projects
        disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']
        
        # Check if line contains disaster project indicators
        is_disaster = False
        if any(keyword in line for keyword in disaster_keywords):
            is_disaster = True
        
        # Also check if line looks like a project name and contains disaster suffix
        if re.search(r'\((FEMA|CalOES|CalJPIA)( Project)?\)', line):
            is_disaster = True
        
        if is_disaster and len(line) > 10 and not line.startswith('('):
            # Extract project name 
            project_name = line
            
            # Look for dates in surrounding lines (st field)
            date_str = ''
            # Check next few lines for dates
            for j in range(max(0, i-2), min(len(lines), i+3)):
                if j != i:
                    context_line = lines[j].strip()
                    if '2022' in context_line or '2023' in context_line or '2024' in context_line:
                        if any(word in context_line for word in ['Schedule', 'Start', 'Begin', 'Complete']):
                            date_str += context_line + '; '
            
            # Also check if project name itself has a year
            if '2022' in project_name:
                date_str = '2022'
            
            # Extract type from context
            project_type = 'disaster'
            
            # Try to extract status
            status = ''
            if 'design' in text.lower():
                status = 'design'
            elif 'construction' in text.lower() or 'completed' in text.lower():
                status = 'completed'
            elif 'not started' in text.lower():
                status = 'not started'
            
            projects.append({
                'Project_Name': project_name,
                'type': project_type,
                'st': date_str.strip(),
                'status': status
            })

# Create projects dataframe
projects_df = pd.DataFrame(projects)

# Filter for projects that started in 2022
disaster_project_names = set()

for _, project in projects_df.iterrows():
    st = str(project['st'])
    project_name = str(project['Project_Name'])
    
    # Check if project started in 2022
    started_in_2022 = False
    if '2022' in st:
        started_in_2022 = True
    if project_name.startswith('2022'):
        started_in_2022 = True
    
    if started_in_2022:
        disaster_project_names.add(project_name)

# Also look for disaster projects in funding data that have 2022 in name
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']
for _, row in funding_df.iterrows():
    project_name = row['Project_Name']
    if '2022' in project_name and any(keyword in project_name for keyword in disaster_keywords):
        disaster_project_names.add(project_name)
                            
# Now sum funding for these disaster projects
total_funding = 0
matched_projects = set()

for _, row in funding_df.iterrows():
    funding_project = row['Project_Name']
    amount = row['Amount']
    
    # Check if this funding matches any of our disaster projects
    for disaster_proj in disaster_project_names:
        # Exact match
        if funding_project == disaster_proj:
            total_funding += amount
            matched_projects.add(funding_project)
            break
        
        # Partial match
        elif disaster_proj in funding_project or funding_project in disaster_proj:
            # Additional check to make sure it's really about disaster
            if any(keyword in funding_project for keyword in disaster_keywords):
                total_funding += amount
                matched_projects.add(funding_project)
                break

result = {
    'total_funding': int(total_funding),
    'matched_projects': list(matched_projects),
    'number_of_projects': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
