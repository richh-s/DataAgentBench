code = """import json
import pandas as pd
import re

# Read civic documents file
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded civic_docs, count:', len(civic_docs))

# Read funding data
funding_data = locals()['var_functions.query_db:0']
funding_df = pd.DataFrame(funding_data)

print('Loaded funding_df, shape:', funding_df.shape)

# Initialize list for project data extracted from documents
projects_data = []

# Helper function to extract project information
def extract_projects(text, filename):
    projects = []
    
    # Look for project sections
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically lines that are capitalized and not too short)
        if len(line) > 10 and line.isupper() and not line.startswith('(') and not any(x in line for x in ['PAGE', 'AGENDA', 'ITEM', 'PUBLIC', 'CAPITAL', 'DISASTER']):
            # This might be a project name
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': '',
                'source_file': filename
            }
        
        # Extract details if we have a current project
        elif current_project:
            lower_line = line.lower()
            
            # Check for dates and status
            if '2022' in line and ('start' in lower_line or 'begin' in lower_line or 'advertise' in lower_line):
                current_project['st'] = '2022'
            elif '2022' in line and ('complete' in lower_line or 'end' in lower_line):
                if 'et' not in current_project or not current_project['et']:
                    current_project['et'] = '2022'
            
            # Check for status keywords
            if any(word in lower_line for word in ['design', 'planning', 'plans']):
                current_project['status'] = 'design'
            elif any(word in lower_line for word in ['construction', 'construction']):
                current_project['status'] = 'construction'
            elif any(word in lower_line for word in ['completed', 'finish', 'done']):
                current_project['status'] = 'completed'
            elif any(word in lower_line for word in ['not started', 'future', 'pending']):
                current_project['status'] = 'not started'
            
            # Check for topics
            if 'fema' in lower_line or 'disaster' in lower_line or 'caloes' in lower_line or 'caljpia' in lower_line:
                current_project['topic'] += ' disaster, FEMA'
                current_project['type'] = 'disaster'
            if 'road' in lower_line or 'street' in lower_line:
                current_project['topic'] += ' road'
            if 'park' in lower_line or 'playground' in lower_line:
                current_project['topic'] += ' park'
            if 'storm' in lower_line or 'drain' in lower_line:
                current_project['topic'] += ' storm drain, drainage'
            if 'bridge' in lower_line:
                current_project['topic'] += ' bridge'
            if 'water' in lower_line:
                current_project['topic'] += ' water treatment'
            if 'emergency' in lower_line or 'warning' in lower_line:
                current_project['topic'] += ' emergency warning'
    
    # Add last project
    if current_project:
        projects.append(current_project)
    
    # Clean up topics (remove duplicates)
    for proj in projects:
        if proj['topic']:
            topics = list(set([t.strip() for t in proj['topic'].split(',')]))
            proj['topic'] = ', '.join(topics)
    
    return projects

# Process all documents
for doc in civic_docs:
    projects = extract_projects(doc['text'], doc['filename'])
    projects_data.extend(projects)

# Create projects dataframe
projects_df = pd.DataFrame(projects_data)
print('Extracted projects:', len(projects_df))

# Clean data type issues
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Join with funding data
# First, clean project names for matching
if not projects_df.empty and not funding_df.empty:
    # Filter for disaster-related projects that started in 2022
    disaster_projects = projects_df[
        (projects_df['type'] == 'disaster') & 
        (projects_df['st'].str.contains('2022', na=False))
    ]
    print('Disaster projects starting in 2022:', len(disaster_projects))
    
    # Now match with funding data
    # Create a mapping of project names from documents to funding table
    matched_funding = []
    for _, proj in disaster_projects.iterrows():
        proj_name = proj['Project_Name']
        
        # Look for exact matches first, then partial matches
        matches = funding_df[funding_df['Project_Name'].str.contains(proj_name, case=False, na=False)]
        if matches.empty:
            # Try reverse - look for project name in funding project name
            matches = funding_df[funding_df['Project_Name'].str.contains(proj_name.split()[0], case=False, na=False)]
        
        if not matches.empty:
            for _, match in matches.iterrows():
                matched_funding.append({
                    'Project_Name': proj_name,
                    'Funding_Project_Name': match['Project_Name'],
                    'Funding_Source': match['Funding_Source'],
                    'Amount': match['Amount']
                })
    
    matched_df = pd.DataFrame(matched_funding)
    print('Matched funding records:', len(matched_df))
    if not matched_df.empty:
        total_funding = matched_df['Amount'].sum()
        print('Total funding:', total_funding)
    else:
        print('No matched funding found')
else:
    print('Empty projects or funding dataframe')

__RESULT__: str(len(projects_df))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
