code = """import json, re

# Load data from file path in storage
file_path = globals()['var_functions.query_db:2']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(civic_docs)} documents')

# Simple extraction function
def extract_projects(text, filename):
    projects = []
    # Look for patterns indicating projects with emergency/FEMA context
    patterns = [
        r'([A-Z][^.]*?(?:Project|Road|Park|Bridge|Facility|System|Plan)[^.]*?)(?=\n\s*(?:Updates|Project Schedule|Construction|Design|Status))',
    ]
    
    # Also look for specific FEMA/emergency mentions
    if 'FEMA' in text or 'emergency' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line and len(line) < 100:
                # Check if this line looks like a project name and has context
                next_chunk = ' '.join(lines[i:i+10])
                if (('Project' in line or 'Road' in line or 'Park' in line) and 
                    ('Updates:' in next_chunk or 'Project Schedule:' in next_chunk)):
                    
                    # Determine type and status
                    proj_type = 'disaster' if 'FEMA' in text else 'capital'
                    status = 'design'
                    if 'completed' in next_chunk.lower():
                        status = 'completed'
                    elif 'construction' in next_chunk.lower():
                        status = 'construction'
                    
                    # Extract topics
                    topics = []
                    low_text = text.lower()
                    if 'emergency' in low_text:
                        topics.append('emergency')
                    if 'FEMA' in text:
                        topics.append('FEMA')
                    if 'fire' in low_text:
                        topics.append('fire')
                    
                    if topics:
                        projects.append({
                            'Project_Name': line,
                            'topic': ', '.join(topics),
                            'type': proj_type,
                            'status': status,
                            'source_file': filename
                        })
    return projects

all_projects = []
for doc in civic_docs:
    if isinstance(doc, dict) and 'text' in doc:
        projects = extract_projects(doc['text'], doc.get('filename', ''))
        all_projects.extend(projects)

# Deduplicate
seen = set()
unique_projects = []
for proj in all_projects:
    key = proj['Project_Name']
    if key not in seen:
        seen.add(key)
        unique_projects.append(proj)

print(f'Found {len(unique_projects)} unique projects')

result = {'projects': unique_projects, 'count': len(unique_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.execute_python:16': {'test': 'data'}, 'var_functions.query_db:18': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
