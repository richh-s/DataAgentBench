code = """import json
import re

# Load the MongoDB documents
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

print('Loaded', len(docs), 'documents')

# Function to extract projects with Spring 2022 start dates
def extract_spring_2022_projects(text, filename):
    projects = []
    text_lower = text.lower()
    
    # Look for Spring 2022 indicators in the text
    spring_2022_indicators = [
        'spring 2022',
        '2022-spring',
        'march 2022',
        '2022-march',
        'april 2022', 
        '2022-april',
        'may 2022',
        '2022-may'
    ]
    
    # Check if any spring 2022 indicator is in the text
    has_spring_2022 = any(indicator in text_lower for indicator in spring_2022_indicators)
    
    if not has_spring_2022:
        return projects
    
    # Split text into sections to find individual projects
    # Look for common project name patterns
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip headers and bullet points
        skip_patterns = [
            'public works', 'agenda', 'item', 'to:', 'prepared', 'approved',
            'date', 'meeting', 'subject:', 'recommended', 'discussion:',
            'updates:', 'project schedule:', 'complete design:', 'advertise:',
            'begin construction:', 'page', '•', '-', '□', '●', '○'
        ]
        
        should_skip = any(pattern in line.lower() for pattern in skip_patterns)
        if should_skip:
            continue
            
        # Lines with capitalized words and reasonable length might be project names
        if len(line) > 10 and len(line) < 100:
            has_capitals = any(c.isupper() for c in line)
            if has_capitals:
                # Check if project name is followed by spring 2022 schedule
                subsequent_text = '\n'.join(lines[i:min(i+10, len(lines))])
                subsequent_lower = subsequent_text.lower()
                
                if any(indicator in subsequent_lower for indicator in spring_2022_indicators):
                    projects.append({
                        'project_name': line,
                        'filename': filename
                    })
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in docs:
    projects = extract_spring_2022_projects(doc.get('text', ''), doc.get('filename', ''))
    all_projects.extend(projects)

print('Found', len(all_projects), 'potential Spring 2022 projects')

# Remove duplicates based on project name and filename
unique_projects = []
seen = set()
for proj in all_projects:
    key = (proj['project_name'], proj['filename'])
    if key not in seen:
        seen.add(key)
        unique_projects.append(proj)

print('Unique projects:', len(unique_projects))
for proj in unique_projects[:10]:  # Show first 10
    print('Project:', proj['project_name'], 'in', proj['filename'])

result = {
    'spring_2022_projects': unique_projects,
    'count': len(unique_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
