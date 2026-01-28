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

# Extract project information from civic documents
projects = []
project_patterns = [
    # Matches project names in the Design section
    r'([A-Z][a-zA-Z\s&\-]+?(?:Project|Improvements|Repairs|Park|Facility|Plan|Structure|Study|System)).*?\(cid:190\) Updates:',
]

type_keywords = ['capital', 'disaster', 'FEMA', 'project', 'improvements', 'repairs', 'road', 'park', 'bridge']
status_patterns = [
    (r'Capital Improvement Projects \(Design\)', 'design'),
    (r'Capital Improvement Projects \(Construction\)', 'construction'),
    (r'Capital Improvement Projects \(Not Started\)', 'not started'),
    (r'Disaster Recovery Projects \(Design\)', 'design'),
    (r'Disaster Recovery Projects \(Construction\)', 'construction'),
]

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find sections and their statuses
    sections = []
    for pattern, status in status_patterns:
        if re.search(pattern, text):
            # Find the section boundaries
            section_match = re.search(pattern + r'(.*?)(?=(?:Capital Improvement Projects|Disaster Recovery Projects|$))', text, re.DOTALL)
            if section_match:
                sections.append((section_match.group(1), status))
    
    # Extract projects from each section
    for section_text, status in sections:
        # Find project names in this section
        lines = section_text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for project names (typically standalone lines that aren't empty, dates, or obvious headings)
            if (line and 
                not line.startswith('(') and 
                not line.startswith('cid:') and 
                not line.startswith('RECOMMENDED ACTION') and
                not line.startswith('DISCUSSION:') and
                not line.startswith('Page') and
                not re.match(r'^\d+\s+of\s+\d+$', line) and
                len(line) > 10 and
                len(line) < 200):
                
                # Check if it's likely a project name
                has_keywords = any(kw.lower() in line.lower() for kw in type_keywords)
                is_all_upper = line.isupper()
                # Check if next few lines contain project indicators
                next_text = ' '.join(lines[i+1:i+4]) if i+1 < len(lines) else ''
                has_updates = 'Updates:' in next_text or 'Schedule:' in next_text
                
                if (has_keywords or is_all_upper or has_updates) and not re.match(r'(cid:|\(|Page \d)', line):
                    project_name = line.strip()
                    # Clean up the name
                    if project_name.endswith(':'):
                        project_name = project_name[:-1]
                    
                    # Determine type
                    project_type = 'unknown'
                    if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
                        project_type = 'disaster'
                    elif any(kw in project_name.lower() for kw in ['capital', 'project', 'improvements', 'repairs', 'facility', 'system']):
                        project_type = 'capital'
                    
                    projects.append({
                        'Project_Name': project_name,
                        'type': project_type,
                        'status': status
                    })

# Filter for capital projects with 'design' status
capital_design_projects = [p for p in projects if p['status'] == 'design' and p['type'] == 'capital']

# Clean project names for matching
def clean_name(name):
    # Remove common suffixes that might not be in the other list
    name = re.sub(r'\s*\(FEMA.*?\)$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES.*?\)$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA.*?\)$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*Project$', '', name, flags=re.IGNORECASE)
    return name.strip()

# Create mapping of cleaned names to original funding records
funding_by_name = {}
for record in funding_records:
    orig_name = record['Project_Name']
    cleaned = clean_name(orig_name)
    amount = int(record['Amount'])
    if amount > 50000:
        funding_by_name[cleaned.lower()] = {
            'original_name': orig_name,
            'amount': amount,
            'record': record
        }

# Match projects with funding
matched_projects = []
for project in capital_design_projects:
    proj_name_clean = clean_name(project['Project_Name']).lower()
    
    # Try exact match
    if proj_name_clean in funding_by_name:
        matched_projects.append({
            'project': project['Project_Name'],
            'funding': funding_by_name[proj_name_clean]['original_name'],
            'amount': funding_by_name[proj_name_clean]['amount']
        })
    else:
        # Try partial matching
        for funded_name in funding_by_name.keys():
            if (proj_name_clean in funded_name or funded_name in proj_name_clean):
                matched_projects.append({
                    'project': project['Project_Name'],
                    'funding': funding_by_name[funded_name]['original_name'],
                    'amount': funding_by_name[funded_name]['amount']
                })
                break

# Count unique projects with funding > $50,000
unique_projects = len(set(p['project'] for p in matched_projects))

print("__RESULT__:")
print(json.dumps({
    "capital_design_projects_found": len(capital_design_projects),
    "matched_with_funding": len(matched_projects),
    "unique_projects_count": unique_projects,
    "matched_projects": matched_projects[:10]  # First 10 for inspection
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
