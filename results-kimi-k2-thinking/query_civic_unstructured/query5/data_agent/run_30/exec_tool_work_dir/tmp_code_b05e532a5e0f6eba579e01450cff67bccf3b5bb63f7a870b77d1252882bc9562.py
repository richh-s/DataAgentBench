code = """import json
import pandas as pd
import re
import os

# Load funding data
funding_file = locals()['var_functions.query_db:10']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents data
civic_file = locals()['var_functions.query_db:6']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Initialize extraction results
extracted_projects = []

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Skip empty documents
    if not text:
        continue
    
    # Look for project sections that start with project names
    # Common patterns in the documents
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Detect project names (typically capitalized, no bullet points, followed by Project Schedule or Updates)
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('ï¿½') and
            not line.startswith('ï¿½') and
            not line.startswith('Page') and
            not line.startswith('Agenda') and
            'To:' not in line and
            'Prepared by:' not in line and
            'Approved by:' not in line and
            'Date prepared:' not in line and
            'Meeting date:' not in line and
            'Subject:' not in line and
            'RECOMMENDED ACTION:' not in line and
            'DISCUSSION:' not in line and
            'Capital Improvement Projects' not in line and
            'Disaster Recovery Projects' not in line and
            'project is delayed' not in line.lower() and
            'staff has also' not in line.lower()):
            
            # Check if this looks like a project name (reasonable length, not a heading)
            if 10 < len(line) < 150:
                # Save previous project if exists
                if current_project and project_info:
                    project_info['Project_Name'] = current_project
                    project_info['Source_File'] = filename
                    extracted_projects.append(project_info.copy())
                
                # Start new project
                current_project = line
                project_info = {'Project_Name': line, 'Source_File': filename}
        
        # Extract dates and other info from project details
        if current_project:
            # Check for start dates
            if any(keyword in line.lower() for keyword in ['complete design:', 'begin construction:', 'advertise:', 'final design:']):
                if '2022' in line:
                    project_info['st'] = '2022'
            
            # Check for disaster-related keywords
            if any(keyword in line.lower() for keyword in ['fema', 'emergency', 'fire', 'disaster', 'caloes', 'caljpia']):
                project_info['is_disaster'] = True
            
            # Check for project type hints
            if 'fema' in line.lower():
                project_info['type'] = 'disaster'
            elif any(keyword in line.lower() for keyword in ['storm drain', 'road', 'pavement', 'bridge', 'park', 'median']):
                project_info['is_infrastructure'] = True
    
    # Add the last project if exists
    if current_project and project_info:
        project_info['Project_Name'] = current_project
        project_info['Source_File'] = filename
        extracted_projects.append(project_info.copy())

# Clean extracted projects
unique_projects = {}
for proj in extracted_projects:
    name = proj.get('Project_Name', '')
    if name and len(name) > 10:
        # Normalize name
        clean_name = name.strip()
        if clean_name not in unique_projects:
            unique_projects[clean_name] = proj

# Mark disaster projects based on name patterns
final_projects = []
for name, proj in unique_projects.items():
    proj_info = proj.copy()
    
    # Auto-detect disaster projects from names
    name_lower = name.lower()
    if any(keyword in name_lower for keyword in ['(fema', '(caloes', '(caljpia', 'emergency', 'fire']):
        proj_info['is_disaster'] = True
        proj_info['type'] = 'disaster'
    
    final_projects.append(proj_info)

# Find disaster projects that started in 2022
disaster_2022_projects = []

for proj in final_projects:
    # Check if marked as disaster type
    is_disaster = proj.get('is_disaster', False) or proj.get('type') == 'disaster'
    
    # Check if has 2022 start date or should check in text
    started_2022 = proj.get('st') == '2022' or '2022' in proj.get('Source_File', '')
    
    if is_disaster and started_2022:
        disaster_2022_projects.append(proj.get('Project_Name'))

# Get funding amounts for these projects
total_funding = 0
funding_matches = []

for funding in funding_records:
    fund_name = funding.get('Project_Name', '').lower()
    fund_amount = float(funding.get('Amount', 0))
    
    for project_name in disaster_2022_projects:
        proj_name_lower = project_name.lower()
        
        # Check for exact match or partial match
        if fund_name == proj_name_lower or fund_name in proj_name_lower or proj_name_lower in fund_name:
            total_funding += fund_amount
            funding_matches.append({
                'project': project_name,
                'funding_name': funding.get('Project_Name'),
                'amount': fund_amount
            })

result_dict = {
    'total_disaster_2022_funding': total_funding,
    'disaster_2022_projects_count': len(disaster_2022_projects),
    'matching_funding_records': len(funding_matches)
}

result_str = json.dumps(result_dict)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'civic_docs_count': 5}}

exec(code, env_args)
