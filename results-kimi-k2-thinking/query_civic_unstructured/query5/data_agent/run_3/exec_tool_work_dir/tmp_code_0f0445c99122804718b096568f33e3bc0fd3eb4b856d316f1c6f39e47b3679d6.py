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

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    current_project = None
    current_type = None
    current_status = None
    current_st = None
    current_et = None
    
    # Patterns to identify sections and project names
    section_patterns = [
        r'Capital Improvement Projects \(Design\)',
        r'Capital Improvement Projects \(Construction\)',
        r'Capital Improvement Projects \(Not Started\)',
        r'Disaster Recovery Projects'
    ]
    
    # Look for project lists by scanning for project names and details
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers to determine project type/status
        if 'Capital Improvement Projects (Design)' in line or 'Projects Under Design' in line:
            current_type = 'capital'
            current_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_type = 'capital' 
            current_status = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_type = 'capital'
            current_status = 'not started'
        elif 'Disaster Recovery Projects' in line:
            current_type = 'disaster'
            current_status = 'design'  # Default, may be updated
        
        # Look for potential project names (lines that don't look like regular text)
        # Project names are typically capitalized and don't end with punctuation
        if line and not line.startswith(('(', '•', '-', '●', '■')) and not any(pattern in line for pattern in section_patterns):
            if len(line) > 10 and (line.isupper() or (sum(1 for c in line if c.isupper()) > len(line) * 0.3)):
                # This looks like a project name
                if not any(keyword in line.lower() for keyword in ['updates', 'project schedule', 'recommended action', 'discussion', 'page', 'agenda item']):
                    
                    # Try to find dates in subsequent lines
                    st_found = None
                    et_found = None
                    
                    # Look ahead for dates
                    for j in range(i+1, min(i+10, len(lines))):
                        next_line = lines[j].strip()
                        if 'Complete Design' in next_line or 'Begin' in next_line or 'Advertise' in next_line:
                            # Look for year patterns
                            year_match = re.search(r'(202\d)', next_line)
                            if year_match:
                                if not st_found:
                                    st_found = year_match.group(1)
                                else:
                                    et_found = year_match.group(1)
                    
                    # Create project record
                    project_name = line.strip()
                    
                    # Determine if it's a disaster project based on name
                    if '(FEMA' in project_name or '(CalOES' in project_name or '(CalJPIA' in project_name or 'Disaster' in project_name or 'Recovery' in project_name:
                        proj_type = 'disaster'
                    else:
                        proj_type = current_type or 'capital'
                    
                    # Update status if construction mentioned
                    if 'Road Repair' in project_name or 'Slope Repair' in project_name:
                        if current_status == 'design':
                            current_status = 'construction'
                    
                    projects.append({
                        'Project_Name': project_name,
                        'type': proj_type,
                        'status': current_status or 'design',
                        'st': st_found,
                        'et': et_found,
                        'topic': extract_topics(project_name)
                    })
        
        i += 1
    
    return projects

def extract_topics(project_name):
    topics = []
    name_lower = project_name.lower()
    
    if 'drain' in name_lower or 'storm' in name_lower:
        topics.append('drainage')
    if 'road' in name_lower or 'street' in name_lower:
        topics.append('road')
    if 'park' in name_lower:
        topics.append('park')
    if 'fire' in name_lower or 'fema' in name_lower:
        topics.append('fire')
        topics.append('FEMA')
    if 'bridge' in name_lower:
        topics.append('bridge')
    if 'siren' in name_lower or 'warning' in name_lower:
        topics.append('emergency warning')
    if 'water' in name_lower:
        topics.append('water treatment')
    
    return ','.join(topics) if topics else ''

# Extract all projects from all documents
all_projects = []
for idx, row in df_civic.iterrows():
    text = row['text']
    projects = extract_projects_from_text(text)
    all_projects.extend(projects)

# Create DataFrame of extracted projects
df_extracted = pd.DataFrame(all_projects)

print('Extracted projects shape:', df_extracted.shape)
print('Sample extracted projects:')
print(df_extracted.head(10).to_string())

# Look for disaster-related projects that started in 2022
disaster_projects = df_extracted[df_extracted['type'] == 'disaster'].copy()
print('\nDisaster projects found:', len(disaster_projects))
print(disaster_projects[['Project_Name', 'st', 'et']].to_string())

# Filter for projects that started in 2022
disaster_2022 = disaster_projects[
    disaster_projects['st'].astype(str).str.contains('2022', na=False)
]

print('\nDisaster projects starting in 2022:', len(disaster_2022))
print(disaster_2022[['Project_Name', 'st', 'et']].to_string())

result = {
    'total_extracted_projects': len(df_extracted),
    'disaster_projects_total': len(disaster_projects),
    'disaster_projects_2022': len(disaster_2022),
    'extracted_projects': df_extracted.to_dict('records'),
    'disaster_2022_projects': disaster_2022.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'civic_docs_shape': [5, 3], 'funding_shape': [500, 4], 'civic_docs_columns': ['_id', 'filename', 'text'], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
