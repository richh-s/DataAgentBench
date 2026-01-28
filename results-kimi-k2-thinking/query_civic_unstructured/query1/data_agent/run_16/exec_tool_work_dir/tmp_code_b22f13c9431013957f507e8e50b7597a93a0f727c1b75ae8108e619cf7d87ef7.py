code = """import json
import re

# Read the funding data
with open('var_functions.query_db:14', 'r') as f:
    funding_records = json.load(f)

# Extract project names
funding_projects = [r['Project_Name'] for r in funding_records]

# Read civic documents  
with open('var_functions.query_db:8', 'r') as f:
    civic_docs = json.load(f)

# Extract design projects from documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    end = text.find('Capital Improvement Projects (Construction)')
    
    if start >= 0 and end > start:
        section = text[start:end]
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for lines that start with capital letters and are long enough
            if (line and len(line) > 15 and not line.startswith('(') and 
                'Capital Improvement' not in line and 'Updates:' not in line and
                'Project Schedule' not in line and 'Complete Design' not in line):
                
                if re.match('^[A-Z]', line):
                    clean = re.sub('[:;\-•*]+$', '', line).strip()
                    if len(clean) > 10:
                        design_projects.append(clean)

# Match projects
capital_design = []
for fp in funding_projects:
    fp_lower = fp.lower()
    for dp in design_projects:
        dp_lower = dp.lower()
        if fp_lower in dp_lower or dp_lower in fp_lower:
            capital_design.append(fp)
            break
        # Check base name
        base = re.sub('\s*\([^)]+\)$', '', fp)
        if base.lower() in dp_lower:
            capital_design.append(fp)
            break

# Filter for capital projects
capital_keywords = ['road', 'street', 'highway', 'bridge', 'park', 'drain', 'culvert', 
                   'walkway', 'traffic', 'signal', 'skate', 'playground', 'water', 
                   'storm', 'slope', 'retaining', 'wall']

final_projects = []
for proj in capital_design:
    plower = proj.lower()
    if any(k in plower for k in capital_keywords):
        final_projects.append(proj)

print('__RESULT__:')
print(json.dumps({
    'total_over_50k': len(funding_projects),
    'design_projects_found': len(design_projects),
    'capital_design_projects': len(final_projects),
    'sample_projects': final_projects[:15]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
