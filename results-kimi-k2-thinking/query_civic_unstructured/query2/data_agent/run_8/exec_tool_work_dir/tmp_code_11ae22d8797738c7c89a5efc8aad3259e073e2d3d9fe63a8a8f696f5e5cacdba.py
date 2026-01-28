code = """import json
import pandas as pd
import re

# Get the file paths from the storage variables
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

# Load the data from the JSON files
with open(civic_docs_path, 'r') as f:
    civic_docs_list = json.load(f)

with open(funding_path, 'r') as f:
    funding_list = json.load(f)

# Create a DataFrame from funding data
funding_df = pd.DataFrame(funding_list)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Extract project information from civic documents
extracted_projects = []

for doc in civic_docs_list:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split into lines and process
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Detect project names (all caps or containing 'Project')
        if (line.isupper() or 'Project' in line) and 10 < len(line) < 200:
            current_project = line
        
        if current_project:
            # Extract status
            status = None
            lower_line = line.lower()
            if 'completed' in lower_line or 'construction was completed' in lower_line:
                status = 'completed'
            elif 'design' in lower_line or 'working with consultant' in lower_line:
                status = 'design'
            elif 'not started' in lower_line:
                status = 'not started'
            
            # Extract end time (year)
            et = None
            if 'Complete' in line or 'complete' in lower_line:
                year_match = re.search(r'(20\d{2})', line)
                if year_match:
                    et = year_match.group(1)
            
            # Check if park-related
            is_park = 'park' in current_project.lower() or 'park' in lower_line
            topic = 'park' if is_park else ''
            
            if status or et or topic:
                extracted_projects.append({
                    'Project_Name': current_project,
                    'status': status,
                    'et': et,
                    'topic': topic,
                    'source_file': filename
                })

# Create projects DataFrame
projects_df = pd.DataFrame(extracted_projects)

# Filter for park-related projects completed in 2022
park_completed_2022 = projects_df[
    (projects_df['topic'] == 'park') & 
    (projects_df['status'] == 'completed') & 
    (projects_df['et'] == '2022')
]

# Get project names
park_project_names = park_completed_2022['Project_Name'].unique()
print('Found park projects completed in 2022:', len(park_project_names))
for name in park_project_names:
    print(' -', name)

# Match with funding data
total_funding = 0
matched_projects = []

for project_name in park_project_names:
    # Normalize project name for matching
    normalized_name = project_name.replace('(CalOES Project)', '').replace('(FEMA Project)', '').strip()
    
    # Look for matching funding records
    matching_records = funding_df[
        funding_df['Project_Name'].str.contains(normalized_name, case=False, na=False) |
        (funding_df['Project_Name'].str.contains(project_name.split()[0], case=False, na=False) & 
         funding_df['Project_Name'].str.contains('park', case=False, na=False))
    ]
    
    if not matching_records.empty:
        project_funding = matching_records['Amount'].sum()
        total_funding += project_funding
        matched_projects.append({
            'project': project_name,
            'funding': int(project_funding),
            'records': len(matching_records)
        })

result = {
    'total_funding': int(total_funding),
    'matched_projects': matched_projects,
    'projects_found': len(park_project_names)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
