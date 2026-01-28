code = """import json
import re

funding_path = locals()['var_functions.query_db:10']
docs_path = locals()['var_functions.query_db:2']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Convert amounts to integers
for record in funding_records:
    record['Amount'] = int(record['Amount'])

# Function to extract disaster projects starting in 2022
def extract_disaster_projects_2022(text):
    disaster_projects = []
    
    # Look for disaster project indicators
    disaster_indicators = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']
    
    # Check each line for project names with disaster indicators
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check if line contains disaster project indicators
        has_disaster_indicator = any(indicator in line for indicator in disaster_indicators)
        
        if has_disaster_indicator:
            # Extract project name (usually on same line or previous line)
            project_name = line
            
            # Look for date patterns mentioning 2022 in surrounding lines
            start_date = None
            for j in range(max(0, i-5), min(len(lines), i+10)):
                context_line = lines[j].strip()
                
                # Check for 2022 in the line
                if '2022' in context_line:
                    # If it's about beginning/advertising, it's a start date
                    if any(word in context_line.lower() for word in ['begin', 'start', 'advertise', 'complete design', 'spring 2022', 'summer 2022', 'fall 2022', 'winter 2022']):
                        start_date = context_line
                        break
            
            if start_date:
                disaster_projects.append({
                    'name': project_name,
                    'start_date': start_date,
                    'year': '2022'
                })
    
    return disaster_projects

# Extract disaster projects from all documents
disaster_projects_2022 = []
for doc in civic_docs:
    projects = extract_disaster_projects_2022(doc['text'])
    disaster_projects_2022.extend(projects)

# Show what we found
sample = disaster_projects_2022[:20]
print('__RESULT__:')
print(json.dumps({
    'found_disaster_projects_2022': len(disaster_projects_2022),
    'sample_projects': sample
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
