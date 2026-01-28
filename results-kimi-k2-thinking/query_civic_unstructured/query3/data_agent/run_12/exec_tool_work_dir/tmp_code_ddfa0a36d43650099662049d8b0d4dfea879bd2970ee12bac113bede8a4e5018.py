code = """import json
import re

# Load the data properly
civic_docs_path = locals()['var_functions.query_db:10']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:10']

# Load funding data
funding_data = locals()['var_functions.query_db:2']

print('=== DATA LOADED ===')
print(f'Loaded {len(civic_docs)} civic documents')
print(f'Loaded {len(funding_data)} funding records')

# Initialize results
all_projects = []

# Extract projects from civic docs
def extract_projects_from_text(text):
    projects = []
    
    # Look for project patterns
    # Projects often appear as: "Project Name\n(Updates/Status)"
    patterns = [
        r'([A-Z][^.!?\n]{20,100})\n\(cid:\d+\)\s*([Uu]pdates?|[Ss]tatus?):',
        r'([A-Z][^.!?\n]{20,100})\n\(cid:\d+\)\s*([Uu]pdates?|[Ss]tatus?)\s*:\s*([^.!?\n]+)',
        r'([A-Z][^.!?\n]{20,100})\n\(cid:\d+\)\s*([Uu]pdates?)\s*:\s*([^.!?\n]+)',
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.MULTILINE)
        for match in matches:
            project_name = match.group(1).strip()
            if project_name and len(project_name) < 200:
                # Look for status keywords
                if 'design' in text.lower():
                    status = 'design'
                elif 'construction' in text.lower() or 'under construction' in text.lower():
                    status = 'construction'
                elif 'completed' in text.lower():
                    status = 'completed'
                else:
                    status = 'not started'
                
                # Look for FEMA/emergency keywords for topic
                topic = []
                if re.search(r'FEMA', text, re.IGNORECASE):
                    topic.append('FEMA')
                if re.search(r'emergency', text, re.IGNORECASE):
                    topic.append('emergency')
                if re.search(r'fire', text, re.IGNORECASE):
                    topic.append('fire')
                if re.search(r'warning', text, re.IGNORECASE):
                    topic.append('emergency warning')
                if re.search(r'storm drain', text, re.IGNORECASE):
                    topic.append('storm drain')
                if re.search(r'drainage', text, re.IGNORECASE):
                    topic.append('drainage')
                
                projects.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'status': status,
                    'source': 'civic_doc'
                })
    
    return projects

# Process all civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Check if this doc contains emergency/FEMA content
    if re.search(r'emergency|FEMA|fema', text, re.IGNORECASE):
        projects = extract_projects_from_text(text)
        all_projects.extend(projects)

print(f'Extracted {len(all_projects)} potential projects from civic docs')

# Process funding data
funding_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    funding_source = record.get('Funding_Source', '')
    amount = record.get('Amount', 0)
    
    funding_projects.append({
        'Project_Name': project_name,
        'Funding_Source': funding_source,
        'Amount': int(amount) if amount else 0,
        'status': 'unknown'
    })

print(f'Loaded {len(funding_projects)} funding records')
print('=== PROCESSING COMPLETE ===')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
