code = """import json
import re

# Load civic documents and funding data
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:6']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integers
for rec in funding_data:
    rec['Amount'] = int(rec['Amount'])

# Function to extract structured project information from text
def extract_projects(text):
    """Extract project information from civic document text"""
    projects = []
    lines = text.split('\n')
    
    # Look for project patterns
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('Public Works') or line.startswith('Commission') or \
           line.startswith('Agenda') or line.startswith('To:') or line.startswith('Prepared by') or \
           line.startswith('Approved by') or line.startswith('Date') or line.startswith('Meeting date') or \
           line.startswith('Subject:') or line.startswith('RECOMMENDED ACTION') or line.startswith('DISCUSSION'):
            i += 1
            continue
        
        # Look for project name (typically a title case line)
        if (line and len(line) < 150 and 
            (line.istitle() or any(keyword in line.lower() for keyword in 
             ['project', 'improvements', 'repairs', 'replacement', 'drainage', 'resurfacing']))):
            
            project_name = line
            project_info = {
                'name': project_name,
                'text': '',
                'status': None,
                'et': None,  # end time
                'topic': []
            }
            
            # Collect project description (next few lines)
            desc_lines = []
            j = i + 1
            while j < len(lines) and j < i + 20:
                next_line = lines[j].strip()
                if next_line and len(next_line) > 5:
                    desc_lines.append(next_line)
                j += 1
            
            project_info['text'] = ' '.join(desc_lines)
            
            # Check status
            text_lower = project_info['text'].lower()
            if 'completed' in text_lower:
                project_info['status'] = 'completed'
            elif 'design' in text_lower or 'planning' in text_lower:
                project_info['status'] = 'design'
            elif 'not started' in text_lower:
                project_info['status'] = 'not started'
            
            # Check for end date/year
            if '2022' in project_info['text']:
                project_info['et'] = '2022'
            elif '2023' in project_info['text']:
                project_info['et'] = '2023'
            elif '2024' in project_info['text']:
                project_info['et'] = '2024'
            
            # Determine topic based on keywords
            topic_keywords = {
                'park': ['park', 'playground', 'bluffs', 'walkway', 'recreation', 'skate'],
                'road': ['road', 'street', 'highway', 'intersection'],
                'drainage': ['drainage', 'storm drain', 'stormwater'],
                'bridge': ['bridge', 'culvert'],
                'FEMA': ['fema', 'disaster', 'caloes', 'caljpia'],
                'emergency': ['emergency', 'warning', 'siren'],
                'fire': ['fire', 'woolsey']
            }
            
            for topic, keywords in topic_keywords.items():
                if any(keyword in text_lower for keyword in keywords):
                    project_info['topic'].append(topic)
            
            projects.append(project_info)
            i = j
        else:
            i += 1
    
    return projects

# Extract all projects from all documents
all_extracted_projects = []
for doc in civic_docs:
    projects = extract_projects(doc['text'])
    for project in projects:
        project['doc_id'] = doc['_id']
        project['filename'] = doc['filename']
        all_extracted_projects.append(project)

# Find park-related projects completed in 2022
park_projects_2022 = [
    p for p in all_extracted_projects 
    if 'park' in p['topic'] and p['status'] == 'completed' and p['et'] == '2022'
]

# Match with funding data
matched_funding = []
for park_project in park_projects_2022:
    project_name = park_project['name']
    project_name_lower = project_name.lower()
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_name_lower = fund_name.lower()
        
        # Check if names match (one contains the other)
        if (project_name_lower in fund_name_lower or fund_name_lower in project_name_lower):
            matched_funding.append({
                'project_name': project_name,
                'funding_record_name': fund_name,
                'amount': fund['Amount'],
                'funding_source': fund['Funding_Source']
            })
            break  # Assume first match is correct

# Calculate total funding
total_funding = sum(f['amount'] for f in matched_funding)

# Prepare results
result = {
    'total_funding_2022_park_projects': total_funding,
    'number_of_projects': len(matched_funding),
    'projects': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}, 'var_functions.execute_python:44': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}}

exec(code, env_args)
