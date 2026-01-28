code = """import json
import re
from pathlib import Path

# Load the data
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:3']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Create a dictionary for quick lookup of funding amounts by project name
funding_dict = {item['Project_Name'].upper(): int(item['Amount']) for item in funding_data}

print(f"Loaded {len(funding_data)} funding records and {len(civic_data)} civic documents")

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    
    # Common project patterns in these documents
    # Look for lines that start with project names followed by updates
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a project name (usually bolded or capitalized)
        # Pattern: project name followed by line with updates/schedule
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('Page'):
            # Check if it's likely a project name (contains keywords)
            project_keywords = ['Park', 'Road', 'Drain', 'Bridge', 'Canyon', 'Beach', 'Street', 'Traffic', 'Signal', 'Siren', 'Warning']
            if any(keyword in line for keyword in project_keywords):
                # Potential project name
                if current_project:
                    # Save the previous project
                    projects.append(project_info)
                
                current_project = line
                project_info = {
                    'Project_Name': line,
                    'topics': [],
                    'status': None,
                    'dates': []
                }
                
                # Determine topics based on keywords
                if 'Park' in line or 'park' in line:
                    project_info['topics'].append('park')
                if 'Road' in line or 'road' in line or 'Street' in line:
                    project_info['topics'].append('road')
                if 'Drain' in line or 'drain' in line or 'Drainage' in line:
                    project_info['topics'].append('drainage')
                if 'Siren' in line or 'Warning' in line:
                    project_info['topics'].append('emergency warning')
                if 'FEMA' in line:
                    project_info['topics'].append('FEMA')
                
        # Look for status and dates
        if current_project:
            if 'completed' in line.lower() or 'construction was completed' in line.lower():
                project_info['status'] = 'completed'
                
                # Look for year in the line
                year_match = re.search(r'(202[0-3])', line)
                if year_match:
                    project_info['dates'].append(year_match.group(1))
            
            # Also check for year in schedule/updates
            year_match = re.search(r'(202[0-3])', line)
            if year_match:
                project_info['dates'].append(year_match.group(1))
    
    # Add the last project
    if current_project and project_info:
        projects.append(project_info)
    
    return projects

# Extract all projects from all documents
all_extracted_projects = []

doc_count = 0
for doc in civic_data:
    text = doc.get('text', '')
    if text:
        projects = extract_projects_from_text(text)
        all_extracted_projects.extend(projects)
        doc_count += 1

print(f"Extracted projects from {doc_count} documents")
print(f"Total extracted projects: {len(all_extracted_projects)}")

# Filter for park-related projects completed in 2022
park_completed_2022 = []

for project in all_extracted_projects:
    is_park = 'park' in project['topics']
    is_completed = project['status'] == 'completed'
    in_2022 = '2022' in project['dates']
    
    if is_park and is_completed and in_2022:
        park_completed_2022.append(project)

print(f"\nPark-related projects completed in 2022: {len(park_completed_2022)}")
for p in park_completed_2022:
    print(f"- {p['Project_Name']}")

# Now match with funding data and sum amounts
total_funding = 0
matched_projects = []

for project in park_completed_2022:
    proj_name = project['Project_Name']
    # Try exact match first, then fuzzy matching
    
    # Direct match
    if proj_name.upper() in funding_dict:
        amount = funding_dict[proj_name.upper()]
        total_funding += amount
        matched_projects.append({
            'project_name': proj_name,
            'amount': amount
        })
    else:
        # Try partial matching - look for projects containing the name
        for funded_name, amount in funding_dict.items():
            if proj_name.upper() in funded_name or funded_name in proj_name.upper():
                total_funding += amount
                matched_projects.append({
                    'project_name': proj_name,
                    'matched_funding_name': funded_name,
                    'amount': amount
                })
                break

print(f"\nMatched {len(matched_projects)} projects with funding data")
print(f"Total funding: ${total_funding:,}")

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'park_completed_2022_count': len(park_completed_2022)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': {'funding_count': 500, 'civic_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'civic_sample': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n10-27-21\nItem\n4.A.\n\nTo:\n\nChair Simmens and Members of the Public Works Commission\n\nPrepared by:\n\nTroy Spayd, Assistant Public Wor'}]}}

exec(code, env_args)
