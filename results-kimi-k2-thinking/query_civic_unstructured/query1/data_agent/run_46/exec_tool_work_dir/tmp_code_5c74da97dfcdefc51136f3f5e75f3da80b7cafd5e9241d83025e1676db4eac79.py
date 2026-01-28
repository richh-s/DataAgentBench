code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:6
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:8
with open(civic_file, 'r') as f:
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
        clean_name = clean_project_name(record['Project_Name']).lower()
        funding_map[clean_name] = {
            'original': record['Project_Name'],
            'amount': amount
        }

# Extract capital projects with 'design' status from civic documents
projects_in_design = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the "Capital Improvement Projects (Design)" section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    construction_section_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_section_start != -1 and construction_section_start != -1:
        # Extract just the design section
        design_section = text[design_section_start:construction_section_start]
        
        # Split into lines and process
        lines = design_section.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Skip empty lines and markers
            if line and not line.startswith('(') and not line.startswith('cid:') and not line.startswith('RECOMMENDED') and not line.startswith('DISCUSSION:') and not line.startswith('Page') and len(line) > 10:
                # Check if next lines contain project indicators
                next_chunk = ' '.join(lines[i+1:min(i+5, len(lines))])
                if 'Updates:' in next_chunk or 'Schedule:' in next_chunk or 'cid:190' in next_chunk:
                    # This is likely a project name
                    project_name = line
                    if project_name.endswith(':'):
                        project_name = project_name[:-1]
                    
                    # Determine if it's capital or disaster
                    is_disaster = 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name
                    is_capital = not is_disaster and any(kw in project_name.lower() for kw in ['road', 'park', 'drain', 'bridge', 'facility', 'system', 'plan', 'structure', 'study', 'improvements'])
                    
                    if is_capital or (not is_disaster and len(project_name) < 100):
                        projects_in_design.append({
                            'name': project_name,
                            'status': 'design',
                            'type': 'capital'
                        })
                        # Skip ahead to avoid duplicate detection
                        i += 4
            i += 1

# Remove duplicates
unique_projects = []
seen_names = set()
for p in projects_in_design:
    if p['name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['name'])

# Match with funding data
matched_count = 0
matched_details = []

for project in unique_projects:
    proj_clean = clean_project_name(project['name']).lower()
    
    if proj_clean in funding_map:
        matched_count += 1
        matched_details.append({
            'project': project['name'],
            'funding_record': funding_map[proj_clean]['original'],
            'amount': funding_map[proj_clean]['amount']
        })
    else:
        # Try partial matching
        for funded_clean in funding_map.keys():
            if proj_clean in funded_clean or funded_clean in proj_clean:
                matched_count += 1
                matched_details.append({
                    'project': project['name'],
                    'funding_record': funding_map[funded_clean]['original'],
                    'amount': funding_map[funded_clean]['amount']
                })
                break

print("__RESULT__:")
print(json.dumps({
    "total_capital_design_projects": len(unique_projects),
    "projects_with_funding_over_50000": matched_count,
    "sample_matches": matched_details[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
