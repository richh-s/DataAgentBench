code = """import json
import re

# Load funding data
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:8
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map for projects with amount > 50000
def clean_project_name(name):
    name = re.sub(r'\s*\(FEMA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES[^\)]*\)', '', name, flags=re.IGNORECASE)  
    name = re.sub(r'\s*\(CalJPIA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*Project\s*$', '', name, flags=re.IGNORECASE)
    return name.strip()

funding_map = {}
for record in funding_records:
    amount = int(record['Amount'])
    if amount > 50000:
        clean_key = clean_project_name(record['Project_Name']).lower()
        funding_map[clean_key] = {
            'original_name': record['Project_Name'],
            'amount': amount
        }

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find where this section ends (next major heading)
    construct_pos = text.find('Capital Improvement Projects (Construction)', design_start)
    if construct_pos == -1:
        construct_pos = text.find('Disaster Recovery Projects (Design)', design_start)
    if construct_pos == -1:
        construct_pos = len(text)
    
    design_section = text[design_start:construct_pos]
    lines = design_section.split('\n')
    
    # Process each line to find project names
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headings and markers
        if line.startswith('(') or 'Capital Improvement' in line:
            continue
        
        # Look ahead to see if this is followed by project details
        if i + 1 < len(lines):
            next_lines = ' '.join(lines[i+1:min(i+5, len(lines))])
            if 'Updates:' in next_lines or 'Schedule:' in next_lines or 'cid:190' in next_lines:
                # This is likely a project name
                project_name = line[:-1] if line.endswith(':') else line
                
                # Skip disaster projects (contain FEMA/CalOES/CalJPIA)
                if 'FEMA' not in project_name and 'CalOES' not in project_name and 'CalJPIA' not in project_name:
                    # Check if it's a capital project by looking for infrastructure keywords
                    keywords = ['road', 'park', 'drain', 'bridge', 'facility', 'system', 'plan', 'structure', 'study', 'improvements', 'repairs', 'street', 'water', 'traffic']
                    if any(kw in project_name.lower() for kw in keywords):
                        design_projects.append(project_name)

# Remove duplicate project names
unique_design_projects = list(set(design_projects))

# Match capital design projects with funding data > $50,000
matched_projects = []

for project_name in unique_design_projects:
    clean_proj = clean_project_name(project_name).lower()
    
    # Direct match
    if clean_proj in funding_map:
        matched_projects.append({
            'project': project_name,
            'funding_record': funding_map[clean_proj]['original_name'],
            'amount': funding_map[clean_proj]['amount']
        })
        continue
    
    # Partial/fuzzy match
    for funded_key in funding_map:
        if clean_proj in funded_key or funded_key in clean_proj:
            matched_projects.append({
                'project': project_name,
                'funding_record': funding_map[funded_key]['original_name'],
                'amount': funding_map[funded_key]['amount']
            })
            break

# Get final count
final_count = len(matched_projects)

print("__RESULT__:")
print(json.dumps({
    "count": final_count,
    "sample_projects": [{'name': m['project'], 'amount': m['amount']} for m in matched_projects[:5]]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
