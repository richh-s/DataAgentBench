code = """import json
import pandas as pd

# Read the civic documents file
civic_docs_file = 'var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs_list = json.load(f)

# Read the funding data file
funding_file = 'var_functions.query_db:5'
with open(funding_file, 'r') as f:
    funding_list = json.load(f)

print(f"Civic docs count: {len(civic_docs_list)}")
print(f"Funding records count: {len(funding_list)}")

# Create a list to store projects with their details
projects = []

# Process each civic document
for doc in civic_docs_list:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for park-related projects completed in 2022
    # Patterns to match completion in 2022
    completion_patterns = [
        r'completed.*2022',
        r'completion.*2022',
        r'2022.*completed',
        r'November 2022',
        r'complete.*2022'
    ]
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line contains park/playground and looks like a project name
        if ('park' in line.lower() or 'playground' in line.lower()) and len(line) > 10:
            # Skip headings and metadata
            skip_terms = ['capital improvement', 'disaster recovery', 'prepared by', 
                         'approved by', 'recommended', 'discussion', 'to:', 'subject:',
                         'public works', 'commission', 'agenda', 'page', 'item']
            
            if any(term in line.lower() for term in skip_terms):
                continue
            
            # Look for completion status in nearby lines
            context_start = max(0, i-10)
            context_end = min(len(lines), i+15)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            # Check if completed in 2022
            if 'completed' in context and '2022' in context:
                # Clean up the project name
                project_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                
                projects.append({
                    'project_name': project_name,
                    'completed_2022': True,
                    'topic': 'park'
                })

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in projects:
    if proj['project_name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['project_name'])

print(f"\nFound {len(unique_projects)} unique park projects:")
for proj in unique_projects:
    print(f"- {proj['project_name']}")

# Create a mapping of project names to funding amounts
funding_dict = {}
for fund in funding_list:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_dict[proj_name] = amount

# Match projects with funding
matched_projects = []
total_funding = 0

for proj in unique_projects:
    proj_name = proj['project_name']
    best_match = None
    best_match_score = 0
    
    # Find matching funding record
    for funded_name in funding_dict.keys():
        # Simple matching: check if project name is contained in funded name or vice versa
        if proj_name.lower() in funded_name.lower() or funded_name.lower() in proj_name.lower():
            # Prefer closer matches
            score = len(set(proj_name.lower().split()) & set(funded_name.lower().split()))
            if score > best_match_score:
                best_match = funded_name
                best_match_score = score
    
    if best_match:
        funding_amount = funding_dict[best_match]
        matched_projects.append({
            'project_name': proj_name,
            'funded_name': best_match,
            'funding': funding_amount
        })
        total_funding += funding_amount
    else:
        matched_projects.append({
            'project_name': proj_name,
            'funded_name': 'NOT FOUND',
            'funding': 0
        })

print(f"\nMatched {len([p for p in matched_projects if p['funding'] > 0])} projects with funding:")
for proj in matched_projects:
    if proj['funding'] > 0:
        print(f"- {proj['project_name']}: ${proj['funding']}")

print(f"\nTotal funding for park-related projects completed in 2022: ${total_funding}")

# Prepare final result
result = {
    'total_funding': total_funding,
    'project_count': len([p for p in matched_projects if p['funding'] > 0]),
    'details': matched_projects
}

print(f"\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
