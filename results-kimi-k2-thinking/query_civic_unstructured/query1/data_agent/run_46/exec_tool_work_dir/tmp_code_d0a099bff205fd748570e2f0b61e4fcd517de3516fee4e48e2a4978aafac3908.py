code = """import json
import re

# Load the funding data file
funding_file_path = var_functions.query_db:6
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents file
civic_file_path = var_functions.query_db:8
with open(civic_file_path, 'r') as f:
    civic_documents = json.load(f)

# Build a map of clean project names to funding records (amount > 50000)
def clean_name(name):
    name = re.sub(r'\s*\(FEMA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*Project\s*$', '', name, flags=re.IGNORECASE)
    return name.strip()

funding_map = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        clean_key = clean_name(record['Project_Name']).lower()
        funding_map[clean_key] = {
            'original_name': record['Project_Name'],
            'amount': amount
        }

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
        
    # Find where this section ends (next major section)
    next_section_start = text.find('Capital Improvement Projects (Construction)', design_start)
    if next_section_start == -1:
        next_section_start = len(text)
    
    design_section = text[design_start:next_section_start]
    lines = design_section.split('\n')
    
    # Extract project names from this section
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and markers
        skip_conditions = [
            not line,
            line.startswith('('),
            line.startswith('cid:'),
            line.startswith('RECOMMENDED'),
            line.startswith('DISCUSSION:'),
            line.startswith('Page'),
            line.startswith('Capital Improvement'),
            len(line) < 10,
            line.isupper() and len(line) < 50  # Skip short all-caps headings
        ]
        
        if any(skip_conditions):
            i += 1
            continue
        
        # Check if this is likely a project name
        keywords = ['road', 'park', 'drain', 'bridge', 'facility', 'system', 'plan', 'structure', 'study', 'improvements', 'repairs']
        has_keyword = any(kw in line.lower() for kw in keywords)
        
        # Look ahead for project indicators
        next_chunk = ' '.join(lines[i+1:min(i+5, len(lines))])
        has_updates = 'Updates:' in next_chunk or 'Schedule:' in next_chunk or 'cid:190' in next_chunk
        
        if has_keyword or has_updates:
            project_name = line
            if project_name.endswith(':'):
                project_name = project_name[:-1]
            
            # Skip disaster projects
            if 'FEMA' not in project_name and 'CalOES' not in project_name and 'CalJPIA' not in project_name:
                design_projects.append(project_name)
                i += 4  # Skip ahead to avoid duplicates
            else:
                i += 1
        else:
            i += 1

# Remove duplicates
unique_projects = list(set(design_projects))

# Match with funding data
matched_projects = []

for project_name in unique_projects:
    clean_proj = clean_name(project_name).lower()
    
    if clean_proj in funding_map:
        matched_projects.append({
            'project': project_name,
            'funding_record': funding_map[clean_proj]['original_name'],
            'amount': funding_map[clean_proj]['amount']
        })
    else:
        # Try partial match
        for funded_clean in funding_map.keys():
            if clean_proj in funded_clean or funded_clean in clean_proj:
                matched_projects.append({
                    'project': project_name,
                    'funding_record': funding_map[funded_clean]['original_name'],
                    'amount': funding_map[funded_clean]['amount']
                })
                break

# Final count
result_count = len(matched_projects)

print("__RESULT__:")
print(json.dumps({
    "count": result_count,
    "sample_projects": matched_projects[:5]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
