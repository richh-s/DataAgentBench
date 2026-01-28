code = """import json
import re

# Get file paths
civic_docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

# Load data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to extract project info from text
def extract_projects(text):
    projects = []
    lines = text.split('\n')
    
    for idx, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Check for disaster indicators
        disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']
        has_disaster = any(keyword in line for keyword in disaster_keywords)
        
        if not has_disaster:
            continue
            
        # Clean project name
        project_name = re.sub(r'^[\d\s\-\•\.]+', '', line)
        
        # Look for 2022 in context (nearby lines)
        context_start = max(0, idx - 15)
        context_end = min(len(lines), idx + 15)
        context_text = ' '.join(lines[context_start:context_end])
        
        started_in_2022 = ('2022' in context_text)
        
        projects.append({
            'name': project_name,
            'started_in_2022': started_in_2022
        })
    
    return projects

# Extract all potential disaster projects from civic docs
all_disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_projects(text)
    all_disaster_projects.extend(projects)

# Create a set of unique 2022 disaster project names
projects_2022 = set()
for p in all_disaster_projects:
    if p['started_in_2022']:
        name_clean = p['name'].split('(')[0].strip()
        if len(name_clean) > 8:
            projects_2022.add(name_clean)

# Match with funding records
total_funding = 0
matched_projects = {}

for funding in funding_data:
    fund_name = funding.get('Project_Name', '')
    
    # Direct match check
    for proj_2022 in projects_2022:
        if (fund_name.startswith(proj_2022) or 
            proj_2022.startswith(fund_name) or
            fund_name.replace('(', '').replace(')', '').startswith(proj_2022)):
            amount = int(funding.get('Amount', 0))
            total_funding += amount
            matched_projects[fund_name] = amount
            break

# Also check for disaster projects in funding that might not be in our civic docs extraction
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire']
for funding in funding_data:
    fund_name = funding.get('Project_Name', '')
    
    if any(keyword in fund_name for keyword in disaster_keywords):
        amount = int(funding.get('Amount', 0))
        total_funding += amount
        matched_projects[fund_name] = amount

# Sum unique amounts
total_funding_unique = sum(matched_projects.values())

result_str = f"Total funding for disaster-related projects that started in 2022: ${total_funding_unique:,}"
print("__RESULT__:")
print(json.dumps(result_str))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
