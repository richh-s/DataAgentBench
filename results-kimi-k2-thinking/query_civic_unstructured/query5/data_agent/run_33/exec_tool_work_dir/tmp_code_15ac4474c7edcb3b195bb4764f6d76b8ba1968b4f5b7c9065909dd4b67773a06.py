code = """import json
import re
import os

# Access the data from storage
civic_docs_file = var_functions.query_db:2
funding_file = var_functions.query_db:5

# Open the files and load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to extract disaster project patterns from text
def extract_disaster_projects(text):
    projects = []
    
    # Look for disaster-related project patterns
    patterns = [
        r'([A-Za-z0-9\s\-\.]+\(FEMA[^\)]*\))',
        r'([A-Za-z0-9\s\-\.]+\(CalOES[^\)]*\))',
        r'([A-Za-z0-9\s\-\.]+\(CalJPIA[^\)]*\))',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        projects.extend(matches)
    
    return list(set(projects))

# Extract disaster projects from all documents that mention 2022
disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    if '2022' in text:
        projects_in_doc = extract_disaster_projects(text)
        disaster_projects.extend(projects_in_doc)

# Remove duplicates
disaster_projects = list(set([p.strip() for p in disaster_projects]))

# Normalize project names for matching
def normalize_name(name):
    name = name.strip()
    name = re.sub(r'\s*\([^\)]*\)$', '', name)
    return name.strip()

# Create normalized mapping
normalized_disaster_projects = {}
for proj in disaster_projects:
    normalized = normalize_name(proj)
    if normalized:
        if normalized not in normalized_disaster_projects:
            normalized_disaster_projects[normalized] = []
        normalized_disaster_projects[normalized].append(proj)

# Find disaster projects in funding data that started in 2022
disaster_2022_projects = []
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'recovery', 'fire', 'culvert', 'bridge', 'drainage']

for funding in funding_data:
    proj_name = funding['Project_Name']
    amount_str = funding['Amount']
    
    if amount_str is None:
        continue
    
    try:
        amount = int(amount_str)
    except (ValueError, TypeError):
        continue
    
    # Check if it's a disaster project
    is_disaster = any(keyword in proj_name.lower() for keyword in disaster_keywords)
    
    # For now, we'll include all disaster projects regardless of 2022 date
    # and also look for explicit 2022 references
    has_2022 = '2022' in proj_name
    
    if is_disaster:
        # Check if it's likely a 2022 project
        likely_2022 = has_2022 or any(year in proj_name for year in ['2021-2022', '2022-2023'])
        
        disaster_2022_projects.append({
            'project': proj_name,
            'amount': amount,
            'source': funding.get('Funding_Source', ''),
            'explicit_2022': has_2022
        })

# Also match based on extracted disaster project names
for funding in funding_data:
    fund_proj_name = funding['Project_Name']
    amount_str = funding['Amount']
    
    if amount_str is None:
        continue
    
    try:
        amount = int(amount_str)
    except (ValueError, TypeError):
        continue
    
    for norm_name, variants in normalized_disaster_projects.items():
        if norm_name.lower() in fund_proj_name.lower():
            disaster_2022_projects.append({
                'project': fund_proj_name,
                'amount': amount,
                'source': funding.get('Funding_Source', ''),
                'matched_from_text': True,
                'explicit_2022': '2022' in fund_proj_name
            })
            break

# Remove duplicates
seen_projects = set()
unique_matches = []
for match in disaster_2022_projects:
    proj_name = match['project']
    if proj_name not in seen_projects:
        seen_projects.add(proj_name)
        unique_matches.append(match)

# Calculate total funding
total_funding = sum(match['amount'] for match in unique_matches)

# Format result
result = {
    'total_funding': total_funding,
    'project_count': len(unique_matches),
    'projects': unique_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
