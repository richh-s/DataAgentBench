code = """import json
import re

# Access the stored civic documents data
civic_docs_key = 'var_functions.query_db:0'
civic_docs_file = locals()[civic_docs_key]

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Access funding data
funding_data = locals()['var_functions.query_db:2']

print(f'Total civic documents: {len(civic_docs)}')
print(f'Total funding records: {len(funding_data)}')

# Initialize list to store extracted projects
extracted_projects = []

# Process each document
doc_count = 0
for doc in civic_docs:
    doc_count += 1
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Pattern 1: Project Name followed by status info
    # Pattern 2: Lines that look like project names
    
    # Find project names that appear to have dates
    lines = text.split('\n')
    
    for line in lines:
        # Look for project names and dates
        # Patterns like: "Project Name" followed by date info
        
        # Check if line looks like a project name (title case, reasonable length)
        if len(line.strip()) > 10 and not line.strip().startswith('('):
            line_clean = line.strip()
            
            # Check if this line or nearby lines contain date information
            if any(keyword in text for keyword in ['Spring 2022', '2022-Spring', '2022-March', '2022-April', '2022-May']):
                # This is a candidate project
                project_info = {
                    'project_name': line_clean,
                    'source_file': filename,
                    'start_time': '2022-Spring'  # Placeholder
                }
                extracted_projects.append(project_info)
                break  # Only take first match per document for now

print(f'Found {len(extracted_projects)} potential projects')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
