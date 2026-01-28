code = """import json
import re

# Load the data
civic_docs_path = locals()['var_functions.query_db:8']
funding_path = locals()['var_functions.query_db:0']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

def is_disaster_project(project_name, text_context):
    """Check if a project is disaster-related based on name and context"""
    # Check for FEMA/CalJPIA/CalOES project markers in name
    if any(marker in project_name for marker in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']):
        return True
    
    # Check for disaster-related keywords in project name
    disaster_keywords = ['FEMA', 'fire', 'emergency', 'recovery', 'disaster', 'CalOES', 'CalJPIA']
    if any(keyword.lower() in project_name.lower() for keyword in disaster_keywords):
        return True
    
    return False

def project_started_in_2022(project_name, text_context):
    """Check if project started in 2022 based on st field or mentions in text"""
    # Look for 2022 in the text near the project name
    pattern = rf"{re.escape(project_name)}.*?2022"
    if re.search(pattern, text_context, re.IGNORECASE | re.DOTALL):
        return True
    
    # Look for project lines starting with 2022
    if project_name.startswith('2022 '):
        return True
    
    # General 2022 mentions with disaster/recovery context
    if '2022' in text_context and ('disaster' in text_context.lower() or 'fema' in text_context.lower()):
        return True
    
    return False

# Extract disaster projects with 2022 start
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project patterns in text
    # Common format: project name followed by updates and schedule
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        # Skip empty lines and markers
        if not line or line.startswith('(') or line.startswith('Page'):
            continue
        
        # Look for project names (typically bolded/uppercase or start with year)
        if (len(line) > 10 and 
            not line.startswith('cid:') and 
            not line.lower().startswith('and ') and
            not line.lower().startswith('or ') and
            not line.lower().startswith('to ') and
            not any(keyword in line.lower() for keyword in ['project schedule', 'updates', 'description'])):
            
            # Check if this looks like a project name
            has_noun = any(word in line.lower() for word in ['road', 'avenue', 'street', 'drain', 'park', 'bridge', 'culvert', 'siren', 'warning'])
            has_action = any(word in line.lower() for word in ['repair', 'improvement', 'replacement', 'project', 'maintenance', 'construction'])
            
            if has_noun or has_action:
                current_project = line.strip()
                
                # Check if it's a disaster project
                if is_disaster_project(current_project, text):
                    # Check if started in 2022
                    if project_started_in_2022(current_project, text):
                        extracted_projects.append({
                            'Project_Name': current_project,
                            'type': 'disaster',
                            'st': '2022',
                            'status': 'inferred',
                            'topic': 'FEMA,disaster,recovery'
                        })

# Also look for FEMA projects in funding data directly
disaster_funding_names = []
for record in funding_data:
    name = record['Project_Name']
    if is_disaster_project(name, '') and not name.startswith('Discussion'):
        disaster_funding_names.append(name)

# Now find which disaster projects started in 2022 based on civic docs
projects_to_fund = []
seen_names = set()

for proj in extracted_projects:
    proj_name = proj['Project_Name']
    # Normalize for matching
    base_name = proj_name.split('(')[0].strip()
    
    # Find matching funding records
    for fund_record in funding_data:
        fund_name = fund_record['Project_Name']
        
        # Check for direct name match or base name match
        if (fund_name.startswith(proj_name[:30]) or 
            proj_name.startswith(fund_name[:30]) or
            base_name and fund_name.startswith(base_name)):
            
            if fund_name not in seen_names:
                projects_to_fund.append(fund_record)
                seen_names.add(fund_name)

# Calculate total funding
total_funding = sum(record['Amount'] for record in projects_to_fund)

print('__RESULT__:')
print(json.dumps({
    'extracted_disaster_2022_projects': len(extracted_projects),
    'matched_funding_records': len(projects_to_fund),
    'total_funding_2022_disaster': total_funding,
    'sample_projects': extracted_projects[:10],
    'sample_funding': projects_to_fund[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records_count': 500, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
