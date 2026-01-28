code = """import json
import re
import pandas as pd

# Load both datasets
with open('file_storage/functions.query_db:6.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:10.json', 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract all project information with dates from civic documents
all_projects = []

for doc in civic_docs:
    text = doc['text']
    # Look for project names and their schedule information
    # Pattern to capture project names and nearby schedule info
    
    # First, find all potential project names
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip headers and irrelevant lines  
        skip_patterns = ['Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']
        if any(pattern in line for pattern in skip_patterns) or line.isupper():
            continue
        
        # Look for lines that might be project names
        # Usually title case, sometimes starting with year
        project_name = None
        
        # Pattern 1: Starts with year (e.g., "2022 Morning View Resurfacing")
        year_match = re.match(r'(\d{4})\s+([A-Z][a-zA-Z\s&\-]+)', line)
        if year_match and len(line) > 15:
            project_name = line
        
        # Pattern 2: Has FEMA/CalOES suffix
        elif re.search(r'\((FEMA|CalOES|CalJPIA)\s+[^)]+\)$', line) and len(line) > 15:
            project_name = line
        
        # Pattern 3: Title case descriptive names (filter out short lines and common phrases)
        elif (len(line) > 15 and 
              not line.isupper() and 
              re.match(r'^[A-Z][a-zA-Z\s&\-/]+$', line) and
              'Project' not in line.split()[:1] and  # Don't start with "Project"
              len(line.split()) > 2):  # At least 3 words
            project_name = line
        
        if project_name:
            # Look ahead for schedule info
            start_date = ''
            for j in range(i+1, min(i+8, len(lines))):
                next_line = lines[j].strip()
                
                # Look for schedule patterns
                schedule_match = re.search(r'(Begin|Complete|Advertise|Construction):\s*(Spring|Summer|Fall|Winter)\s*(\d{4})', next_line, re.IGNORECASE)
                if schedule_match:
                    action, season, year = schedule_match.groups()
                    date_str = f"{year}-{season}"
                    if 'Begin' in action or 'Complete Design' in next_line:
                        start_date = date_str
                        break
            
            # Also check for "2022-Spring" format
            direct_date_match = re.search(r'(\d{4})-(Spring|Summer|Fall|Winter)', line, re.IGNORECASE)
            if direct_date_match:
                start_date = f"{direct_date_match.group(1)}-{direct_date_match.group(2)}"
            
            if start_date and '2022-Spring' in start_date:
                all_projects.append({
                    'Project_Name': project_name,
                    'start_date': start_date,
                    'doc_id': doc['_id'],
                    'filename': doc['filename']
                })

projects_df = pd.DataFrame(all_projects)

print('__RESULT__:')
print(json.dumps({
    "spring_2022_projects": len(projects_df),
    "project_names": projects_df['Project_Name'].tolist(),
    "unique_projects": len(projects_df['Project_Name'].unique())
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_docs_count': 5, 'total_funding_amount': 28094000, 'sample_project_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}}

exec(code, env_args)
