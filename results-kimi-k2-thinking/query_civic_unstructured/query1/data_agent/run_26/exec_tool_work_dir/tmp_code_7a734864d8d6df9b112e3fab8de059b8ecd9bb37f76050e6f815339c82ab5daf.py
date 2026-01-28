code = """import json
import re

# Load funding data (projects > $50,000)
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Create a dictionary of funded projects for easy lookup
funded_projects = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip().lower()
    funded_projects[proj_name] = {
        'original_name': record['Project_Name'],
        'amount': int(record['Amount'])
    }

# Load civic documents
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

# Parse civic documents to extract capital projects with design status
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for "Capital Improvement Projects (Design)" section
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)'
    design_section = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_section:
        section_text = design_section.group(1)
        
        # Find project names - they typically appear as standalone lines before updates
        lines = section_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('▪') \
               and 'Updates:' not in line and 'Project Schedule:' not in line \
               and 'Estimated Schedule:' not in line and 'Project Description:' not in line \
               and not any(keyword in line for keyword in ['Complete Design:', 'Advertise:', 'Begin Construction:', 'Final Design:']):
                
                # This might be a project name - check if next lines contain updates/schedule
                if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1] or 'Estimated Schedule:' in lines[i+1]):
                    project_name = line.strip()
                    if project_name and len(project_name) > 5:
                        design_capital_projects.append({
                            'project_name': project_name,
                            'type': 'capital',
                            'status': 'design'
                        })
            i += 1

# Now match design capital projects with funded projects > $50,000
matched_projects = []
for project in design_capital_projects:
    proj_name_lower = project['project_name'].lower()
    
    # Direct match
    if proj_name_lower in funded_projects:
        matched_projects.append({
            'project_name': project['project_name'],
            'funding': funded_projects[proj_name_lower]['amount']
        })
    else:
        # Fuzzy match - check if any funded project contains this name or vice versa
        for funded_name_lower, funded_info in funded_projects.items():
            if (proj_name_lower in funded_name_lower or funded_name_lower in proj_name_lower) \
                and abs(len(proj_name_lower) - len(funded_name_lower)) < 20:
                matched_projects.append({
                    'project_name': project['project_name'],
                    'funded_as': funded_info['original_name'],
                    'funding': funded_info['amount']
                })
                break

count_over_50000 = sum(1 for p in matched_projects if p['funding'] > 50000)

print('__RESULT__:')
print(json.dumps({
    'total_design_capital_projects': len(design_capital_projects),
    'matched_funded_projects': len(matched_projects),
    'count_over_50000': count_over_50000
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
