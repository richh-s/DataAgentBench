code = """import json
import re
from collections import defaultdict

# Load both datasets
funding_data = locals()['var_functions.query_db:6']
documents_path = locals()['var_functions.query_db:0']

with open(documents_path, 'r') as f:
    documents = json.load(f)

print('__RESULT__:')

# First, let's collect all project names from funding data that are related to FEMA/emergency
fema_projects = [f['Project_Name'] for f in funding_data]
funding_dict = {f['Project_Name']: f for f in funding_data}

print(f"Found {len(fema_projects)} FEMA/emergency projects in funding database")

# Now parse documents to find project information
# Pattern to match project names (typically start with a year, or are title case)
project_patterns = [
    r'^[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+',  # e.g., "Morning View Resurfacing"
    r'^\d{4} [A-Z][a-z]+',  # e.g., "2022 Morning View"
    r'^[A-Z][a-z]+ [A-Z][a-z]+',  # e.g., "Malibu Bluffs", "PCH Median"
    r'^[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+',  # e.g., "Clover Heights Storm"
    r'^[A-Z/]+',  # e.g., "PCH", "FEMA"
]

status_keywords = ['design', 'completed', 'not started', 'construction', 'under construction']
type_keywords = ['capital', 'disaster', 'fema']
topic_keywords = ['emergency', 'fema', 'fire', 'warning', 'drainage', 'storm drain', 'road', 'bridge', 'park']

# Extract project information from documents
extracted_projects = []

for doc in documents:
    text = doc['text'].lower()
    
    # Split by lines to find project headings
    lines = doc['text'].split('\n')
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        # Look for project names (typically capitalized, not bullet points)
        if (line_stripped and 
            line_stripped[0].isupper() and 
            not line_stripped.startswith('(') and
            not line_stripped.startswith('•') and
            not line_stripped.startswith('-') and
            not line_stripped.startswith('Page') and
            not line_stripped.startswith('Agenda') and
            len(line_stripped) > 10 and
            len(line_stripped.split()) >= 2):
            
            # Check if this line looks like a project name
            is_project = False
            
            # Check if it matches known project names from funding
            for proj_name in fema_projects:
                clean_name = proj_name.replace('(FEMA Project)', '').replace('(FEMA)', '').replace('(CalOES Project)', '').replace('(CalJPIA/FEMA Project)', '').strip()
                if clean_name and clean_name.lower() in line_stripped.lower():
                    is_project = True
                    project_name = proj_name
                    break
            
            if is_project:
                # Extract status from nearby lines
                status = None
                for j in range(max(0, i-5), min(len(lines), i+10)):
                    nearby_line = lines[j].lower()
                    if 'design' in nearby_line or 'complete design' in nearby_line:
                        status = 'design'
                        break
                    elif 'complete' in nearby_line and 'construction' in nearby_line:
                        status = 'completed'
                        break
                    elif 'not started' in nearby_line:
                        status = 'not started'
                        break
                    elif 'construction' in nearby_line or 'under construction' in nearby_line:
                        status = 'construction'
                        break
                
                # Determine type
                type_val = 'disaster' if '(FEMA' in project_name or '(FEMA' in line else 'capital'
                
                # Extract topics
                topics = []
                for topic in topic_keywords:
                    if topic in line_stripped.lower() or topic in ' '.join(lines[max(0,i-3):i+5]).lower():
                        topics.append(topic)
                
                extracted_projects.append({
                    'project_name': project_name,
                    'status': status or 'unknown',
                    'type': type_val,
                    'topics': topics,
                    'source_file': doc['filename']
                })

# Filter for projects that have funding data
matched_projects = []
for proj in extracted_projects:
    for funding_proj, funding_info in funding_dict.items():
        clean_funding_name = funding_proj.replace('(FEMA Project)', '').replace('(FEMA)', '').replace('(CalOES Project)', '').replace('(CalJPIA/FEMA Project)', '').strip()
        clean_project_name = proj['project_name'].replace('(FEMA Project)', '').replace('(FEMA)', '').replace('(CalOES Project)', '').replace('(CalJPIA/FEMA Project)', '').strip()
        
        if clean_funding_name.lower() in clean_project_name.lower() or clean_project_name.lower() in clean_funding_name.lower():
            matched_projects.append({
                'project_name': funding_proj,
                'funding_source': funding_info['Funding_Source'],
                'amount': funding_info['Amount'],
                'status': proj['status'],
                'type': proj['type'],
                'source_file': proj['source_file']
            })

# Also add projects that are in funding but not found in documents
missing_from_docs = []
found_proj_names = [p['project_name'] for p in matched_projects]

for funding_proj, funding_info in funding_dict.items():
    if funding_proj not in found_proj_names:
        # Check if topic is in funding project name
        topics = []
        if 'emergency' in funding_proj.lower():
            topics.append('emergency')
        if 'fema' in funding_proj.lower():
            topics.append('fema')
        if 'storm' in funding_proj.lower() or 'drainage' in funding_proj.lower():
            topics.append('drainage')
        
        missing_from_docs.append({
            'project_name': funding_proj,
            'funding_source': funding_info['Funding_Source'],
            'amount': funding_info['Amount'],
            'status': 'unknown',
            'type': 'disaster' if '(FEMA' in funding_proj else 'unknown',
            'source_file': 'not found in documents'
        })

all_projects = matched_projects + missing_from_docs

# Format output
output = []
for proj in all_projects:
    output.append({
        'project_name': proj['project_name'],
        'funding_source': proj['funding_source'],
        'amount': f"${int(proj['amount']):,}" if proj['amount'] else '$0',
        'status': proj['status'],
        'type': proj['type']
    })

print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'message': 'Found 5 documents', 'first_doc_keys': ['_id', 'filename', 'text'], 'text_sample_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'emergency_count': 2, 'fema_count': 5, 'total_docs': 5}, 'var_functions.query_db:6': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
