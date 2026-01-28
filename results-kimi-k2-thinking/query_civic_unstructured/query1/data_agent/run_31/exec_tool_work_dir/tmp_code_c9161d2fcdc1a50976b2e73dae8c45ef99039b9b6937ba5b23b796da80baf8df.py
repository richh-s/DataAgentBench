code = """import json
import re

# Access the stored results from locals()
funding_result = locals()['var_functions.query_db:2']
civic_result = locals()['var_functions.query_db:5']

# Load funding data
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic docs data
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Function to extract projects from civic docs text
def extract_projects_from_text(text):
    projects = []
    text_lower = text.lower()
    
    # Look for capital projects in design section
    if 'capital improvement projects' in text_lower and 'design' in text_lower:
        # Split into sections
        sections = re.split(r'\n\s*\n', text)
        
        for section in sections:
            section_lower = section.lower()
            
            # Check if this is a capital design project
            if 'capital' in section_lower and 'design' in section_lower:
                # Extract project name (usually first line of section)
                lines = [l.strip() for l in section.split('\n') if l.strip()]
                if lines:
                    # First non-empty line is likely the project name
                    project_name = lines[0]
                    
                    # Clean up project name - remove common prefixes/suffixes
                    project_name = re.sub(r'^[\(\)\-\•\d\.\s]*', '', project_name)
                    project_name = re.sub(r'\s+(project|improvements|repairs|improvement)$', '', project_name, flags=re.IGNORECASE)
                    
                    if len(project_name) > 3 and len(project_name) < 150:  # Reasonable length
                        projects.append({
                            'Project_Name': project_name,
                            'status': 'design',
                            'type': 'capital'
                        })
    
    return projects

# Extract all projects from civic docs
all_projects = []
for doc in civic_docs:
    if 'text' in doc:
        projects = extract_projects_from_text(doc['text'])
        all_projects.extend(projects)

# Get unique projects (remove duplicates)
unique_projects = []
seen_names = set()
for proj in all_projects:
    name_key = proj['Project_Name'].lower().strip()
    if name_key not in seen_names:
        seen_names.add(name_key)
        unique_projects.append(proj)

# Get funding projects with amount > 50000
funding_dict = {}
for f in funding_data:
    amount = int(f['Amount'])
    if amount > 50000:
        funding_dict[f['Project_Name']] = f

# Match projects
def normalize_name(name):
    """Normalize project name for comparison"""
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)  # Normalize spaces
    name = re.sub(r'\(fema[^\)]+\)', '', name)  # Remove FEMA suffixes
    name = re.sub(r'\(cal[^\)]+\)', '', name)   # Remove CalOES/CalJPIA suffixes
    name = re.sub(r'[^a-z0-9\s]', '', name)     # Remove special chars
    name = re.sub(r'\s+', ' ', name).strip()
    return name

matched_count = 0
matched_details = []

for proj in unique_projects:
    proj_norm = normalize_name(proj['Project_Name'])
    
    for funding_name, funding_rec in funding_dict.items():
        fund_norm = normalize_name(funding_name)
        
        # Check for substring matches
        if proj_norm in fund_norm or fund_norm in proj_norm:
            matched_count += 1
            matched_details.append({
                'project_name': proj['Project_Name'],
                'funding_name': funding_name,
                'amount': int(funding_rec['Amount']),
                'funding_source': funding_rec['Funding_Source']
            })
            break  # Match found, move to next project

# Print result
result = {
    'count': matched_count,
    'projects': matched_details
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
