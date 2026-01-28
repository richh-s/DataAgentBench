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

# Define status patterns for finding sections
status_patterns = [
    (r'Capital Improvement Projects \(Design\)', 'design'),
    (r'Disaster Recovery Projects \(Design\)', 'design'),
]

# Keywords to identify project names
type_keywords = ['capital', 'disaster', 'FEMA', 'project', 'improvements', 'repairs', 'road', 'park', 'bridge', 'facility', 'system', 'plan', 'structure', 'study']

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find sections with "design" status
    for pattern, status in status_patterns:
        if re.search(pattern, text):
            # Find the section content (between this heading and the next major heading)
            section_pattern = pattern + r'(.*?)(?=(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects \(Construction\)|Disaster Recovery Projects \(Not Started\)|Staff has also prepared|$))'
            section_match = re.search(section_pattern, text, re.DOTALL)
            if section_match:
                section_text = section_match.group(1)
                # Extract project names from this section
                lines = section_text.split('\n')
                for i, line in enumerate(lines):
                    line = line.strip()
                    # Skip empty lines, special markers, page numbers, etc.
                    if (line and 
                        not line.startswith('(') and 
                        not line.startswith('cid:') and 
                        not line.startswith('RECOMMENDED ACTION') and
                        not line.startswith('DISCUSSION:') and
                        not line.startswith('Page') and
                        not re.match(r'^\d+\s+of\s+\d+$', line) and
                        not re.match(r'^[A-Z\s]+$', line) and  # Skip all-caps headings
                        len(line) > 10 and
                        len(line) < 200):
                        
                        # Check if it's likely a project name (contains keywords or next lines have project indicators)
                        has_keywords = any(kw.lower() in line.lower() for kw in type_keywords)
                        
                        # Look ahead for project indicators
                        next_text = ' '.join(lines[i+1:min(i+4, len(lines))])
                        has_project_indicators = 'Updates:' in next_text or 'Schedule:' in next_text or 'cid:190' in next_text
                        
                        if has_keywords or has_project_indicators:
                            project_name = line.strip()
                            if project_name.endswith(':'):
                                project_name = project_name[:-1]
                            
                            # Determine type
                            project_type = 'unknown'
                            if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
                                project_type = 'disaster'
                            elif any(kw in project_name.lower() for kw in ['capital', 'project', 'improvements', 'repairs', 'facility', 'system', 'plan', 'park', 'road', 'structure', 'study']):
                                project_type = 'capital'
                            
                            if project_type == 'capital':
                                projects.append({
                                    'Project_Name': project_name,
                                    'type': project_type,
                                    'status': status
                                })

# Filter for capital projects with 'design' status
capital_design_projects = [p for p in projects if p['status'] == 'design' and p['type'] == 'capital']

# Clean project names for matching (remove parenthetical suffixes and generic terms)
def clean_name(name):
    name = re.sub(r'\s*\(FEMA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA[^\)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*Project\s*$', '', name, flags=re.IGNORECASE)
    return name.strip()

# Create mapping of cleaned project names to funding records with amount > 50000
funding_map = {}
for record in funding_records:
    amount = int(record['Amount'])
    if amount > 50000:
        cleaned_name = clean_name(record['Project_Name']).lower()
        funding_map[cleaned_name] = {
            'original_name': record['Project_Name'],
            'amount': amount
        }

# Match capital design projects with funding
matched_count = 0
matched_projects = []

for project in capital_design_projects:
    proj_name = project['Project_Name']
    proj_clean = clean_name(proj_name).lower()
    
    # Try to find matching funding
    if proj_clean in funding_map:
        matched_count += 1
        matched_projects.append({
            'project': proj_name,
            'funding_record': funding_map[proj_clean]['original_name'],
            'amount': funding_map[proj_clean]['amount']
        })
    else:
        # Try partial matching
        for funded_name in funding_map.keys():
            if proj_clean in funded_name or funded_name in proj_clean:
                matched_count += 1
                matched_projects.append({
                    'project': proj_name,
                    'funding_record': funding_map[funded_name]['original_name'],
                    'amount': funding_map[funded_name]['amount']
                })
                break

print("__RESULT__:")
print(json.dumps({
    "capital_design_projects_extracted": len(capital_design_projects),
    "projects_with_funding_over_50000": matched_count,
    "sample_matches": matched_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
