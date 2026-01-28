code = """import json
import re

# Load the data from storage
mongo_result = locals().get('var_functions.query_db:10')
funding_result = locals().get('var_functions.query_db:22')

# Load MongoDB documents
if isinstance(mongo_result, str):
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_result or []

# Load funding data
if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result or []

print('Loaded {} documents and {} funding records'.format(len(mongo_docs), len(funding_records)))

# Create a set of all funded project names for easy lookup
funded_project_names = set()
funding_amount_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    if name:
        funded_project_names.add(name)
        funding_amount_map[name] = int(rec.get('Amount', 0))

# Extract project-status pairs from MongoDB documents
project_status_map = {}

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for the section headers that indicate project status
    # Pattern: "Capital Improvement Projects (Status)"
    status_pattern = r'Capital Improvement Projects \((Design|Construction|Not Started)\)'
    status_matches = re.finditer(status_pattern, text)
    
    for match in status_matches:
        status = match.group(1).lower()
        section_start = match.start()
        
        # Find the end of this section (start of next major section)
        next_section = text.find('\n\n', section_start)
        if next_section == -1:
            section_text = text[section_start:section_start + 3000]
        else:
            section_text = text[section_start:next_section]
        
        # Extract project names from this section
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines, bullet points, headers
            if not line or line.startswith('(') or line.startswith('•') or line.startswith('▪'):
                continue
            if line.isupper() or line.endswith(':'):
                continue
            # Skip noise lines
            noise_keywords = ['Updates:', 'Schedule:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Subject:', 'To:', 'From:', 'Page', 'Item', 'Agenda Report', 'Staff will provide', 'City Council']
            if any(noise in line for noise in noise_keywords):
                continue
            
            # This looks like a project name
            if len(line) > 8:
                project_status_map[line] = status

print('Found {} project-status mappings'.format(len(project_status_map)))

# Check some examples
examples = list(project_status_map.items())[:10]
print('Sample mappings:')
for proj, stat in examples:
    print('  {}: {}'.format(proj[:60], stat))

# Now find projects that are in design status AND have funding > $50k
design_projects_with_funding = []

for project_name, status in project_status_map.items():
    if status == 'design':
        # Check if this project is in our funding list
        # Need to handle name variations
        for funded_name in funded_project_names:
            # Check for direct or partial match
            proj_clean = project_name.lower().replace('project', '').strip()
            fund_clean = funded_name.lower().replace('project', '').strip()
            
            # Check if project name is similar (share at least 2 key words, excluding common words)
            proj_words = set(proj_clean.split())
            fund_words = set(fund_clean.split())
            
            # Remove very common words
            common = {'and', 'road', 'street', 'drive', 'avenue', 'lane', 'the', 'of', 'in', 'for', 'to', 'improvements', 'repairs', 'project'}
            proj_key = proj_words - common
            fund_key = fund_words - common
            
            # Check for matches
            if len(proj_key.intersection(fund_key)) >= 2:
                if funded_name not in [p['name'] for p in design_projects_with_funding]:
                    design_projects_with_funding.append({
                        'name': funded_name,
                        'amount': funding_amount_map[funded_name],
                        'matched_design_name': project_name
                    })
                break
            # Also check if one name contains the other (for shorter names)
            elif len(proj_key) <= 3 and any(word in fund_key for word in proj_key):
                overlap = proj_key.intersection(fund_key)
                if len(overlap) >= 1 and len(proj_key) <= 3:
                    if funded_name not in [p['name'] for p in design_projects_with_funding]:
                        design_projects_with_funding.append({
                            'name': funded_name,
                            'amount': funding_amount_map[funded_name],
                            'matched_design_name': project_name
                        })
                    break

print('Found {} design projects with funding > $50k'.format(len(design_projects_with_funding)))

# Return the count
result = {
    'count': len(design_projects_with_funding),
    'sample_projects': design_projects_with_funding[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
