code = """import json
import re

# Read the civic docs data from the stored file
civic_docs_file = locals()['var_functions.query_db:0']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data from the stored file
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract project information from civic docs
projects = []

disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery', 'Woolsey']

for doc in civic_docs:
    text = doc.get('text', '').lower()
    original_text = doc.get('text', '')
    
    # Check for 2022 in the document
    has_2022 = '2022' in original_text
    
    # Look for project sections
    lines = original_text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 10 and len(line) < 80 and not line.startswith('(') and not line.startswith('•'):
            # Potential project name
            if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 'replacement']):
                current_project = line
                
                # Check if it's a disaster project
                is_disaster = False
                if any(indicator in original_text for indicator in disaster_indicators):
                    is_disaster = True
                
                # Check if it started in 2022
                started_2022 = False
                if '2022' in original_text:
                    # Look for start/completion dates
                    schedule_section = ''
                    if 'Project Schedule' in original_text:
                        schedule_start = original_text.find('Project Schedule')
                        schedule_section = original_text[schedule_start:schedule_start+500]
                    
                    if re.search(r'(2022).*(start|begin|complete|advertise)', original_text, re.IGNORECASE) or \
                       re.search(r'(start|begin|complete|advertise).*(2022)', original_text, re.IGNORECASE):
                        started_2022 = True
                
                if is_disaster and started_2022 and current_project:
                    projects.append({
                        'project_name': current_project,
                        'type': 'disaster',
                        'start_2022': True
                    })

# Create a set of disaster-related base project names
disaster_base_names = set()
for p in projects:
    name = p['project_name']
    # Clean up the name
    clean_name = re.sub(r' Project$', '', name)
    clean_name = re.sub(r' Improvements$', '', clean_name)
    clean_name = re.sub(r' Repairs$', '', clean_name)
    disaster_base_names.add(clean_name)

# Calculate total funding for disaster projects
total_funding = 0
funded_projects = []

for funding in funding_data:
    fund_project_name = funding.get('Project_Name', '')
    amount = int(funding.get('Amount', 0))
    
    # Check if this is a disaster project
    is_disaster_funding = False
    
    # Check for disaster indicators in the name
    if any(indicator in fund_project_name for indicator in disaster_indicators):
        is_disaster_funding = True
    
    # Check if it matches any of our extracted disaster projects
    if not is_disaster_funding:
        for base_name in disaster_base_names:
            if base_name in fund_project_name or fund_project_name in base_name:
                is_disaster_funding = True
                break
    
    if is_disaster_funding:
        total_funding += amount
        funded_projects.append({
            'project': fund_project_name,
            'amount': amount
        })

result = {
    'total_funding': total_funding,
    'project_count': len(funded_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
