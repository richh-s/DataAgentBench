code = """import json
import re

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:24']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = locals()['var_functions.query_db:2']

print(f'Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records')

# Initialize data structures
spring_2022_projects = set()  # Use set to avoid duplicates
total_funding = 0
project_funding_details = []

# Define spring 2022 date patterns
date_patterns = [
    r'2022-Spring',
    r'Spring 2022',
    r'2022-March',
    r'2022-April', 
    r'2022-May',
    r'March 2022',
    r'April 2022',
    r'May 2022'
]

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Check if document contains spring 2022 dates
    found_spring_2022 = any(pattern in text for pattern in date_patterns)
    
    if found_spring_2022:
        lines = text.split('\n')
        current_project = None
        
        for i, line in enumerate(lines):
            line_clean = line.strip()
            
            # Skip empty lines and metadata
            if not line_clean or len(line_clean) < 5:
                continue
                
            # Skip header/footer lines
            skip_indicators = ['Page ', 'Agenda Item', 'To:', 'From:', 'Subject:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'RECOMMENDED ACTION:']
            if any(indicator in line_clean for indicator in skip_indicators):
                continue
            
            # Detect project names (heuristic: capitalized, reasonable length, ends without punctuation or has project-like words)
            if line_clean[0].isupper() and len(line_clean) > 8:
                # Check if line looks like a project name (doesn't end in sentence punctuation)
                if not line_clean.endswith(('.', '!', '?', ':')):
                    current_project = line_clean
                # Also check if next few lines contain spring 2022 dates
                elif 'Project' in line_clean or 'Improvements' in line_clean or 'Repair' in line_clean:
                    current_project = line_clean
            
            # Check for spring 2022 dates in current and surrounding lines
            if current_project:
                # Look ahead for date information
                look_ahead = 10
                context_lines = lines[i:i+look_ahead] if i+look_ahead <= len(lines) else lines[i:]
                context_text = ' '.join(context_lines)
                
                if any(pattern in context_text for pattern in date_patterns):
                    # Found a spring 2022 project
                    spring_2022_projects.add(current_project)
                    
                    # Find funding for this project
                    for fund in funding_data:
                        if fund['Project_Name'] == current_project:
                            amount = int(fund['Amount'])
                            total_funding += amount
                            project_funding_details.append({
                                'project_name': current_project,
                                'funding_id': fund['Funding_ID'],
                                'amount': amount,
                                'source': fund['Funding_Source']
                            })
                    
                    current_project = None  # Reset after finding a match

print(f'Found {len(spring_2022_projects)} unique Spring 2022 projects')
print(f'Total funding identified: ${total_funding:,}')

# Prepare result
result = {
    'number_of_projects': len(spring_2022_projects),
    'total_funding': total_funding,
    'project_names': list(spring_2022_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:18': {'documents_with_spring_2022': 5, 'sample_filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
