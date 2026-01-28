code = """import json
import re

# Read the file paths
with open('/tmp/tmpu6u5shtd.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmphv6u7l7_.json', 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# List to store park projects completed in 2022
park_projects_2022 = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for completion statements with 2022
    completion_patterns = [
        (r'Construction was completed[^\n]*2022[^\n]*', 'Construction'),
        (r'completed[^\n]*2022[^\n]*', 'Simple'),
        (r'Complete Construction[^\n]*2022[^\n]*', 'Construction')
    ]
    
    for pattern, ptype in completion_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Get surrounding context to find project name
            start_pos = max(0, match.start() - 1000)
            context = text[start_pos:match.start()]
            
            # Split into lines and look backwards for project name
            lines = context.split('\n')
            project_name = None
            
            # Look for project names in preceding lines (common patterns)
            for line in reversed(lines):
                line = line.strip()
                if line and len(line) > 5:
                    # Skip bullet points and metadata
                    if any(line.startswith(x) for x in ['(', '•', '-', '□', '■', '♦']):
                        continue
                    if 'Updates:' in line or 'Schedule:' in line:
                        continue
                    
                    # Look for typical project name patterns
                    project_indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Structure', 
                                         'Walkway', 'Park', 'Facility', 'System']
                    
                    if any(indicator in line for indicator in project_indicators):
                        # Check if line looks like a project name (not too long, not metadata)
                        if 10 < len(line) < 150:
                            project_name = line
                            break
            
            if project_name:
                # Check if it's park-related
                park_keywords = ['park', 'Park', 'playground', 'Playground']
                is_park = any(kw in project_name for kw in park_keywords)
                
                # Also check if context contains park references
                if not is_park and any(kw in context for kw in park_keywords):
                    is_park = True
                
                if is_park:
                    park_projects_2022.append({
                        'Project_Name': project_name,
                        'source_file': filename,
                        'completion_context': match.group(0)
                    })

# Remove duplicates based on project name
unique_projects = {}
for project in park_projects_2022:
    name = project['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = project

park_projects_2022 = list(unique_projects.values())

print(f"Found {len(park_projects_2022)} unique park projects completed in 2022:")
for p in park_projects_2022:
    print(f"  - {p['Project_Name']}")

# Now find these projects in the funding database and sum their amounts
project_names = [p['Project_Name'] for p in park_projects_2022]

# Normalize project names for matching
def normalize_name(name):
    return name.lower().strip().replace('  ', ' ')

# Also create simplified versions (without long descriptions)
def simplify_name(name):
    # Take first part before comma or parenthesis
    if ',' in name:
        name = name.split(',')[0]
    if '(' in name:
        name = name.split('(')[0]
    return name.strip()

# Build a mapping of simplified names
funding_by_exact = {}
funding_by_simplified = {}

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    
    exact_key = normalize_name(fund_name)
    if exact_key not in funding_by_exact:
        funding_by_exact[exact_key] = []
    funding_by_exact[exact_key].append(amount)
    
    simp_key = normalize_name(simplify_name(fund_name))
    if simp_key not in funding_by_simplified:
        funding_by_simplified[simp_key] = []
    funding_by_simplified[simp_key].append(amount)

# Try to match our park projects with funding
matched_projects = []
total_funding = 0

for project in park_projects_2022:
    proj_name = project['Project_Name']
    simp_proj = normalize_name(simplify_name(proj_name))
    
    # Try exact matches first
    amount = 0
    matched = False
    
    for fund_key in funding_by_exact:
        if fund_key in simp_proj or simp_proj in fund_key:
            amount = sum(funding_by_exact[fund_key])
            matched = True
            break
    
    if not matched:
        # Try simplified matches
        for fund_key in funding_by_simplified:
            if fund_key in simp_proj or simp_proj in fund_key:
                amount = sum(funding_by_simplified[fund_key])
                matched = True
                break
    
    if matched:
        matched_projects.append({
            'project': proj_name,
            'funding': amount
        })
        total_funding += amount
    else:
        matched_projects.append({
            'project': proj_name,
            'funding': 0
        })

print(f"\nMatched {len([p for p in matched_projects if p['funding'] > 0])} projects with funding")
print(f"Total funding: ${total_funding:,}")

result = json.dumps({
    'projects': matched_projects,
    'total_funding': total_funding
})

print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
