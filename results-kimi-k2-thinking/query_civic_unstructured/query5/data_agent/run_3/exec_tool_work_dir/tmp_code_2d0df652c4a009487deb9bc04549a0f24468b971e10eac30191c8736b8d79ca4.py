code = """import json
import pandas as pd
import re

# Load the data
civic_docs_data = locals()['var_functions.query_db:0']
funding_data = locals()['var_functions.query_db:2']

# Load from files if they're strings
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)
        
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert to DataFrames
df_civic = pd.DataFrame(civic_docs_data)
df_funding = pd.DataFrame(funding_data)

# Find disaster-related projects in funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Fire']
funding_disaster = df_funding[df_funding['Project_Name'].str.contains('|'.join(disaster_keywords), case=False)].copy()

# Convert Amount to integer
funding_disaster['Amount'] = funding_disaster['Amount'].astype(int)

print('Disaster-related funding records found:', len(funding_disaster))

# Get unique disaster project names
disaster_project_names = funding_disaster['Project_Name'].unique()
print('Unique disaster projects:', len(disaster_project_names))

# Create a mapping of project information from documents
project_info = {}

for _, doc in df_civic.iterrows():
    text = doc['text']
    
    # For each disaster project, find mentions and look for start dates
    for proj_name in disaster_project_names:
        if proj_name in text:
            # Extract context around the project name
            idx = text.find(proj_name)
            context = text[max(0, idx-500):min(len(text), idx+500)]
            
            # Look for date patterns that indicate start times
            # Look for: "2022", "Begin", "Start", "Complete Design", "Advertise"
            lines = context.split('\n')
            
            st_date = None
            et_date = None
            project_status = 'unknown'
            
            for i, line in enumerate(lines):
                line_lower = line.lower()
                
                # Determine status
                if 'design' in line_lower:
                    project_status = 'design'
                elif 'construction' in line_lower:
                    project_status = 'construction'
                elif 'complete' in line_lower:
                    project_status = 'completed'
                elif 'not started' in line_lower:
                    project_status = 'not started'
                
                # Look for dates
                year_matches = re.findall(r'202[0-9]', line)
                if year_matches:
                    if 'Begin' in line or 'Start' in line or 'Complete Design' in line:
                        st_date = year_matches[0] if year_matches else None
                    elif 'Complete' in line and 'Construction' in line:
                        et_date = year_matches[0] if year_matches else None
            
            # If we found a 2022 start date, record it
            if st_date == '2022':
                if proj_name not in project_info:
                    project_info[proj_name] = {
                        'st': st_date,
                        'status': project_status,
                        'has_2022_mention': '2022' in text
                    }

print('Disaster projects with 2022 start dates found:', len(project_info))

# Calculate funding for these projects
projects_started_2022 = list(project_info.keys())
total_funding_2022_start = 0

for proj_name in projects_started_2022:
    proj_funding = funding_disaster[funding_disaster['Project_Name'] == proj_name]
    if not proj_funding.empty:
        amount = proj_funding['Amount'].sum()
        total_funding_2022_start += amount
        project_info[proj_name]['funding'] = amount
        project_info[proj_name]['funding_records'] = len(proj_funding)

print('Total funding for disaster projects starting in 2022: $', total_funding_2022_start)
print('Number of projects:', len(projects_started_2022))

result = {
    'total_funding_2022_start': int(total_funding_2022_start),
    'project_count': len(projects_started_2022),
    'project_details': project_info
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'civic_docs_shape': [5, 3], 'funding_shape': [500, 4], 'civic_docs_columns': ['_id', 'filename', 'text'], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:18': {'total_funding': 1367000, 'project_count': 26, 'funding_records': 26}}

exec(code, env_args)
