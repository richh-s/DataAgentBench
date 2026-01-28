code = """import json
import re

# Load the data
funding_path = var_functions.query_db:14
civic_path = var_functions.query_db:8

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Get unique project names from funding
project_names = set(item['Project_Name'] for item in funding_data)

# Extract design projects from documents
design_projects = set()
for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section boundaries
    design_start = text.find('Capital Improvement Projects (Design)')
    design_end = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0 and design_end > design_start:
        design_section = text[design_start:design_end]
        lines = design_section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip metadata and look for project names
            if (line and len(line) > 15 and not line.startswith('(') and 
                line[0].isupper() and 'Capital Improvement' not in line and
                'Updates:' not in line and 'Project Schedule' not in line and
                'Complete Design' not in line):
                
                # Clean line
                clean_line = re.sub(r'[:;\-•*]+$', '', line).strip()
                if len(clean_line) > 10:
                    design_projects.add(clean_line)

# Match funding projects with design projects
matched_projects = []
for fp in project_names:
    fp_lower = fp.lower()
    for dp in design_projects:
        dp_lower = dp.lower()
        # Check if one contains the other
        if fp_lower in dp_lower or dp_lower in fp_lower:
            matched_projects.append(fp)
            break
        # Check base name without parentheses
        base_fp = re.sub(r'\s*\([^)]+\)$', '', fp)
        if base_fp.lower() in dp_lower:
            matched_projects.append(fp)
            break

# Filter for capital improvement projects (infrastructure)
capital_keywords = ['road', 'street', 'highway', 'bridge', 'park', 'drain', 
                   'walkway', 'traffic', 'skate', 'playground', 'water', 
                   'storm', 'slope', 'retaining', 'wall', 'culvert']

capital_design_projects = []
for proj in matched_projects:
    proj_lower = proj.lower()
    if any(keyword in proj_lower for keyword in capital_keywords):
        capital_design_projects.append(proj)

print('__RESULT__:')
print(json.dumps({
    'funding_projects_over_50k': len(project_names),
    'design_projects_in_documents': len(design_projects),
    'capital_design_with_funding': len(capital_design_projects)
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
