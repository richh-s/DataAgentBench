code = """# Load both datasets
import json
civic_docs_path = 'var_functions.query_db:2'
funding_path = 'var_functions.query_db:5'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_data)))

# Identify FEMA/emergency funding records
fema_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '').lower()
    if 'fema' in name or 'emergency' in name:
        fema_projects.append(rec)

print('Found %d FEMA/emergency projects' % len(fema_projects))

# Extract project status from civic documents
def find_status(text, project_name):
    # Look for the project and nearby status indicators
    text_lower = text.lower()
    proj_lower = project_name.lower()
    
    # Check if project mentioned
    if proj_lower not in text_lower:
        return 'Unknown'
    
    # Check for status indicators around the project mention
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if proj_lower in line.lower():
            # Check next few lines
            context = '\n'.join(lines[i:min(len(lines), i+15)]).lower()
            
            if 'construction was completed' in context:
                return 'completed'
            elif 'under construction' in context:
                return 'construction'
            elif 'complete design' in context or 'finalize design' in context or 'awaiting' in context:
                return 'design'
            elif 'not started' in context:
                return 'not started'
    
    return 'Unknown'

# Build results
final_results = []

for project in fema_projects:
    proj_name = project['Project_Name']
    status = 'Unknown'
    
    # Try to find status in each civic document
    for doc in civic_docs:
        found_status = find_status(doc.get('text', ''), proj_name)
        if found_status != 'Unknown':
            status = found_status
            break
    
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': status,
        'Type': 'disaster'
    })

# Output in required format
import json as js
print('__RESULT__:')
print(js.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'relevant_funding': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'civic_docs_count': 5}}

exec(code, env_args)
