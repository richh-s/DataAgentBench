code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:4
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:4

# Load civic docs
civic_file = var_functions.query_db:5
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:5

# Filter funding > $50,000
high_funding = []
for f in funding_data:
    if isinstance(f, dict) and int(f.get('Amount', 0)) > 50000:
        high_funding.append(f)

# Find capital projects with design status
design_projects = []

for doc in civic_docs:
    if not isinstance(doc, dict):
        continue
    
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for design section header
    if 'Capital Improvement Projects (Design)' in text:
        # Find all project names in this document (lines that look like project names)
        lines = text.split('\n')
        in_design_section = False
        
        for line in lines:
            line = line.strip()
            
            if 'Capital Improvement Projects (Design)' in line:
                in_design_section = True
                continue
            
            if 'Capital Improvement Projects (Construction)' in line:
                in_design_section = False
                continue
            
            if in_design_section and line and len(line) > 10:
                # Skip headers and metadata
                skip_words = ['Public Works', 'Commission', 'Agenda', 'Date', 'To:', 'From:', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Page', 'Agenda Item', 'cid:', 'Project', 'Schedule', 'Updates', 'Complete', 'Advertise', 'Begin']
                should_skip = any(word in line for word in skip_words)
                
                if not should_skip and not line.endswith(':') and not line.startswith('(') and not line.startswith('•') and not line.startswith('-'):
                    # Clean up the line
                    clean_name = re.sub(r'\s+', ' ', line).strip()
                    
                    # Check if this is likely a project name (not a date, not a status)
                    if not re.match(r'^(cid:|\d|Spring|Summer|Fall|Winter|Complete|Advertise|Begin)', clean_name):
                        design_projects.append(clean_name)

# Now match with funding data
results = []
for funding in high_funding:
    project_name = funding.get('Project_Name', '')
    if not project_name:
        continue
    
    # Check base name
    base_name = project_name.split(' (')[0]
    
    # Check if base name appears in design projects
    for design_project in design_projects:
        if base_name in design_project or design_project in base_name:
            # Check if it's a capital project (not disaster)
            if 'FEMA' not in project_name.upper() and 'CalOES' not in project_name and 'CalJPIA' not in project_name:
                results.append({
                    'Project_Name': project_name,
                    'Funding': int(funding['Amount']),
                    'Source': funding['Funding_Source']
                })
                break

# Remove duplicates
unique_results = []
seen_names = set()
for r in results:
    if r['Project_Name'] not in seen_names:
        unique_results.append(r)
        seen_names.add(r['Project_Name'])

final_result = {
    'count': len(unique_results),
    'projects': unique_results
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
