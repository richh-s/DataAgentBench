code = """import json
import re

# Read the civic documents from the file
civic_docs_file = var_functions.query_db:2
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data from the file
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to extract project information from text
def extract_disaster_projects(text):
    projects = []
    
    # Look for disaster project patterns
    # Disaster projects often have FEMA/CalOES/CalJPIA suffixes
    patterns = [
        r'([A-Za-z0-9\s\-\.]+\(FEMA[^\)]*\))',  # FEMA projects
        r'([A-Za-z0-9\s\-\.]+\(CalOES[^\)]*\))',  # CalOES projects
        r'([A-Za-z0-9\s\-\.]+\(CalJPIA[^\)]*\))',  # CalJPIA projects
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        projects.extend(matches)
    
    return list(set(projects))  # Remove duplicates

# Extract disaster projects from all documents
disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if the document mentions 2022
    if '2022' in text:
        projects_in_doc = extract_disaster_projects(text)
        disaster_projects.extend(projects_in_doc)

# Remove duplicates and clean up
disaster_projects = list(set([p.strip() for p in disaster_projects]))

# Also look for projects with "2022" in their name that might be disaster-related
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all lines that mention 2022 and contain disaster keywords
    lines = text.split('\n')
    for line in lines:
        if '2022' in line and any(keyword in line.lower() for keyword in ['disaster', 'fema', 'emergency', 'recovery', 'fire']):
            # Try to extract project name (simplified approach)
            if len(line.strip()) < 200:  # Exclude long paragraphs
                # Clean the line to get project name
                project_name = line.strip()
                # Remove common prefixes
                project_name = re.sub(r'^[\*\-\•\d\.\s]+', '', project_name)
                # Remove status indicators
                project_name = re.sub(r'\s+(Design|Construction|Completed|Not Started).*$', '', project_name, flags=re.IGNORECASE)
                
                if project_name and len(project_name) > 10:
                    # Check if it looks like a disaster project
                    if any(keyword in project_name.lower() for keyword in ['fema', 'emergency', 'recovery', 'drainage', 'culvert', 'bridge']):
                        disaster_projects.append(project_name)

# Remove duplicates again
disaster_projects = list(set([p.strip() for p in disaster_projects if p.strip()]))

# Normalize project names for matching (remove common suffixes for matching)
def normalize_name(name):
    name = name.strip()
    # Remove parenthetical suffixes for matching purposes
    name = re.sub(r'\s*\([^\)]*\)$', '', name)
    return name.strip()

# Normalize disaster project names
normalized_disaster_projects = {}
for proj in disaster_projects:
    normalized = normalize_name(proj)
    if normalized not in normalized_disaster_projects:
        normalized_disaster_projects[normalized] = []
    normalized_disaster_projects[normalized].append(proj)

# Now match with funding data
funding_matches = []
for funding in funding_data:
    fund_proj_name = funding['Project_Name']
    fund_amount = int(funding['Amount'])
    
    # Check if it matches any disaster project
    for norm_name, variants in normalized_disaster_projects.items():
        # Check if funding project name contains the normalized name
        if norm_name.lower() in fund_proj_name.lower():
            # Verify it's actually a disaster project by checking for disaster keywords
            if any(keyword in fund_proj_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'recovery']):
                funding_matches.append({
                    'project': fund_proj_name,
                    'amount': fund_amount,
                    'source': funding.get('Funding_Source', ''),
                    'matched_to': variants
                })
                break
        # Also check reverse - if funding name is in variants
        for variant in variants:
            if variant.lower() in fund_proj_name.lower() and len(variant) > 10:
                if any(keyword in fund_proj_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'recovery']):
                    funding_matches.append({
                        'project': fund_proj_name,
                        'amount': fund_amount,
                        'source': funding.get('Funding_Source', ''),
                        'matched_to': variants
                    })
                    break

# Also check for projects that explicitly have 2022 in their name and are disaster-related
disaster_2022_projects = []
for funding in funding_data:
    proj_name = funding['Project_Name']
    amount = int(funding['Amount'])
    
    # Check if project name suggests 2022 start and disaster type
    has_2022 = '2022' in proj_name
    is_disaster = any(keyword in proj_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'recovery', 'fire'])
    
    if has_2022 and is_disaster:
        disaster_2022_projects.append({
            'project': proj_name,
            'amount': amount,
            'source': funding.get('Funding_Source', '')
        })

# Combine matches - use disaster_2022_projects as primary (more reliable)
if disaster_2022_projects:
    final_matches = disaster_2022_projects
else:
    # Fall back to matches extracted from text
    final_matches = funding_matches

# Remove duplicates based on project name
seen_projects = set()
unique_matches = []
for match in final_matches:
    proj_name = match['project']
    if proj_name not in seen_projects:
        seen_projects.add(proj_name)
        unique_matches.append(match)

# Calculate total funding
total_funding = sum(match['amount'] for match in unique_matches)

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'project_count': len(unique_matches),
    'projects': unique_matches
}, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
